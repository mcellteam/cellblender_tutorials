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
      preload="metadata" width="960" height="540" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/sc_sm.ogg" type='video/ogg'/>
    </video>

Start Blender. Hit the **Object** button in the **Properties Editor**. Scroll to the bottom of the Editor. Hit **+** twice so that you have two new surface regions. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/sc_sm/top_bottom_regions.png

Click on the first one and change its name in the text field to **top**. Next, click on the second entry and change its name to **bottom**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/triangulate.png

Move your cursor to the **3D View** window and hit **Tab** to switch into **Edit Mode**.  Hit **Ctrl-T** to triangulate the faces.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/ctrl_tab.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/select_top.png

Then hit **Ctrl-Tab** and select **Face**. Right click on the top faces, select the **top** surface region, and click **Assign**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/sc_sm/select_bottom.png

Next move your mouse back to the **3D View** window and hold the middle mouse button down and drag upward so that the bottom face is shown. Right click on the bottom faces, select **bottom** from the list of materials, and click **Assign**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/sc_sm/model_objects_init.png

Expand the **Model Objects** panel. Hit the **+** button and **Cube** will appear in the list. Next, expand the **Model Initialization** panel. Change **Simulation Iterations** to **1000**. Change **Simulation Time Step** to **1e-5**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/sc_sm/define_surf_molec.png

Expand the **Define Molecules** panel and hit the **+** button. Change the **Molecule Name** to **surf1**, the **Molecule Type** to **Surface Molecule**, and the **Diffusion Constant** to **1e-7**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/sc_sm/molec_release.png

Expand the **Molecule Release/Placement** panel and hit the **+** button. Change **Site Name** to **surf1_rel**. Change **Molecule** to **surf1'**. Change **Release Shape** to **Object/Region**. Change **Object/Region** to **Cube**. Change **Quantity to Release** to **1000**.

Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to the directory where we will export the files (``/home/user/mcell_tutorial/sc_sm`` where **user** is your user name) and hit **OK** when it prompts you to make a new directory. Then select **Set Project Directory**. Set the **Project Base** to **sc_sm**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

.. _surf_class_sm_mdl:

Modifying the MDL
---------------------------------------------

Create a file called **sc_sm.surface_classes.mdl**::

    DEFINE_SURFACE_CLASSES 
    {
        absorb {ABSORPTIVE = surf1}
        reflect {REFLECTIVE = surf1}
    }  

Create a file called **sc_sm.mod_surf_regions.mdl**::

    MODIFY_SURFACE_REGIONS 
    {
        Cube[top]
        {
            SURFACE_CLASS = absorb
        }   
        Cube[bottom]
        {
            SURFACE_CLASS = reflect
        }   
    }

In this example, we have two surface classes, **absorb** and **reflect**. **absorb** is applied to **top** and **reflect** is applied to **bottom**. The faces in the middle do not have a surface region assigned to them. **surf1** molecules are released all over the **Cube**, not just one surface region. The effect of the **absorb** class is that all the **surf1** molecules are destroyed when they hit the boundary between the **top** region and the undefined middle section. The effect of the **reflect** class is that molecules cannot pass the boundary between the **bottom** region and the undefined middle section. Therefore, all the **surf1** molecules that start inside of the **bottom** region never escape and the **surf1** molecules starting in the middle section and **top** region will ultimately be destroyed. You should run the **sc_sm.main.mdl** with MCell and visualize the results with CellBlender to confirm this.

