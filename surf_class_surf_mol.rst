.. _surf_class_surf_mol:

*********************************************
Surface Classes and Surface Molecules
*********************************************

We have already discussed surface classes at length, but we haven't touched on how they can affect the diffusion of surface molecules. Their effects are manifested at the boundaries of the surface regions that they are applied to. For example, if a surface is **REFLECTIVE** to **surf1**, then any **surf1** can't get in or out of that that surface region. It acts as a fence of sorts corralling the molecules in one region. The **ABSORPTIVE** surface class also acts somewhat like a fence, but, instead of molecules harmlessly "bouncing" off of it, they are destroyed whenever they touch it. **TRANSPARENT** surface classes don't affect surface molecules, so we can ignore them in this context.

Since our current MDL is beginning to get a little complicated, we will start fresh with this next example. First, we need to create the mesh and export the MDL. Then, we will modify the MDL.

.. contents:: :local:

.. _surf_class_sm_mesh:

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

.. _surf_class_sm_mdl:

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

