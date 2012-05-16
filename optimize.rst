.. _optimize:

*********************************************
Optimizing Your Simulation
*********************************************

These simplistic simulations should not be overly taxing on a relatively recent desktop machine. However, you may likely want to develop simulations which have many more molecules possibly on large dense mesh objects. There are a couple of strategies you can use to speed up your simulation (and/or to save disk space). The following three topics will address some of these issues:

.. contents:: :local:

.. _adding_partitions:

Adding Partitions
---------------------------------------------

A full explanation of partitions is outside of the scope of this tutorial, but, essentially, when MCell is checking to see if a reaction occurs, partitions lower the number of potential partners it must check. For practical puprposes, partitions can greatly speed up your simulation, but, if used improperly, they can actually slow it down. Begin by creating a directory called **partitions** inside the main tutorial directory. Inside the **partitions** directory, create a file called **partitions.mdl** with the following text:

.. code-block:: none
    :emphasize-lines: 4-6

    ITERATIONS = 1000
    TIME_STEP = 5e-6

    PARTITION_X = [ [-1.0 TO 1.0 STEP 0.20] ]
    PARTITION_Y = [ [-1.0 TO 1.0 STEP 0.20] ]
    PARTITION_Z = [ [-1.0 TO 1.0 STEP 0.20] ]

    DEFINE_MOLECULES 
    {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol2 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol3 {DIFFUSION_CONSTANT_3D = 1E-6}
    }

    DEFINE_REACTIONS 
    {
        vol1 + vol2 -> vol1 + vol3 [1E7]
        vol1 + vol3 -> vol2 + vol3 [1E6]
    }

    INSTANTIATE World OBJECT 
    {
        Cube BOX {CORNERS = [-1.0,-1.0,-1.0],[1.0,1.0,1.0]}
        vol1_rel RELEASE_SITE 
        {
            SHAPE = World.Cube
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 2000
        }
        vol2_rel RELEASE_SITE 
        {
            SHAPE = World.Cube
            MOLECULE = vol2
            NUMBER_TO_RELEASE = 2000
        }
    }

The new thing of interest in this MDL is the **PARTITION** commands. Each of these three commands creates planes along the axis specified. The intersection of these planes create subvolumes. The distance of these subvolumes should generally not be smaller in length than the mean diffusion distance of the faster molecules in your simulation.

Run this MDL, and take note of the **Total wall clock time** reported by MCell. Then remove (or comment out) the partitions and run it again. The actual speed improvement will depend on the machine running it, but for the machine this example was tested on, it resulted in a speed increase of almost six times.

Although unrelated to partitions, note that instead of creating a **Cube** object with Blender, we simply used MCell's built in command (**BOX**) for creating one.

.. _target_only:

Target Only
---------------------------------------------

If you have a reaction between two molecules in which there are many of one molecule and very few of another, you might want to consider using the **TARGET_ONLY** command. Normally, a diffusing molecule will check to see if there are any potential molecules to react with. However, a molecule that is marked as **TARGET_ONLY** can only be the target of a reaction, and will not search for partners to react with. Create a directory called **target_only**. In that new directory, copy the following text into a file called **target_only.mdl**

.. code-block:: none
    :emphasize-lines: 9

    iterations = 500
    time_step = 5e-6
    ITERATIONS = iterations
    TIME_STEP = time_step

    DEFINE_MOLECULES 
    {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol2 {DIFFUSION_CONSTANT_3D = 1E-6 TARGET_ONLY}
        vol3 {DIFFUSION_CONSTANT_3D = 1E-6}
    }

    DEFINE_REACTIONS 
    {
        vol1 + vol2 -> vol1 + vol3 [1E8]
    }

    INSTANTIATE World OBJECT 
    {
        Cube BOX {CORNERS = [-1.0,-1.0,-1.0],[1.0,1.0,1.0]}
        vol1_rel RELEASE_SITE 
        {
            SHAPE = World.Cube
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 100
        }
        vol2_rel RELEASE_SITE 
        {
            SHAPE = World.Cube
            MOLECULE = vol2
            NUMBER_TO_RELEASE = 10000
        }
    }

In this case, **vol2** is marked as being **TARGET_ONLY** in the **DEFINE_MOLECULES** section. From the **DEFINE_REACTIONS** section, we can see that **vol1** reacts with **vol2** to create **vol3** and reproduce **vol1**. Without the **TARGET_ONLY** command, every **vol2** molecule would have to check to see if there were **vol1** molecules to react with and vice versa. With this command, *only* **vol1** must search for reaction partners. Given that there are 100 **vol1** and 10000 **vol2**, this second method is much more efficient.

.. _only_export_needed:

Only Export What You Need
---------------------------------------------

Visualization data can be great if you are making a figure to accompany a paper, or you are trying to troubleshoot a problem in your simulation, but there's probably no need to export everything at all times (**ALL_DATA @ ALL_ITERATIONS**). You could either comment out the **VIZ_OUTPUT** section entirely when you don't need it or only export what you need. This can speed up your simulation and save you disk space. The following **VIZ_OUPUT** sections illustrates how to selectively export visualization data.

.. code-block:: none
    :emphasize-lines: 7,8

    VIZ_OUTPUT 
    {
        MODE = ASCII
        FILENAME = "selective"
        MOLECULES 
        {
            NAME_LIST {vol1}
            ITERATION_NUMBERS {ALL_DATA @ [[100 TO 200 STEP 10]]}
        }   
    }   

The line **NAME_LIST {vol1}** indicates that we will only be exporting the molecule named **vol1**. The following line indicates that we will export it from iterations 100 to 200 at every 10 steps (i.e. 100, 110, ... 190, 200).

These are just examples of what you can do, and the actual list of molecules, meshes, and iterations that you export will depend entirely on your own needs for your specific simulation.

