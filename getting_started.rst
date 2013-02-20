.. _getting_started:

*********************************************
Getting Started
*********************************************

For this first example, we'll use Blender and the CellBlender plugin to set
some simulation parameters. We'll export this into the MDL file format which MCell
can parse. Then we will run these MDL files with MCell to generate visualization
data, which will be used in the next section.

Note that most blender actions can be accomplished with either key commands or
mouse menu/button clicks. But for speed, it is strongly advised that you learn
the key commands.

.. _gen_mesh:

Starting Blender
---------------------------------------------

The majority of this tutorial can be easily accomplished by following the
Tutorial Instructions below. However, sections that rely heavily on a GUI
(like this one), might be better understood by watching a video tutorial
either before following the instructions or instead of them.

Tutorial Video
---------------------------------------------

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="960" height="540" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/getting_started.ogg" type='video/ogg'/>
    </video>

If you've followed along with this video, you can skip to the :ref:`annotate` section.
If not, or if you'd like to go through it again, the following instructions should give
you the same result.

Tutorial Instructions
---------------------------------------------

Open up a terminal and enter the command::

    blender

You should see a cube in the **3D View Editor**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/cube.png

.. _define_region:

Define a Surface Region
---------------------------------------------

Hit the **Object** button in the **Properties Editor** (little cube in the right side panel).

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/object_button.png

Scroll to the bottom of the Properties Editor panel. Expand the **Define Surface Regions** 
panel by clicking the small triangle next to the name (*note that you may have to scroll
further after actions which expand the sizes of panels because new fields may appear beyond
the currently visible portion of the panel*). Hit the **+** button and new region named "**Region**"
should appear in the list of regions, indicating that a new surface region was created
(*again, you may need to scroll the panel to see all of the new fields created by the* **+** *button*).

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/new_region.png

Rename this new surface region to "**top**" by changing the **Region Name** field from "**Region**"
to "**top**".

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/top.png

.. _assign_region:

Assign a Surface Region
---------------------------------------------

Move the cursor to the **3D View Editor**. Hit **Tab** to change into **Edit
Mode** (or enter **Edit Mode** via the "Mode" selection control). Hit **Ctrl-t** to triangulate 
the faces (or use **Mesh/Faces/TriangulateFaces**). 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/triangulate.png

Hit **Ctrl-Tab** and select **Face** (or click on the "**Face select**" button) to enter face
selection mode.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/ctrl_tab.png

Then hit **a** (or use menu option **Select/(De)select All**) to deselect everything. Select
just the top two triangular faces by **holding Shift** while **right clicking** on each
of the two top faces to select them.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/select_top.png

Under the **Define Surface Regions** panel, click the **Assign** button (*remember that
you might need to scroll down to see the new buttons added*). After clicking the **Assign**
button, those top two faces will now have the "**top**" surface region assigned to them.
They won't look any different, but they're now "tagged" with the name "top" which MCell
can use to reference them.

With the cursor over the **3D View Editor**, hit **Tab** to change back into **Object Mode**
(or enter Object Mode via the "Mode" selection control).

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/assign.png

.. _set_parameters:

Set Simulation Parameters
---------------------------------------------

Hit the **Scene** button in the **Properties Editor**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/scene_button.png

There may be many Scene panels which are open (triangles pointing downward). In order to
find things easily, take the time to close all of these panels by clicking the triangles
to collapse them down to one line each. Then find and expand just the **Model Objects** panel.
With the **Cube** object still selected, hit the **+** button. This will add **Cube** to the
list of mesh objects to be exported and initialized.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/model_objects.png

Now find and expand the **Model Initialization** panel. Change **Simulation Iterations** to
**1000**. Change **Simulation Time Step** to **5e-6**. The units are in seconds.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/model_init.png

Define Molecules
---------------------------------------------

We will now define three new molecule species. Expand the **Define Molecules**
panel and hit the **+** button three times. This will create three instances of
**Molecule** in the list of molecules (don't worry about the "Duplicate molecule..."
warning because we'll be renaming each of these molecules next).

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/new_molecules.png

Left click on the first instance of **New Molecule**. Change the **Molecule
Name** to **vol1**, the **Molecule Type** to **Volume Molecule**, and the
**Diffusion Constant** to **1e-6**. Repeat this process for the next molecule
in the list, but call this one **vol2**. Now, change the third entry to
**surf1**. The **Molecule Type** should be set to **Surface Molecule** and
change the **Diffusion Constant** to **1e-7**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/define_molecules.png

Define Reactions
---------------------------------------------

In order to have our molecules interact with one another, we first need to
define some reactions. Expand the **Define Reaction** panel and hit the **+**
button. Change **Reactants** to **vol1' + surf1,**. Change **Products** to
**surf1, + vol2,**. Be sure to use the commas and apostrophes shown in these
examples. The meaning of these symbols will be explained in the :ref:`rxn_dir`
section. Lastly, change **Forward Rate** to **1e8**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/define_reactions.png

Create Release Sites
---------------------------------------------

We have defined molecules and reactions, but we still need to release some
molecules into our simulation.

Expand the **Molecule Release/Placement** panel and hit the **+** button twice,
which will create two instances of **New Release Site**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/vol1_rel.png

Select the first instance, and change **Site Name** to **vol1_rel**. Change
**Molecule** to **vol1**. Change **Release Shape** to **Object/Region**. Change
**Object/Region** to **Cube**. Change **Quantity to Release** to **2000**. This
will release 2000 **vol1** molecules randomly throughout the interior of the
**Cube** object.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/surf1_rel.png

Now select the second release site. Change **Site Name** to **surf1_rel**.
Change **Molecule** to **surf1'**. Change **Release Shape** to
**Object/Region**. Change **Object/Region** to **Cube[top]**. Change **Quantity
to Release** to **2000**. This will release **2000** molecules randonmly on the
**top** surface region.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/rxn_viz_output.png

Under **Reaction Output Settings**, enable **Include Reaction Output**. Then,
under **Visualization Output Settings**, enable **Include Viz Output**.

.. _export_mdls:

Export MDLs
---------------------------------------------

Under **CellBlender Project Settings**, select **Export CellBlender Project**.
Navigate to the directory where we will export the files
(**/home/user/mcell_tutorial/intro** where **user** is your user name) and hit
**OK** when it prompts you to make a new directory. Then select **Set Project
Directory**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/set_project_dir_pt1.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/set_project_dir_pt2.png

Set the **Project Base** to **intro**. Then hit **Export CellBlender Project**,
navigate to same directory as before, and hit **Export MCell MDL**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/project_base_prefix.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/export_mcell_mdl.png

Either leave Blender open or save and quit, as we'll need to modify this model
later.

At the command line, type::

    ls

You should notice that we have created four new files: **intro.main.mdl**,
**intro.geometry.mdl**, **intro.molecules.mdl**, and **intro.reactions.mdl**.
We will take a look at all of these in turn.
