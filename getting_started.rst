.. _getting_started:

*********************************************
Getting Started
*********************************************

For this first example, we'll export the default mesh from Blender into the MDL format which MCell can parse. We will then run this MDL with MCell to generate visualization data.

.. _gen_mesh:

Generate Mesh and Export MDL with Blender
=============================================

The majority of this tutorial can be easily accomplished by following along with the text. However, sections that rely heavily on a GUI (like this one), might be better understood by watching a video tutorial.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/getting_started.ogg" type='video/ogg'/>
    </video>

You can skip to the next section (:ref:`run_sim`) if you have watched the previous video tutorial. Otherwise, follow along with the rest of the directions in this section. 

Open up a terminal and enter the command::

    blender

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/cube.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/object_button.png

You should see a cube in the **3D View Editor**. Hit the **Object** button in the **Properties Editor**. Scroll to the bottom of the Editor.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/new_region.png


Define a Surface Region
---------------------------------------------

Expand the **Define Surface Regions** panel. Hit the **+** button and **New Region** should appear in the list of regions. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/top.png

Change the text field which reads **New Region** to **top**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/triangulate.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/ctrl_tab.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/select_top.png

Move the cursor to the **3D View Editor**. Hit **Tab** to change into **Edit Mode**. Hit **Ctrl-T** to triangulate the faces. Then, hit **Ctrl-Tab** and select **Face**. Then while **holding Shift**, **right click** on the two top faces to select them.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/assign.png

Under the **Define Surface Regions** panel, click **Assign**. Hit **Tab** to change back into **Object Mode**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/scene_button.png

Hit the **Scene** button in the **Properties Editor**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/model_objects.png

Expand the **Model Objects** panel. With the **Cube** object still selected, hit the **+** button.

Set Simulation Parameters
---------------------------------------------

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/model_init.png

Expand the **Model Initialization** panel. Change **Simulation Iterations** to **1000**. Change **Simulation Time Step** to **5e-6**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/new_molecules.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/define_molecules.png

Expand the **Define Molecules** panel and hit the **+** button three times. This will create three instances of **New Molecule** in the list of molecules. Left click on the first instance of **New Molecule**. Change the **Molecule Name** to **vol1**, the **Molecule Type** to **Volume Molecule**, and the **Diffusion Constant** to **1e-6**. Repeat this process for the next molecule in the list, but call this one **vol2**. Finally, change the third entry **Molecule Name** of the first one to **surf1**, and the **Diffusion Constant** to **1e-7**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/define_reactions.png

Expand the **Define Reaction** panel and hit the **+** button. Change **Reactants** to **vol1' + surf1,**. Change **Products** to **surf1, + vol2,**. Change **Forward Rate** to **1e8**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/molecule_release.png

Expand the **Molecule Release/Placement** panel and hit the **+** button twice, which will create two instances of **New Release Site**. Select the first instance, and change **Site Name** to **vol1_rel**. Change **Molecule** to **vol1**. Change **Release Shape** to **Object/Region**. Change **Object/Region** to **Cube**. Change **Quantity to Release** to **2000**.

Now select the second release site. Change **Site Name** to **surf1_rel**. Change **Molecule** to **surf1'**. Change **Release Shape** to **Object/Region**. Change **Object/Region** to **Cube[top]**. Change **Quantity to Release** to **2000**.

Export MDLs
---------------------------------------------

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/export.png

Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to the directory where we will export the files (**/home/user/mcell_tutorial/intro** where **user** is your user name) and hit **OK** when it prompts you to make a new directory. Then select **Set Project Directory**. Set the **Project Base** to **intro**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

Either leave Blender open or save and quit, as we'll need to modify this model later.

.. _run_sim:

