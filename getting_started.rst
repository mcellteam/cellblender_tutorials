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

You can skip to the next section (`Run the Simulation`_) if you have watched the previous video tutorial. Otherwise, follow along with the rest of the directions in this section. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/cube.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/material_button.png

Open up a terminal and enter the command::

    blender

You should see a cube in the **3D View Window**. Hit the **Material** button in the **Properties Window**. 

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

Next, select **File>Export>Model Description Language (.mdl)**. Navigate to the directory where we will export the files (**/home/user/mcell_tutorial/intro** where **user** is your user name) and select **OK** when it prompts you to make a new directory. In the text field below the directory, type::

    intro.mdl

and hit **Export MDL**. Either leave Blender open or save and quit, as we'll need to modify this model later.

.. _run_sim:

Run the Simulation
=============================================

.. _tut_viz_data1.tgz: http://mcell.psc.edu/tutorials/mdl/main/tut_viz_data1.tgz

Let's verify that this simple case works with MCell before adding in more details.

At the command line, navigate to the appropriate directory (``cd /home/user/mcell_tutorial/intro`` where **user** is your user name), and enter the command:: 

    mcell intro.mdl

MCell should output some information to the command line indicating that it ran successfully. Enter the command:: 
    
    ls

and you should see that a directory called **intro_viz_data** has been created.

.. _visualize_mesh:

Visualize the Mesh
=============================================

As with the Blender section, this section requires extensive use of a GUI, so you may find it easier to follow along with this video tutorial.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/dreamm_pt1.ogg" type='video/ogg'/>
    </video>

You can skip to the next section (:ref:`annotate`) if you have watched the previous video tutorial. Otherwise, follow along with the rest of the directions in this section. 

To start DReAMM, open a terminal, enter the command::
    
    dreamm

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


