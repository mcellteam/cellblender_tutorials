.. _surface_classes:

*********************************************
Introduction to Surface Classes
*********************************************

.. _surf_class_vol_mol:

Surface Classes and Volume Molecules
=============================================

Surface classes allow various properties (e.g. **ABSORPTIVE**, **TRANSPARENT**) to be applied to surfaces, which can affect specified molecules. 

Begin by creating a copy of the **intro** directory, by typing the following command at the terminal::

    cp -fr /home/user/mcell_tutorial/intro /home/user/mcell_tutorial/surf_class

Don't forget to replace **user** with your actual user name.

.. _surf_class_vm_mod_mesh:

Modify the Mesh
---------------------------------------------

Watch the following video tutorial or follow along with the instructions below.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/export_above.ogg" type='video/ogg'/>
    </video>

If you watched the previous video tutorial, you can skip ahead to :ref:`surf_class_vm_mod_mdl`.

In order to complete the next section (:ref:`surf_class_vm_mod_mdl`), we first have to make a few simple changes to our Blender model. We'll pick up right where we left off in :ref:`gen_mesh`. Hit **z** to switch to a wireframe view. Hit **Shift-a** and select **Plane**. Hit **g** to "grab" the plane, **z** to constrain the movement to the z-axis, **1.5** to move it 1.5 units, and **Enter** to confirm.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/new_mat_plane.png

Hit the **Object** button on the **Properties** Editor. Under the **Surface Regions** panel, hit **+**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/mat_above.png

Change the default name to **above**. Change into **Edit Mode** by hitting **Tab** in the **3D View Window**. With the faces selected, click **Assign**.

Under **Define Surface Classes**, select **Include Surface Classes** and **Include Modify Surface Regions**.

Hit the **Scene** button in the **Properties** Editor. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to the directory where we will export the files (**/home/user/mcell_tutorial/sc** where **user** is your user name) and hit **OK** when it prompts you to make a new directory. Then select **Set Project Directory**. Set the **Project Base** to **sc**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

.. _surf_class_vm_mod_mdl:

Modify the MDL
---------------------------------------------

Create a file called **sc.surface_classes.mdl** and enter the following text into it ::

    DEFINE_SURFACE_CLASSES 
    {
        absorb_vol2 {ABSORPTIVE = vol2}
    }

The command above creates a surface class called **absorb_vol2**. Since **vol2** is the value set to the **ABSORPTIVE** command, this means that any **vol2** molecules that touch a surface that has the **absorb_vol2** surface class will be destroyed.

Now we actually have to apply the surface class to a surface region. Create a file called **sc.mod_surf_regions.mdl**::

    MODIFY_SURFACE_REGIONS {
        Plane[above] {
            SURFACE_CLASS = absorb_vol2
        }   
    }

That's all there is to it. The other two surface class commands are **REFLECTIVE** (the default state for surfaces) and **TRANSPARENT** (allows molecules to freely pass through). Feel free to try these out on your own.

Save the file and run it with MCell by entering the command::

    mcell intro.mdl

Visualize the results with CellBlender just like was done in the :ref:`visualize_molecules` section. See if you can notice the **vol2** molecules being destroyed by the absorptive surface.

.. _surf_class_rxns:

Surface Classes and Reactions
=============================================
In the :ref:`surf_class_vol_mol` section, we learned that surface classes can be used to give parts of meshes special properties. Surface classes can also be used to provide extra specificity over how reactions occur.

.. _surf_class_rxns_mesh:

More Mesh Modifications
---------------------------------------------

Watch the following video tutorial or follow along with the instructions below.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/export_inside.ogg" type='video/ogg'/>
    </video>

If you watched the previous video tutorial, you can skip ahead to :ref:`surf_class_rxns_mdl`.

We need to make a few more changes to our Blender model to complete the next section (:ref:`surf_class_rxn_mod_mdl`). We're picking up where we left off in :ref:`surf_class_vm_mod_mesh`. In fact, the instructions will be very similar, aside from a few minor changes. While still in **Object Mode**, hit **Shift-a**, select **Plane**, and **Enter** to confirm.  

Hit the **Object** button on the **Properties** Editor. Under the **Surface Regions** panel, hit **+**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/new_mat_plane2.png

Change the newly created surface region text field from **New Region** to **inside**. Change into **Edit Mode** by hitting **Tab**. Click **Assign**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/mat_inside.png

Expand the **Define Molecules** panel and hit the **+** button. Left click **New Molecule**. Change the **Molecule Name** to **surf2**, the **Molecule Type** to **Surface Molecule**, and the **Diffusion Constant** to **0**.

Expand the **Define Reaction** panel and hit the **+** button. Change **Reactants** to **vol1, + surf2' @ empty'**. Change **Products** to **surf2' + vol2'**. Change **Forward Rate** to **1e8**.

Hit the **Scene** button in the **Properties** Editor. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to the directory where we will export the files (**/home/user/mcell_tutorial/sc_rxn** where **user** is your user name) and hit **OK** when it prompts you to make a new directory. Then select **Set Project Directory**. Set the **Project Base** to **sc_rxn**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

.. _surf_class_rxns_mdl:

More MDL Modifications
---------------------------------------------

Open **sc_rxns.surface_classes.mdl** in the new **sc_rxns** directory. Change the **DEFINE_SURFACE_CLASSES** section as follows::

    DEFINE_SURFACE_CLASSES {
        absorb_vol1 {ABSORPTIVE = vol1}
        empty {}
    }  

This new surface class, **empty**, is the simplest case you can have for a surface class. By itself, it's not very useful, but we can use it in reactions. Let's look at the **sc_rxns.reactions.mdl** file::

    DEFINE_REACTIONS {
        vol1, + surf1' -> surf1' + vol2' [1E8]
        vol1, + surf2' @ empty' -> surf2' + vol2' [1E8]
    }   

The above change means that **vol1** will only react with the **BOTTOM** of **surf** at the **BACK** of the **empty** surface class. This means the reaction won't occur when the surface molecules diffuse away from surface regions that have this surface class applied (i.e. when it diffuses from **top** to **sides_and_bottom**). Lastly, change the **sc_rxns.mod_surf_regions.mdl** like this::

    MODIFY_SURFACE_REGIONS {
        Plane[above] {
            SURFACE_CLASS = absorb_vol1
        }
        Plane.001[inside] {
            SURFACE_CLASS = empty
        }
    }

Save the file and run it with MCell by enterting the command::

    mcell intro.mdl

When you visualize the results with CellBlender, want to add in custom rendering properties for **surf2**. You should notice that there are **vol2** molecules being created inside the box, but only in the upper portion of it, despite the fact that the **surf2** molecules are facing both up *and* down. The reason for this is because the reaction is only taking place at the **BACK** of the **empty** surface class with the **BOTTOM** of **surf2**.
