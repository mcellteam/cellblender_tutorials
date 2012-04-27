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

If you watched the previous video tutorial, you can skip ahead to `Surface Classes and Volume Molecules`_.

In order to complete the next section (`Surface Classes and Volume Molecules`_), we first have to make a few simple changes to our Blender model. We'll pick up right where we left off in :ref:`gen_mesh`. Hit **z** to switch to a wireframe view. Hit **Shift-a** and select **Plane**. Hit **g** to "grab" the plane, **z** to constrain the movement to the z-axis, **1.5** to move it 1.5 units, and **Enter** to confirm.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/new_mat_plane.png

Hit the **New** button in the **Materials** section of the **Properties** window. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/blender/mat_above.png

Change the newly created material text field from **Material** to **above**. Click **Assign**. 

Next, select **File>Export>Model Description Language (.mdl)**. Deselect **Instantiate & Viz** so that we only export the new meshes and don't override the changes in **intro.mdl**. Navigate to the directory where you want to create your file (e.g. **/home/user/mcell_tutorial/surf_class**). In the text field below the directory, type::

    intro.mdl

and hit **Export MDL**.

.. _surf_class_vm_mod_mdl:

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

Save the file and run it with MCell by entering the command::

    mcell intro.mdl

Visualize the results with CellBlender just like was done in the :ref:`visualize_molecules` section. See if you can notice the **vol2** molecules being destroyed by the absorptive surface.

.. _surf_class_rxns:

Surface Classes and Reactions
=============================================
In the `Surface Classes and Volume Molecules`_ section, we learned that surface classes can be used to give parts of meshes special properties. Surface classes can also be used to provide extra specificity over how reactions occur. Begin by creating a copy of the **surf_class** directory, by typing the following command at the terminal: **cp -fr /home/user/mcell_tutorial/surf_class /home/user/mcell_tutorial/surf_class_rxns** (don't forget to replace **user** with your actual user name).

.. _surf_class_rxns_mod_mesh:

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

Next, select **File>Export>Model Description Language (.mdl)**. *Deselect* **Instantiate & Viz** to indicate that we *only* want to export the mesh object. Navigate to the directory where you want to create your file (e.g. **/home/user/mcell_tutorial/surf_class_rxns**). In the text field below the directory, type::

    intro.mdl

and hit **Export MDL**.

.. _surf_class_rxns_mod_mdl:

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

Save the file and run it with MCell by enterting the command::

    mcell intro.mdl

When you visualize the results with CellBlender, want to add in custom rendering properties for **surf2**. You should notice that there are **vol2** molecules being created inside the box, but only in the upper portion of it, despite the fact that the **surf2** molecules are facing both up *and* down. The reason for this is because the reaction is only taking place at the **BACK** of the **empty** surface class with the **BOTTOM** of **surf2**.

