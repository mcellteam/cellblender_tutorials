.. _checkpointing:

*********************************************
Checkpointing Overview
*********************************************

Checkpointing allows you to stop a simulation at a specified iteration and resume it at some later point. This can be beneficial for several different reasons:

* You are using any sort of multi-user system that you must share time with on with others
* The computer you are using crashes or is shutdown unexpectedly
* There are parameters you want to change partway through a simulation

We'll cover how to set up checkpointing in the next two sections, starting with a simple case where we modify a couple parameters. Then we will follow this up with a more interesting case where we have a mesh changing shape over time and molecules that will react to it.

.. contents:: :local:

.. _basic_checkpointing:

Basic Checkpointing
---------------------------------------------
inside of **/home/user/mcell_tutorial**, create a directory called **change_dc**. Inside that directory, create a file called **change_dc1.mdl**. Add the following text to that file::

    CHECKPOINT_INFILE = "dc_chkpt"
    CHECKPOINT_OUTFILE = "dc_chkpt"
    CHECKPOINT_ITERATIONS = 100 
    ITERATIONS = 200 
    TIME_STEP = 1E-6

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-7}
    }   

    INSTANTIATE World OBJECT {
        vol1_rel RELEASE_SITE {
            SHAPE = SPHERICAL
            LOCATION = [0,0,0]
            SITE_DIAMETER = 0.0 
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 100 
        }   
    }   

    VIZ_OUTPUT {
        FILENAME = "change_dc"
        MOLECULES {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }   
    } 

:index:`\ <single:CHECKPOINT_INFILE>` :index:`\ <single:CHECKPOINT_OUTFILE>` :index:`\ <single:CHECKPOINT_ITERATIONS>` There are three new commands in this file: **CHECKPOINT_INFILE**, **CHECKPOINT_OUTFILE**, and **CHECKPOINT_ITERATIONS**. As we mentioned earlier, checkpointing allows you to stop a simulation and resume it later. This is accomplished by means of a checkpoint file that is written (**CHECKPOINT_OUTFILE**) when the simulation is temporarily stopped and later read (**CHECKPOINT_INFILE**) when the simulation is resumed. The value assigned to these two commands is the name of the file that is written or read. In this case, they both have the same name, although that is not required. **CHECKPOINT_ITERATIONS** indicates at what iteration the simulation is temporarily stopped and the checkpoint file is created.

Now make a copy of **change_dc1.mdl** called **change_dc2.mdl** by entering the command::

    cp change_dc1.mdl change_dc2.mdl

Then change the diffusion constant from **1E-7** to **1E-5** in the second mdl. Once again, save and quit. Now run the first mdl by entering the command::

    mcell change_dc1.mdl

When it is finished running, enter the command::

    ls

Notice that a file called **dc_chkpt** was created. This file stores the information needed to recommence running the simulation. Let's finish it now by entering teh command::

    mcell change_dc2.mdl

Visualize the results with CellBlender. When you playback the animation, you will notice that the molecules start off moving rather slowly, and then speed up halfway through the simulation, coinciding with the change in diffusion constant.

This is just a simple example of one parameter you can change. Here is a partial list of some other parameters that you could change:

* **TIME_STEP**
* reaction rates
* **SURFACE_CLASS** properties (**ABSORPTIVE**, **TRANSPARENT**, **REFLECTIVE**)

.. _dynamic_mesh:

Checkpointing and Dynamic Meshes
---------------------------------------------
For this section, we will create a mesh in blender that grows every time step. We will export this animation as a series of MDLs. Then we can annotate these files to release a volume molecule inside of the changing mesh.

* `Creating the Animated Mesh in Blender`_
* `Annotating a Sequence of MDLs`_

.. _dynamic_mesh_blender:

Creating the Animated Mesh in Blender
+++++++++++++++++++++++++++++++++++++++++++++

Watch the following video tutorial or follow along with the instructions below.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/anim.ogg" type='video/ogg'/>
    </video>

If you watched the previous video tutorial, you can skip ahead to :ref:`dynamic_mesh`.

Open Blender. The Cube object should already be selected. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/scale_keyframe.png

Hit **i** to bring up the **Insert Keyframe Menu** and select **Scaling**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/frame_ten.png

Then click in the current frame marker and change it to **10**. Note: each frame in blender will count as one iteration in MCell. Hit **s** to scale, then **2** to make it twice the size, and **Enter** to confirm. Once again, hit **i** to bring up the **Insert Keyframe Menu** and select **Scaling**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/export_animation.png

Now select **File>Export>Model Description Language (.mdl)**. Navigate to **/home/user/mcell_tutorial/scaling** and select **OK** when it prompts you to make a new directory. Change the file name to **scaling.mdl**. Select **Enable Animation** and **Iterate Script**. Hit **Export MDL**.

.. _dynamic_mesh_mdl:

Annotating a Sequence of MDLs
+++++++++++++++++++++++++++++++++++++++++++++
Navigate to the directory where you just exported your MDLs. Type **ls** and hit **Enter**. You should notice that there are two different files for each frame or iteration of the animation. There is also one very simple python_ script which will iterate over each of the files with MCell. When you have a large number of files to edit, like we have here, you will almost certainly want to automate the task. This either means using a scripting language (python, ruby_, etc) or some command line tool like sed_ or awk_. Unfortunately, this can be a little intimidating for people who have never done any scripting before.

.. _python: http://www.python.org
.. _ruby: http://www.ruby-lang.org/en/
.. _sed: http://www.gnu.org/software/sed/manual/sed.html
.. _awk: http://www.gnu.org/software/gawk/manual/gawk.html

For this example, we can keep it fairly simple. All we need to do is add the same molecule definition (**DEFINE_MOLECULES { vol1 {DIFFUSION_CONSTANT_3D = 1E-6}}**) to ten files at line eleven. This can be accomplished by typing the following sed command at the terminal::

    sed -e "11aDEFINE_MOLECULES { vol1 {DIFFUSION_CONSTANT_3D = 1E-6}}\n" -i scaling_??.mdl

Now add the following text to the **INSTANTIATION** section of **scaling_01.mdl** after the **Cube** instantiation::

    vol1_rel RELEASE_SITE {
        SHAPE = World.Cube
        LOCATION = [0,0,0]
        SITE_DIAMETER = 0.0 
        MOLECULE = vol1
        NUMBER_TO_RELEASE = 100 
    }  

Now, at the command line enter the command::
    
    python scaling.py

After the simulation is done running, visualize the results with CellBlender. As in previous cases, the molecules stay within the box; the only difference now is that the box expands every iteration. For something more interesting and physiologically relevant, download this `expanding pore`_ example.

.. _expanding pore: http://mcell.psc.edu/tutorials/mdl/expanding_pore.tgz

