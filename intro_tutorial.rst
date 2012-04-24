*************************
An Introduction to MCell
*************************
Overview
=========================

In order to quickly show what can be done with MCell, we'll begin by generating a simple model and gradually add in more features. Our initial model will contain a cube that has diffusing surface and volume molecules that react with each other to create new molecules. Later, we'll add more complex reactions and surface properties. At that point, we'll begin to move on to some more advanced topics, like optimizing a simulation and analyzing data.

Much of the theory will be skipped over, as it's available elsewhere_. For a more detailed explanation of any given topic, please see the `quick reference guide`_. 

The completed project files for the tutorial can be downloaded here_. You will generate these same files simply by following along with the tutorial, but they are provided here in case you need them for any reason.

.. _elsewhere: https://www.mcell.psc.edu/publications.html

.. _quick reference guide: http://mcell.psc.edu/download/files/mcell3_qrg_092010.pdf

.. _here: https://www.mcell.psc.edu/tutorials/mdl/main/mcell_tutorial.tgz

* `Software Needed`_
* `Generate Mesh and Export MDL with Blender`_
* `Run the Simulation`_
* `Visualize the Mesh`_
* `Annotate the MDL`_

  * `Examining the MDL`_
  * `Initialization Commands`_
  * `Molecule Definitions`_
  * Reactions_
  * `Reaction Directionality`_
  * `Release Sites`_
  * `Reaction Data`_

* `Run the Simulation again`_
* `Visualize the Molecules`_
* `Customize Rendering Properties`_
* `Graph the Reaction Data`_
* `Surface Classes and Volume Molecules`_

  * `Modify the Mesh`_
  * `Modify the MDL`_

* `Surface Classes and Reactions`_

  * `More Mesh Modifications`_
  * `More MDL Modifications`_

* `Variable Reaction Rates`_
* `Surface Classes and Surface Molecules`_

  * `Creating the Mesh`_
  * `Modifying the MDL`_

* `Checkpointing Overview`_

  * `Basic Checkpointing`_
  * `Checkpointing and Dynamic Meshes`_

    * `Creating the Animated Mesh in Blender`_
    * `Annotating a Sequence of MDLs`_

* `Release Patterns`_
* `Clamp Concentration`_
* `Optimizing Your Simulation`_

  * `Adding Partitions`_
  * `Target Only`_
  * `Only Export What You Need`_

* `Analyzing Your Data`_
* `Running Multiple Seed Values`_

Software Needed
========================
To use this tutorial, you'll want to have the following software installed:

* MCell_ (registration required)
* DReAMM_ (registration required)
* Blender_
* `Blender MDL export plugin`_
* A text editor (gedit_, vim_, emacs_, etc.)
* Some graphing and analysis software (matplotlib_ (with python_ and numpy_), Grace_, gnuplot, etc.)

.. _MCell: http://mcell.psc.edu/download.html
.. _DReAMM: http://mcell.psc.edu/download.html
.. _Blender: http://www.blender.org/download/get-blender/
.. _Blender MDL export plugin: http://mcell.psc.edu/download/files/io_mesh_mdl.tgz
.. _gedit: http://projects.gnome.org/gedit/
.. _vim: http://www.vim.org/
.. _emacs: http://www.gnu.org/software/emacs/
.. _matplotlib: http://matplotlib.sourceforge.net/
.. _python: http://www.python.org
.. _numpy: http://numpy.scipy.org/
.. _Grace: http://plasma-gate.weizmann.ac.il/Grace/

This tutorial assumes you are using either some version of linux (e.g. Ubuntu_) or OSX as your operating system. It also requires that you have some basic familiarity with the command line. There are many tutorials online that explain the basics, like `this one`_. Although no previous knowledge of Blender, DReAMM, or python is required, the goal of this tutorial is not to teach these topics. There are already many good resources available to learn about these subjects.

.. _Ubuntu: http://www.ubuntu.com/download
.. _this one: http://www.tuxfiles.org/linuxhelp/linuxfiles.html

Generate Mesh and Export MDL with Blender
=============================================

The majority of this tutorial can be easily accomplished by following along with the text. However, sections that rely heavily on a GUI (like this one), might be better understood by watching a video tutorial.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/blender_pt1.ogg" type='video/ogg'/>
    </video>

You can skip to the next section (`Run the Simulation`_) if you have watched the previous video tutorial. Otherwise, follow along with the rest of the directions in this section. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/cube.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/material_button.png

Open up a terminal and type **blender**. You should see a cube in the **3D View Window**. Hit the **Material** button in the **Properties Window**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/plus_button.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/new_button.png

Hit the **+** button and then the **New** button. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/top.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/sides_and_bottom.png

Change the newly created material text field from **Material.001** to **top**. Left click **Material** in the list of materials. Change the text field from **Material** to **sides_and_bottom**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/face_select.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/right_click.png

Move the cursor to the **3D View Window**. Hit **Tab** to change into **Edit Mode**. Hit **Ctrl-Tab** and select **Face**. Then **right click** on the top face to select it.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/assign.png

Select the **top** material from the list of materials. Click **Assign**. Hit **Tab** to change back into **Object Mode**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/export_mdl.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/export_mdl_dir.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/export_mdl_button.png

Next, select **File>Export>Model Description Language (.mdl)**. Navigate to the directory where we will export the files (**/home/user/mcell_tutorial/intro** where **user** is your user name) and select **OK** when it prompts you to make a new directory. In the text field below the directory, type **intro.mdl** and hit **Export MDL**.

Either leave Blender open or save and quit, as we'll need to modify this model later.

Run the Simulation
=============================================

.. _tut_viz_data1.tgz: http://mcell.psc.edu/tutorials/mdl/main/tut_viz_data1.tgz

Let's verify that this simple case works with MCell before adding in more details.

At the command line, navigate to the appropriate directory (**/home/user/mcell_tutorial/intro**), type **mcell intro.mdl**, and hit **Enter**. MCell should output some information to the command line indicating that it ran successfully. Type **ls** and you should see that a directory called **intro_viz_data** has been created.

Visualize the Mesh
=============================================

As with the Blender section, this section requires extensive use of a GUI, so you may find it easier to follow along with this video tutorial.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/dreamm_pt1.ogg" type='video/ogg'/>
    </video>

You can skip to the next section (`Annotate the MDL`_) if you have watched the previous video tutorial. Otherwise, follow along with the rest of the directions in this section. 

To start DReAMM, open a terminal, type **dreamm**, and hit **Enter**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/import_select.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/ellipsis.png

Hit **Import & Select** on the **Quick Controls** window. Click the ellipsis (**...**) on the **Import & Select Objects** window. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/enter_dir.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/load_dx.png

Navigate to the directory where you ran the mdl. Double click on the **tutorial_viz_data** directory and then double click on **tutorial.dx**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/select_wireframes.png

Select **World.Cube** in the **Import & Select Objects** window. Click **Apply Operation**, and the cube object should appear in the  **DReAMM Image Window**. 

**Left click** in the **DReAMM Image Window** and hit **Ctrl-f** to center the cube.

Leave DReAMM open as we'll return to it shortly.

Annotate the MDL
=============================================
Open **intro.mdl** with your favorite text editor (try gedit or kedit if you aren't sure what to use).

- `Examining the MDL`_
- `Initialization Commands`_
- `Molecule Definitions`_
- Reactions_
- `Reaction Directionality`_
- `Release Sites`_
- `Reaction Data`_

Examining the MDL
---------------------------------------------

Before we start making changes, let's *briefly* look at what we have to start with::

    iterations = 1
    time_step = 1e-6
    ITERATIONS = iterations
    TIME_STEP = time_step

    INCLUDE_FILE = "./intro_Cube.mdl"

    INSTANTIATE World OBJECT {
        Cube OBJECT Cube{}
    }

    VIZ_OUTPUT {
        FILENAME = "tutorial"
        MOLECULES {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }
        MESHES {
            NAME_LIST {ALL_MESHES}
            ITERATION_NUMBERS {ALL_DATA @ [1]}
        }
    }

The first four lines are some `Initialization Commands`_ that we'll cover in the next section.

**INCLUDE_FILE** commands let you break up MDLs into multiple sections. In this particular instance, the vertices and faces that make up our **Cube** are being imported or *included*.

In addition to simply *including* meshes, you also have to **INSTANTIATE** meshes to make them exist and interact in the simulation. We'll see later that we can also instantiate other types of objects, like molecule `Release Sites`_.

Lastly, the **VIZ_OUTPUT** section specifies what visualization data to export and at what time values. Right now, it is set to export everything. 

Initialization Commands
---------------------------------------------
At the beginning of the mdl, there are two variables **time_step** and **iterations**. These variables are applied to the initialization commands **TIME_STEP** and **ITERATIONS** respectively. As the names imply, these commands control how many **ITERATIONS** the simulation runs for, with each iteration lasting one **TIME_STEP** (units are seconds). 

At the beginning of the mdl, change **iterations** from **1** to **1000** and **time_step** from **1e-6** to **5e-6**. This means that the simulation will run for 1000 iterations at a time step of **5e-6** seconds (total time: 1000*5e-6=5e-3 seconds).

::

    iterations = 1000
    time_step = 5e-6
    ITERATIONS = iterations
    TIME_STEP = time_step

Molecule Definitions
---------------------------------------------
Molecules need to be defined before they are used (as a release site or a reaction) in the MDL.

After the **INCLUDE_FILE** command, add a **DEFINE_MOLECULES** section as shown here::

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol2 {DIFFUSION_CONSTANT_3D = 1E-6}
        surf1 {DIFFUSION_CONSTANT_2D = 1E-7}
    }

Molecules that use **DIFFUSION_CONSTANT_3D** command, like **vol1** and **vol2**, will be volume molecules, meaning that they will exist in solution. Molecules that use **DIFFUSION_CONSTANT_2D**, like **surf1**, will be surface molecules, meaning that they exist on a surface. The units of the values assigned to this command (**1E-6** and **1E-7** in this instance) are in cm\ :sup:`2`\ /s. 

Reactions
---------------------------------------------
Molecules that were defined in the previous section can be created and destroyed in a number of different ways using reactions. A reaction is defined in the following manner:

**reactant(s) -> product(s) [rate]**

This means that **reactant(s)** are converted into **product(s)** at a given **rate**.

There must be one or more molecules on the left hand  **reactants** side. On the right hand **products** side, you must have zero (**NULL**) or more molecules. The units of the **rate** depend on the type of reaction. [s\ :sup:`-1`\ ] for unimolecular reactions and [M\ :sup:`-1`\ s\ :sup:`-1`\ ] for bimolecular reactions between two volume molecules or a volume molecule and a surface molecule.

Reaction Directionality
---------------------------------------------

Surface molecules have a **TOP** and a **BOTTOM**, so we need a way to differentiate between reactions that happen on one side versus the other. Commas (**,**), ticks (**'**), and semi-colons (**;**) serve this purpose. For detailed information on this reaction syntax, please refer to this pdf_. Let's look at a relatively simple example. First, add this code after the **DEFINE_MOLECULES** section::

    DEFINE_REACTIONS {
        vol1, + surf1' -> surf1' + vol2' [1E8]
    }

.. _pdf: http://mcell.psc.edu/download/files/MCell3_rxns_06_18_2007.pdf

Read this next section carefully, as some people find this syntax confusing at first. If a volume molecule and a surface molecule have their orientations *opposed* (i.e. a tick and a comma), then the volume molecule interacts with the **BOTTOM** of the surface molecule. If a volume molecule and a surface molecule have their orientations *aligned* (i.e. two ticks *or* two commas), then the volume molecule interacts with the **TOP** of the surface molecule. 

For this reaction, **vol1** and **surf1** are opposed (a comma and a tick), and **vol2** and **surf1** are aligned (two ticks). This means that **vol1** will react with the **BOTTOM** of **surf1**, creating **vol2** at the **TOP** of **surf1**. Since **vol1** is not on the products side, it is destroyed when it reacts with **surf1**. Conversely, **surf1** is on both the **reactant** and **product** side, so it will not be destroyed from the reaction.

The directionality of these ticks and commas are relative, which means that we could flip the signs and get the same result, like this::

    DEFINE_REACTIONS {
        vol1' + surf1, -> surf1, + vol2, [1E8]
    }

Release Sites
---------------------------------------------

*Modify* the **INSTANTIATE** section of the MDL so it looks like this::

    INSTANTIATE World OBJECT {
        Cube OBJECT Cube{}
        vol1_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 2000
        }
        surf1_rel RELEASE_SITE {
            SHAPE = World.Cube[top]
            MOLECULE = surf1'
            NUMBER_TO_RELEASE = 2000
        }
    }

*Note*: Don't just add this section in or you will have two **INSTANTIATE** sections.

This section creates two release sites, one called **vol1_rel** and the other **surf1_rel**. Each release site can take a number of different commands. 

The **SHAPE** of the release determines what object (or region of an object) that molecules are released onto or into. You can also use some predefined shapes, like **CUBIC** or **SPHERICAL**, but we won't cover that here.

**MOLECULE** determines what molecule is released. If it is a surface molecule, an orientation is also specified This is similar to what's described in `Reaction Directionality`_, but it is not relative. A tick means that the **TOP** of the molecule is aligned with the **FRONT** of the surface, and a comma means that the **TOP** is aligned with the **BACK** of the surface.

**NUMBER_TO_RELEASE** gives an absolute number of molecules to be released. Alternatively, one could define a **CONCENTRATION** or **DENSITY**.

These two release sites together will release 1000 **vol1** molecules randomly throughout the inside of **World.Cube** and also 5000 **surf1** molecules randomly on the **top** surface region of **World.Cube**. Also, the **TOP** of **surf1** will be aligned with the **FRONT** of the surface.

Reaction Data
---------------------------------------------
At the end of the MDL, add the following::

    REACTION_DATA_OUTPUT {
        STEP=time_step
        {COUNT[vol1,WORLD]}=> "./react_data/vol1.dat"
        {COUNT[vol2,WORLD]}=> "./react_data/vol2.dat"
    }

The **STEP** command tells MCell how often it should write out reaction data.

The brackets after the **COUNT** command tell MCell what molecule to count and where to count it. For instance the first **COUNT** statement tells it to count all of the **vol1** molecules in the **WORLD** (the entire simulation). Alternatively, you could specify that it only count those found in/on an object/region (e.g. **[vol1,World.Cube]**) 

The file listed after the arrow symbol (**=>**) tells it where to save it. 

Run the Simulation again
=============================================
We've finished adding our changes. Let's rerun the simulation with MCell.

As before, navigate to the appropriate directory, type **mcell intro.mdl**, and hit **Enter**. After it's finished running, type **ls** and you should see that a new directory called **react_data** has been created.

Visualize the Molecules
=============================================

Visualize molecules with DReAMM in this video tutorial.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/dreamm_pt2.ogg" type='video/ogg'/>
    </video>

Skip to the next section (`Customize Rendering Properties`_) if you just watched the video tutorial.

If you still have DReAMM open, hit the **Reimport** button and add the wireframe for **World.Cube** in the same way that you did in `Visualize the Mesh`_. If you closed DReAMM, simply follow all the steps in `Visualize the Mesh`_ again. When you are finished, you should have the centered cube in the middle of the **DReAMM Image Window**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/volume_molecules.png

Select **Volume Molecules** in the **Import & Select Objects** window. Next, select **Add Filtered**. Click **Apply Operation**, and the volume molecules should appear in the  **DReAMM Image Window**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/surface_molecules.png

Select **Surface Molecules** in the **Import & Select Objects** window. **Add Filtered** should still be selected. Click **Apply Operation**, and the surface molecules should appear in the **DReAMM Image Window**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/play.png

Hit the Play button on the Sequencer and watch the molecules diffusing and reacting in the **DReAMM Image Window**.

*Note:* The "up" axis is the Z-axis in Blender, but the Y-axis in DReAMM, meaning that the **top** surface region is pointing straight toward you. You will probably want to rotate it to get a better view. **Left click** in the **DReAMM Image Window** and hit **Ctrl-R**. Now **left click and drag** upward until the **top** region is facing up. 

Customize Rendering Properties
=============================================

Learn how to customize rendering properties with DReAMM in this video tutorial.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/dreamm_rendering.ogg" type='video/ogg'/>
    </video>

Skip to the next section (`Graph the Reaction Data`_) if you just watched the video tutorial.

By default, every molecule just shows up as a white pixel. This might be fine if you only have one molecule in your simulation, but, for anything more complicated, you will probably want to be able to differentiate between them.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/set_rendering_prop.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/select_molecules.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/select_vol1.png

Hit the **Set Rendering Prop.** button. Select **Molecules** and then **vol1.**

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/set_red.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/sphere_height_radius.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/apply_op_once.png

Set the **(Front) Color** RGB values to **1,0,0** (for red). Change **Glyph** to **sphere(simple)**. Change **Height** and **Radius** to **0.02**. The hit the **Apply Operation Once** button. You should notice the change in the **DReAMM Image Window**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/select_vol2.png

Select **vol2** and deselect **vol1**. Change  the RGB value of the **(Front) Color** to **0,1,0** (for green). Hit **Apply Operation Once**. *Note*: The specific colors and values don't matter as long as we can easily tell everything apart.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/set_cyan.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/arrow.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/apply_op_once.png

Finally, we are going to add **surf1**, but we have a few more changes to make with this one since it is a surface molecule, and therefore has a directionality to it. First, select **surf1** and deselect **vol2**. Then change the RGB value to **0,1,1** (for cyan). Change the **Glyph** to **arrow(simple)**. Then, change the **Height** and **Radius** to **0.10** and **0.02** respectively. Finally, hit **Apply Operation Once**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/play.png

Hit the Play button on the Sequencer and watch the molecules diffusing and reacting in the **DReAMM Image Window**.

Graph the Reaction Data
=============================================

Change into the **react_data** directory (**cd react_data**) and type **ls**. You should see two files, **vol1.dat**, and **vol2.dat**.

Plot **vol1.dat** and **vol2.dat** with the graphing software of your choice. For something as simple as this, xmgrace or gnuplot will suffice. Although we don't need all the power (and complexity) of numpy and matplotlib right now, we'll introduce it here anyways, since we will be using it for some more advanced tasks later. First create a file called **plot.py** and put the following text into it::

    #!/usr/bin/env python

    import numpy as np
    import matplotlib.pyplot as plt 

    x1 = np.genfromtxt("./react_data/vol1.dat",dtype = float)[:,0]
    y1 = np.genfromtxt("./react_data/vol1.dat",dtype = float)[:,1]
    x2 = np.genfromtxt("./react_data/vol2.dat",dtype = float)[:,0]
    y2 = np.genfromtxt("./react_data/vol2.dat",dtype = float)[:,1]
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.show()

Run the file by typing **python plot.py**. You should notice that **vol1.dat** is decreasing and **vol2.dat** is increasing as expected. This can be a quick way to verify that our simulation is working as expected.

Surface Classes and Volume Molecules
=============================================

Surface classes allow various properties (e.g. **ABSORPTIVE**, **TRANSPARENT**) to be applied to surfaces, which can affect specified molecules. 

Begin by creating a copy of the **intro** directory, by typing the following command at the terminal: **cp -fr /home/user/mcell_tutorial/intro /home/user/mcell_tutorial/surf_class** (don't forget to replace **user** with your actual user name).

Modify the Mesh
---------------------------------------------

Watch the following video tutorial or follow along with the instructions below.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/export_above.ogg" type='video/ogg'/>
    </video>

If you watched the previous video tutorial, you can skip ahead to `Surface Classes and Volume Molecules`_.

In order to complete the next section (`Surface Classes and Volume Molecules`_), we first have to make a few simple changes to our Blender model. We'll pick up right where we left off in `Generate Mesh and Export MDL with Blender`_. Hit **z** to switch to a wireframe view. Hit **Shift-a** and select **Plane**. Hit **g** to "grab" the plane, **z** to constrain the movement to the z-axis, **1.5** to move it 1.5 units, and **Enter** to confirm.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/new_mat_plane.png

Hit the **New** button in the **Materials** section of the **Properties** window. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/mat_above.png

Change the newly created material text field from **Material** to **above**. Click **Assign**. 

Next, select **File>Export>Model Description Language (.mdl)**. Deselect **Instantiate & Viz** so that we only export the new meshes and don't override the changes in **intro.mdl**. Navigate to the directory where you want to create your file (e.g. **/home/user/mcell_tutorial/surf_class**). In the text field below the directory, type **intro.mdl** and hit **Export MDL**.

Modify the MDL
---------------------------------------------

Open **intro.mdl** in the new **surf_class** directory. After the first **INCLUDE** command, add this::

    INCLUDE_FILE = "./intro_Plane.mdl"

Before the **DEFINE_REACTIONS** section, add the following::

    DEFINE_SURFACE_CLASSES {
        absorb_vol2 {ABSORPTIVE = vol2}
    }

The command above creates a surface class called **absorb_vol2**. Since **vol2** is the value set to the **ABSORPTIVE** command, this means that any **vol2** molecules that touch a surface that has the **absorb_vol2** surface class will be destroyed.

Now we actually have to apply the surface class to a surface region. After the **DEFINE_REACTIONS** section, add the following::

    MODIFY_SURFACE_REGIONS {
        Plane[above] {
            SURFACE_CLASS = absorb_vol2
        }   
    }

Finally, we need to instantiate our new **Plane** object, so add the following line before the **Cube** instantiation (i.e. before **Cube OBJECT Cube{}**)::

        Plane OBJECT Plane{}

That's all there is to it. The other two surface class commands are **REFLECTIVE** (the default state for surfaces) and **TRANSPARENT** (allows molecules to freely pass through). Feel free to try these out on your own.

Save the file and run it with MCell (type **mcell intro.mdl** and hit **Enter** at the command line). Visualize the results with DReAMM just like was done in the `Visualize the Mesh`_ and `Visualize the Molecules`_ sections, except you should be sure to also add the new **Plane** object as a wireframe. See if you can notice the  **vol2** molecules being destroyed by the absorptive surface.

Surface Classes and Reactions
=============================================
In the `Surface Classes and Volume Molecules`_ section, we learned that surface classes can be used to give parts of meshes special properties. Surface classes can also be used to provide extra specificity over how reactions occur. Begin by creating a copy of the **surf_class** directory, by typing the following command at the terminal: **cp -fr /home/user/mcell_tutorial/surf_class /home/user/mcell_tutorial/surf_class_rxns** (don't forget to replace **user** with your actual user name).

More Mesh Modifications
---------------------------------------------

Watch the following video tutorial or follow along with the instructions below.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/export_inside.ogg" type='video/ogg'/>
    </video>

If you watched the previous video tutorial, you can skip ahead to `Surface Classes and Reactions`_.

We need to make a few more changes to our Blender model to complete the next section (`Surface Classes and Reactions`_). We're picking up where we left off in `Modify the Mesh`_. In fact, the instructions will be very similar, aside from few minor changes. While still in **Object Mode**, hit **Shift-a**, select **Plane**, and **Enter** to confirm.  

Hit the **New** button in the **Materials** section of the **Properties** window. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/new_mat_plane2.png

Change the newly created material text field from **Material** to **inside**. Click **Assign**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/mat_inside.png

Next, select **File>Export>Model Description Language (.mdl)**. *Deselect* **Instantiate & Viz** to indicate that we *only* want to export the mesh object. Navigate to the directory where you want to create your file (e.g. **/home/user/mcell_tutorial/surf_class_rxns**). In the text field below the directory, type **intro.mdl** and hit **Export MDL**.

More MDL Modifications
---------------------------------------------

Open **intro.mdl** in the new **surf_class_rxns** directory. After the first **INCLUDE** command, add this::

    INCLUDE_FILE = "./intro_Plane.001.mdl"

Modify the **DEFINE_MOLECULES** section like this::

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol2 {DIFFUSION_CONSTANT_3D = 1E-6}
        surf1 {DIFFUSION_CONSTANT_2D = 1E-7}
        surf2 {DIFFUSION_CONSTANT_2D = 0}
    }  

Change the **DEFINE_SURFACE_CLASSES** section as follows::

    DEFINE_SURFACE_CLASSES {
        absorb_vol1 {ABSORPTIVE = vol1}
        empty {}
    }  

This new surface class, **empty**, is the simplest case you can have for a surface class. By itself, it's not very useful, but we can use it in reactions. Modify the **DEFINE_REACTIONS** section as follows::

    DEFINE_REACTIONS {
        vol1, + surf1' -> surf1' + vol2' [1E8]
        vol1, + surf2' @ empty' -> surf2' + vol2' [1E8]
    }   

The above change means that **vol1** will only react with the **BOTTOM** of **surf** at the **BACK** of the **empty** surface class. This means the reaction won't occur when the surface molecules diffuse away from surface regions that have this surface class applied (i.e. when it diffuses from **top** to **sides_and_bottom**). Lastly, change the **MODIFY_SURFACE_REGIONS** section like this::

    MODIFY_SURFACE_REGIONS {
        Plane[above] {
            SURFACE_CLASS = absorb_vol1
        }
        Plane.001[inside] {
            SURFACE_CLASS = empty
        }
    }

Lastly, we need to instantiate our new **Plane.001** object and add in a release site for **surf2**, so modify the **INSTANTIATE** section like this::

    INSTANTIATE World OBJECT {
        Plane OBJECT Plane{}
        Plane.001 OBJECT Plane.001{}
        Cube OBJECT Cube{}
        vol1_rel RELEASE_SITE intro{
            SHAPE = World.Cube
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 2000
        }   
        surf1_rel RELEASE_SITE {
            SHAPE = World.Cube[top]
            MOLECULE = surf1'
            NUMBER_TO_RELEASE = 2000
        }   
        surf2_rel RELEASE_SITE {
            SHAPE = World.Plane.001[inside]
            MOLECULE = surf2;
            NUMBER_TO_RELEASE = 2000
        }   
    }   

Save the file and run it with MCell (type **mcell intro.mdl** and hit **Enter** at the command line). When you visualize the results with DReAMM, be sure to add in **Plane.001** as a wireframe and **surf2** as a surface molecule. You might also want to add in custom rendering properties for **surf2**. You should notice that there are **vol2** molecules being created inside the box, but only in the upper portion of it, despite the fact that the **surf2** molecules are facing both up *and* down. The reason for this is because the reaction is only taking place at the **BACK** of the **empty** surface class with the **BOTTOM** of **surf2**.

Variable Reaction Rates
=============================================

Begin by creating a copy of the **surf_class_rxns** directory, by typing the following command at the terminal: **cp -fr /home/user/mcell_tutorial/surf_class_rxns /home/user/mcell_tutorial/var_rxn_rate** (don't forget to replace **user** with your actual user name). In the new **var_rxn_rate** directory, create a new text file called **rxn_rate.txt**. Add the following text in the file::

    0      0
    5E-4   1E8

The first column is the time (seconds), and the second column is the reaction rate at that time. The units for the reaction rate are the same as used earlier in the Reactions_ section. 

The example shown above is a very simple case where the reaction only changes once. You could just as well have it change every time step, like this::

    0      0
    1E-6   1.0E5
    2E-6   1.1E5
    3E-6   1.2E5
    ...

Save the file and quit. In **intro.mdl**, go to the reaction section and change the rate to **"rxn_rate.txt"** (with quotations), like in the following::

    DEFINE_REACTIONS {
        vol1, + surf1' -> surf1' + vol2' ["rxn_rate.txt"]
        vol1, + surf2' @ empty' -> surf2' + vol2' ["rxn_rate.txt"]
    }   

Save the file and run it with MCell (type **mcell intro.mdl** and hit **Enter** at the command line).

Surface Classes and Surface Molecules
=============================================

We have already discussed surface classes at length, but we haven't touched on how they can affect the diffusion of surface molecules. Their effects are manifested at the boundaries of the surface regions that they are applied to. For example, if a surface is **REFLECTIVE** to **surf1**, then any **surf1** can't get in or out of that that surface region. It acts as a fence of sorts corralling the molecules in one region. The **ABSORPTIVE** surface class also acts somewhat like a fence, but, instead of molecules harmlessly "bouncing" off of it, they are destroyed whenever they touch it. **TRANSPARENT** surface classes don't affect surface molecules, so we can ignore them in this context.

Since our current MDL is beginning to get a little complicated, we will start fresh with this next example. First, we need to create the mesh and export the MDL. Then, we will modify the MDL.

* `Creating the Mesh`_
* `Modifying the MDL`_

Creating the Mesh
---------------------------------------------

Let's look at an example. First we need to create the model in Blender. To do this, either watch the following video tutorial or follow along with the instructions below.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/sc_sm.ogg" type='video/ogg'/>
    </video>

Start Blender. Hit the **Material** button in the **Properties** window. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/plus_button.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/new_button.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/two_new_mats.png

Hit **New**, **+**, and then repeat these two steps again, so that you have two new materials (and three total). 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/renamed_mats.png

Click on the top one (**Material**) and change its name in the text field to **middle**. Change **Material.001** to **top** and change **Material.002** to **bottom**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/face_select.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/right_click.png

Move your cursor to the **3D View* window and hit **Tab** to switch into **Edit Mode**. Then hit **Ctrl-Tab** and select **Face**. Right click on the top face, select the **top** material, and click **Assign**. Next move your mouse back to the **3D View** window and hold the middle mouse button down and drag upward so that the bottom face is shown. Right click on the bottom face, select **bottom** from the list of materials, and click **Assign**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/export_mdl.png

Now select **File>Export>Model Description Language (.mdl)**. Navigate to **/home/user/mcell_tutorial/sc_sm**. Change the file name to **sc_sm.mdl** and hit **Export MDL**.

Modifying the MDL
---------------------------------------------

Modify the first two lines like this::

    iterations = 1000
    time_step = 1e-5

Next, add the following text after the **INCLUDE_FILE** command::

    DEFINE_MOLECULES {
        surf1 {DIFFUSION_CONSTANT_2D = 1E-7}
    }

    DEFINE_SURFACE_CLASSES {
        absorb {ABSORPTIVE = surf1}
        reflect {REFLECTIVE = surf1}
    }  

    MODIFY_SURFACE_REGIONS {
        Cube[top] {
            SURFACE_CLASS = absorb
        }   
        Cube[bottom] {
            SURFACE_CLASS = reflect
        }   
    }

Modify the **INSTANTIATE** section like this::

    INSTANTIATE World OBJECT {
        Cube OBJECT Cube{SCALE = [0.1,0.1,0.1]}
        surf1_top_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = surf1'
            NUMBER_TO_RELEASE = 1000
        }   
    }



In this example, we have two surface classes, **absorb** and **reflect**. **absorb** is applied to **top** and **reflect** is applied to **bottom**. **surf1** molecules are released all over the **Cube**, not just one surface region. The effect of the **absorb** class is that all the **surf1** molecules are destroyed when they hit the boundary between the **top** and **middle** region. The effect of the **reflect** class is that molecules cannot pass the boundary between the **bottom** and the **middle** region. Therefore, all the **surf1** molecules that start inside of the **bottom** region never escape and the **surf1** molecules starting in the **middle** and **top** region will ultimately be destroyed.

Checkpointing Overview
=============================================
Checkpointing allows you to stop a simulation at a specified iteration and resume it at some later point. This can be beneficial for several different reasons:

* You are using any sort of multi-user system that you must share time with on with others
* The computer you are using crashes or is shutdown unexpectedly
* There are parameters you want to change partway through a simulation

We'll cover how to set up checkpointing in the next two sections, starting with a simple case where we modify a couple parameters. Then we will follow this up with a more interesting case where we have a mesh changing shape over time and molecules that will react to it.

* `Basic Checkpointing`_
* `Checkpointing and Dynamic Meshes`_

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

Save and quit. Now make a copy of this file called **change_dc2.mdl**. Then change the diffusion constant from **1E-7** to **1E-5** in the second mdl. Once again, save and quit. Now run the first mdl by typing **mcell change_dc1.mdl** at the command line. When it is finished, type **ls** and notice that a file called **dc_chkpt** was created. This file stores the information needed to recommence running the simulation. Let's finish it now by typing **mcell change_dc2.mdl**. Visualize the results with DReAMM. When you playback the animation, you will notice that the molecules start off moving rather slowly, and then speed up halfway through the simulation, coinciding with the change in diffusion constant.

This is just a simple example of one parameter you can change. Here is a partial list of some other parameters that you could change:

* **TIME_STEP**
* reaction rates
* **SURFACE_CLASS** properties (**ABSORPTIVE**, **TRANSPARENT**, **REFLECTIVE**)

Checkpointing and Dynamic Meshes
---------------------------------------------
For this section, we will create a mesh in blender that grows every time step. We will export this animation as a series of MDLs. Then we can annotate these files to release a volume molecule inside of the changing mesh.

* `Creating the Animated Mesh in Blender`_
* `Annotating a Sequence of MDLs`_

Creating the Animated Mesh in Blender
+++++++++++++++++++++++++++++++++++++++++++++

Watch the following video tutorial or follow along with the instructions below.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/anim.ogg" type='video/ogg'/>
    </video>

If you watched the previous video tutorial, you can skip ahead to `Annotating a Sequence of MDLs`_.

Open Blender. The Cube object should already be selected. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/scale_keyframe.png

Hit **i** to bring up the **Insert Keyframe Menu** and select **Scaling**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/frame_ten.png

Then click in the current frame marker and change it to **10**. Note: each frame in blender will count as one iteration in MCell. Hit **s** to scale, then **2** to make it twice the size, and **Enter** to confirm. Once again, hit **i** to bring up the **Insert Keyframe Menu** and select **Scaling**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/export_animation.png

Now select **File>Export>Model Description Language (.mdl)**. Navigate to **/home/user/mcell_tutorial/scaling** and select **OK** when it prompts you to make a new directory. Change the file name to **scaling.mdl**. Select **Enable Animation** and **Iterate Script**. Hit **Export MDL**.

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

Now, at the command line type **python scaling.py**. After the simulation is done running, visualize the results with DReAMM. Add the **Cube** as a wireframe and **vol1** as a volume molecule. As in previous cases, the molecules stay within the box; the only difference now is that the box expands every iteration. For something more interesting and physiologically relevant, download this `expanding pore`_ example.

.. _expanding pore: http://mcell.psc.edu/tutorials/mdl/expanding_pore.tgz

Release Patterns
=============================================
Release patterns allow you to release molecules at specified time intervals. One thing this can be useful for is simulating a synaptic vesicle releasing neurotransmitter. First, create a directory called **release_pattern** in the main tutorial directory. Inside the new directory, create a file called **release_pattern.mdl** and add the following text to it::

    time_step = 1E-6 
    iterations = 1000 
    ITERATIONS = iterations
    TIME_STEP = time_step

    DEFINE_RELEASE_PATTERN rel_pat1 {
        DELAY = 50E-6
        RELEASE_INTERVAL = 50E-6
        TRAIN_DURATION = 200E-6
        TRAIN_INTERVAL = 300E-6
        NUMBER_OF_TRAINS = 3
    } 

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
    }

    DEFINE_REACTIONS {
        vol1 -> NULL [1E5]
    }

    INSTANTIATE World OBJECT {
        vol1_rel RELEASE_SITE {
            SHAPE = SPHERICAL
            LOCATION = [0,0,0]
            SITE_DIAMETER = 0.0
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 100
            RELEASE_PATTERN = rel_pat1
        }
    }

    VIZ_OUTPUT {
        FILENAME = "release_pattern"
        MOLECULES {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }
    }
    REACTION_DATA_OUTPUT {
        STEP=time_step
        {COUNT[vol1,WORLD]}=> "./react_data/vol1.dat"
    }

A release pattern consists of one or more "trains." Each train can last for a certain period of time (**TRAIN_DURATION**), and an interval between trains can be set(**TRAIN_INTERVAL**). Within a given train, you can release molecules at specific intervals (**RELEASE_INTERVALS**). And lastly, the **DELAY** indicates when the first train will start. This may sound more confusing than it really is. Plotting the reaction data should help illustrate what's happening for this specific release pattern.

Clamp Concentration
=============================================
Clamp concentration lets you maintain a constant concentration of a molecule at a surface. This is done by creating and destroying molecules at the surface. **CLAMP_CONC** is created and applied like other surface classes (e.g. **ABSORPTIVE**). We'll begin by making two meshes, one which will have the **CLAMP_CONC** applied and the other will prevent molecules from diffusing away from the surface.

Start Blender. Hit **z** to switch to wireframe mode. With the **Cube** selected, hit **s**, **z**, **0.1**, and **Enter**. Hit **Shift-a**, select **Mesh>Plane**. Hit **s**, **0.9**, and **Enter**. Hit the **Material** button in the **Properties** window. Hit **New** and change the material name from **Material.001** to **clamp_sr**. Next, select **File>Export>Model Description Language (.mdl)**. Navigate to the directory where you want to create your file (e.g. **/home/user/mcell_tutorial/clamp_conc**). In the text field below the directory, type **clamp_conc.mdl** and hit **Export MDL**.

Now open **clamp_conc.mdl** and change **iterations** to **500**. Next, add in the following text after the **INCLUDE_FILE** commands::

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
    }

    DEFINE_SURFACE_CLASSES {
        clamp_sc {CLAMP_CONC vol1 = 1E-5}
    }  

    MODIFY_SURFACE_REGIONS {
        Plane[clamp_sr] {
            SURFACE_CLASS = clamp_sc
        }
    }

Finaly, add the following text to the end of the file::

    REACTION_DATA_OUTPUT {
        STEP=time_step
        {COUNT[vol1,World.Plane,ESTIMATE_CONC]}=> "./react_data/vol1.dat"
    }

Save and run the mdl by typing **mcell clamp_conc.mdl**. The only new commands here are **CLAMP_CONC** and **ESTIMATE_CONC**. **CLAMP_CONC** is applied like any other surface class, except that the molarity of a certain molecule is specified. **ESTIMATE_CONC** is used in a count statement after an object or region, and (unsurprisingly) estimates the concentration at that location. *Note:* The units for these two commands are different; **CLAMP_CONC** is M and **ESTIMATE_CONC** is uM.

In this example, we clamp the concentration of **vol1** at a molarity of **1E-5** M. When you plot the results, you'll notice that the concentration of molecules increases for a period of time and then reaches a steady state near 10 uM, which is what we would expect given what we asked for in the **CLAMP_CONC** command. 

Optimizing Your Simulation
=============================================

These simplistic simulations should not be overly taxing on a relatively recent desktop machine. However, you may likely want to develop simulations which have many more molecules possibly on large dense mesh objects. There are a couple of strategies you can use to speed up your simulation (and/or to save disk space). The following three topics will address some of these issues:

* `Adding Partitions`_
* `Target Only`_
* `Only Export What You Need`_

Adding Partitions
---------------------------------------------

A full explanation of partitions is outside of the scope of this tutorial, but, essentially, when MCell is checking to see if a reaction occurs, partitions lower the number of potential partners it must check. For practical puprposes, partitions can greatly speed up your simulation, but, if used improperly, they can actually slow it down. Begin by creating a directory called **partitions** inside the main tutorial directory. Inside the **partitions** directory, create a file called **partitions.mdl** with the following text::

    ITERATIONS = 1000
    TIME_STEP = 5e-6

    PARTITION_X = [ [-1.0 TO 1.0 STEP 0.20] ]
    PARTITION_Y = [ [-1.0 TO 1.0 STEP 0.20] ]
    PARTITION_Z = [ [-1.0 TO 1.0 STEP 0.20] ]

    INCLUDE_FILE = "./partitions_Cube.mdl"

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol2 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol3 {DIFFUSION_CONSTANT_3D = 1E-6}
    }

    DEFINE_REACTIONS {
        vol1 + vol2 -> vol1 + vol3 [1E7]
        vol1 + vol3 -> vol2 + vol3 [1E6]
    }

    INSTANTIATE World OBJECT {
        Cube BOX {CORNERS = [-1.0,-1.0,-1.0],[1.0,1.0,1.0]}
        vol1_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 2000
        }
        vol2_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = vol2
            NUMBER_TO_RELEASE = 2000
        }
    }

The new thing of interest in this MDL is the **PARTITION** commands. Each of these three commands creates planes along the axis specified. The intersection of these planes create subvolumes. The distance of these subvolumes should generally not be smaller in length than the mean diffusion distance of the faster molecules in your simulation.

Run this MDL, and take note of the **Total wall clock time** reported by MCell. Then remove (or comment out) the partitions and run it again. The actual speed improvement will depend on the machine running it, but for the machine this example was tested on, it resulted in a speed increase of almost six times.

Although unrelated to partitions, note that instead of creating a **Cube** object with Blender, we simply used MCell's built in command (**BOX**) for creating one.

Target Only
---------------------------------------------

If you have a reaction between two molecules in which there are many of one molecule and very few of another, you might want to consider using the **TARGET_ONLY** command. Normally, a diffusing molecule will check to see if there are any potential molecules to react with. However, a molecule that is marked as **TARGET_ONLY** can only be the target of a reaction, and will not search for partners to react with. Create a directory called **target_only**. In that new directory, copy the following text into a file called **target_only.mdl**::

    iterations = 500
    time_step = 5e-6
    ITERATIONS = iterations
    TIME_STEP = time_step

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol2 {DIFFUSION_CONSTANT_3D = 1E-6 TARGET_ONLY}
        vol3 {DIFFUSION_CONSTANT_3D = 1E-6}
    }

    DEFINE_REACTIONS {
        vol1 + vol2 -> vol1 + vol3 [1E8]
    }

    INSTANTIATE World OBJECT {
        Cube BOX {CORNERS = [-1.0,-1.0,-1.0],[1.0,1.0,1.0]}
        vol1_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 100
        }
        vol2_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = vol2
            NUMBER_TO_RELEASE = 10000
        }
    }

In this case, **vol2** is marked as being **TARGET_ONLY** in the **DEFINE_MOLECULES** section. From the **DEFINE_REACTIONS** section, we can see that **vol1** reacts with **vol2** to create **vol3** and reproduce **vol1**. Without the **TARGET_ONLY** command, every **vol2** molecule would have to check to see if there were **vol1** molecules to react with and vice versa. With this command, *only* **vol1** must search for reaction partners. Given that there are 100 **vol1** and 10000 **vol2**, this second method is much more efficient.

Only Export What You Need
---------------------------------------------

Visualization data can be great if you are making a figure to accompany a paper, or you are trying to troubleshoot a problem in your simulation, but there's probably no need to export everything at all times (**ALL_DATA @ ALL_ITERATIONS**). You could either comment out the **VIZ_OUTPUT** section entirely when you don't need it or only export what you need. This can speed up your simulation and save you disk space. The following **VIZ_OUPUT** sections illustrates how to selectively export visualization data::

    VIZ_OUTPUT {
        FILENAME = "selective"
        MOLECULES {
            NAME_LIST {vol1}
            ITERATION_NUMBERS {ALL_DATA @ [[100 TO 200 STEP 10]]}
        }   
    }   

The line **NAME_LIST {vol1}** indicates that we will only be exporting the molecule named **vol1**. The following line indicates that we will export it from iterations 100 to 200 at every 10 steps (i.e. 100, 110, ... 190, 200). The **MESHES** section was also omitted entirely. 

These are just examples of what you can do, and the actual list of molecules, meshes, and iterations that you export will depend entirely on your own needs for your specific simulation.

Analyzing Your Data
=============================================

There are many tools available for plotting and analyzing data. We will make use of python along with numpy and matplotlib. Using these tools, we will generate a histogram of molecule locations relative to the origin, and also find such things as the mean, min, and max. First, however, we need the mdl. In the main tutorial directory, create a new directory called **hist**. Inside that directory, create an mdl called **hist.mdl**, and insert the following text into it::

    TIME_STEP = 1.0e-6
    ITERATIONS = 1000
                     
    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1e-7}
    }

    INSTANTIATE world OBJECT { 
        vol1_rel SPHERICAL_RELEASE_SITE {
            LOCATION = [0,0,0] 
            MOLECULE = vol1 
            NUMBER_TO_RELEASE = 5000
            SITE_DIAMETER = 0.0 
        }   
    }

    VIZ_OUTPUT {
        VIZ_MOLECULE_FORMAT = ASCII
        FILENAME = "hist" 
        MOLECULES { 
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}  
        }   
    } 

This is very similar to MDLs you have run in the past with the exception of the line **VIZ_MOLECULE_FORMAT = ASCII**. Normally, "viz_data" molecule locations are stored in a binary file to make them smaller, but this command will cause them to be created in a human-readable, ASCII format.

Run this mdl by typing **mcell hist.mdl**. It will create a visualization directory called **hist_viz_data**.

Create a file called **hist.py** and copy the following text into it::

    #!/usr/bin/env python

    import numpy as np
    import matplotlib.pyplot as plt 

    mol_pos_file = "./hist_viz_data/frame_data/iteration_1000/vol1.positions.dat"
    data = np.genfromtxt(mol_pos_file)   # open molecule positions as 2d array
    data = data[:, 0]                    # create array from 1st column (X pos)
    print('The min is: %.3f' % np.min(data))
    print('The max is: %.3f' % np.max(data))
    print('The mean is: %.3f' % np.mean(data))
    print('The standard deviation is: %.3f' % np.std(data))
    plt.hist(data, 100)                  # create a histogram with 100 bins
    plt.xlabel('Distance (Microns)')     # add an x-axis label
    plt.ylabel('Molecules')              # add an y-axis label
    plt.show()                           # plot the data

Although the comments explain what is happening, let's break it down as simply as possible. The file **vol1.positions.dat** contains the positions of each vol1 molecule at an iteration specified by the directory (e.g. **iteration_1000**). Every line of the file contains three numbers each separated by a space. These numbers represent the x, y, and z locations. Here are what the first few lines of **vol.positions.dat** in the **iteration_1000** directory look like::

    -0.258572 0.15827 -0.0314231 
    0.0452288 -0.0677351 0.037688 
    -0.0572103 0.0192047 -0.0370933 
    0.0644877 0.230798 -0.0415339 

We are loading **vol1.positions.dat** into a two dimensional array called **data**. We then "slice" the first column which contains all the X locations. We then print the min, max, mean, and standard deviation to the command line. Lastly, we create the histogram with labels and plot (or show) it.

Run the file now by typing **python hist.py**.

Running Multiple Seed Values
=============================================

In MCell, diffusion (amongst other things) happen stochastically. However, the results are replicable as long as one provides the same seed value. Given this stochastic nature, you can expect the data generated from a simulation to look noisy, especially if the number of reacting molecules is small. We can overcome this problem by running many different simulations, each with a different seed value, and then averaging the results of all the simulations.

We'll begin by creating a directory called **seed**. Inside it, create an MDL called **seed.mdl** with this text::

    iterations = 1000 
    time_step = 5e-6 
    ITERATIONS = iterations
    TIME_STEP = time_step

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol2 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol3 {DIFFUSION_CONSTANT_3D = 1E-6}
    }   

    DEFINE_REACTIONS {
        vol1 + vol2 -> vol1 + vol3 [1E7]
        vol1 + vol3 -> vol2 + vol3 [1E6]
    }   

    INSTANTIATE World OBJECT {
        Cube BOX {CORNERS = [-0.1,-0.1,-0.1],[0.1,0.1,0.1]}
        vol1_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 100 
        }   
        vol2_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = vol2
            NUMBER_TO_RELEASE = 100 
        }   
    }   

    sprintf(seed,"%04g",SEED)

    REACTION_DATA_OUTPUT {
        STEP=time_step
        {COUNT[vol1,WORLD]}=> "./react_data/vol1." & seed & ".dat"
        {COUNT[vol2,WORLD]}=> "./react_data/vol2." & seed & ".dat"
        {COUNT[vol3,WORLD]}=> "./react_data/vol3." & seed & ".dat"
    }

All the syntax should be familiar except for the line **sprintf(seed,"%04g",SEED)**. This assigns the value of the **SEED** to the variable **seed**. The **%04g** formats it so that there are four leading zeros.

Next, create the following python script called **seed.py**::

    #!/usr/bin/env python

    import os

    for i in range(1, 21):
        os.system("mcell -seed %i ./seed.mdl" % i)

This file is similar to the **scaling.py** file that we created in the checkpointing section. This will run MCell twenty different times, each time incrementing the seed value by one. Save and run this file. You should now have sixty files in the **react_data** directory (20 for each molecule). Now we will begin the process of averaging these results. Create a python script called **avg_seeds.py** with the following text in it::

    #!/usr/bin/env python

    import numpy as np
    import matplotlib.pyplot as plt 
    import os

    mol_counts = None
    files = os.listdir('react_data')   #build a list of reaction data file names
    files.sort()                       #sort that list alphabetically

    for f in files:                    #iterate over the list of file names
        if f.startswith('vol1'):
            rxn_data = np.genfromtxt("./react_data/%s" % f, dtype=int)
            rxn_data = rxn_data[:, 1]  #take the second column
            plt.plot(rxn_data, '0.5')  #plot the results as a gray line
            if mol_counts is None:
                mol_counts = rxn_data
            else:
                #built up 2d array of molecule counts (one col/seed)
                mol_counts = np.column_stack((mol_counts, rxn_data))
        else:
            pass

    mol_counts = mol_counts.mean(axis=1)  #take the mean of the rows
    plt.plot(mol_counts, 'r')             #plot the results as a red line
    plt.show()                            #show the plot

This script will load (and plot) each of the twenty **vol1.####.dat** files into a two dimensional array, take the mean of the rows, and plot the results.

.. #target-notes::
.. #index:: Blender 
