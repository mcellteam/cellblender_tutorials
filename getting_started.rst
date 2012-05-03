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
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/blender_pt1.ogg" type='video/ogg'/>
    </video>

You can skip to the next section (:ref:`run_sim`) if you have watched the previous video tutorial. Otherwise, follow along with the rest of the directions in this section. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/cube.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/material_button.png

Open up a terminal and enter the command::

    blender

You should see a cube in the **3D View Editor**. Hit the **Object** button in the **Properties Editor**. Scroll to the bottom of the Editor.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/plus_button.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/new_button.png

Expand the **Define Surface Regions** panel. Hit the **+** button and **New Region** should appear in the list of regions. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/top.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/sides_and_bottom.png

Change the text field which reads **New Region** to **top**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/face_select.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/right_click.png

Move the cursor to the **3D View Editor**. Hit **Tab** to change into **Edit Mode**. Hit **Ctrl-Tab** and select **Face**. Then **right click** on the top face to select it.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/assign.png

Select the **top** surface region from the list of surface regions. Click **Assign**. Hit **Tab** to change back into **Object Mode**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/export_mdl.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/export_mdl_dir.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/export_mdl_button.png

Hit the **Scene** button in the **Properties Editor**. 

Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to the directory where we will export the files (**/home/user/mcell_tutorial/intro** where **user** is your user name) and hit **OK** when it prompts you to make a new directory. Then select **Set Project Directory**. Set the **Project Base** to **intro**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

Expand the **Model Objects** panel. With the **Cube** object still selected, hit the **+** button.

Expand the **Define Molecules** panel and hit the **+** button three times. This will create three instance of **New Molecule** in the list of molecules. Left click on the first instance of **New Molecule**. Change the **Molecule Name** to **vol1**, the **Molecule Type** to **Volume Molecule**, and the **Diffusion Constant** to **1e-6**. Repeat this process for the next molecule in the list, but call this one **vol2**. Finally, change the third entry **Molecule Name** of the first one to **vol1**, and the **Diffusion Constant** to **1e-6**. the **Molecule Type** to  the second to **vol2**, and the third to **surf1**

Either leave Blender open or save and quit, as we'll need to modify this model later.

.. _run_sim:

Run the Simulation
=============================================

.. _tut_viz_data1.tgz: http://mcell.psc.edu/tutorials/mdl/main/tut_viz_data1.tgz

Let's verify that this simple case works with MCell before adding in more details.

At the command line, navigate to the appropriate directory (``cd /home/user/mcell_tutorial/intro`` where **user** is your user name), and enter the command:: 

    mcell intro.mdl

MCell should output some information to the command line indicating that it ran successfully.
