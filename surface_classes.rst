.. _surface_classes:

*********************************************
Introduction to Surface Classes
*********************************************

.. _surf_class_vol_mol:

Surface Classes and Volume Molecules
=============================================

Surface classes allow various properties (e.g. **ABSORPTIVE**, **TRANSPARENT**)
to be applied to surfaces, which can affect specified molecules. 

.. _surf_class_vm_mod_mesh:

Modify the Mesh
---------------------------------------------

Watch the following video tutorial or follow along with the instructions below.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="960" height="540" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/surf_reg_above.ogg" type='video/ogg'/>
    </video>

If you watched the previous video tutorial, you can skip ahead to :ref:`surf_class_vm_mod_mdl`.

In order to complete the next section (:ref:`surf_class_vm_mod_mdl`), we first
have to make a few simple changes to our Blender model. We'll pick up where we
left off at the end of the :ref:`getting_started` section. Hit **Shift-a** and
select **Plane**. Hit **g** to "grab" the plane, **z** to constrain the
movement to the z-axis, **1.5** to move it 1.5 units, and **Enter** to confirm.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/above.png

Hit the **Object** button on the **Properties** Editor. Under the **Surface
Regions** panel, hit **+**. Change the default name to **above**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/above_quad.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/above_triangulated.png

Change into **Edit Mode** by hitting **Tab** in the **3D View Window**. With
the face of the plane selected, hit **Ctrl-t** to triangulate it. Then, click
**Assign** under **Define Surface Regions**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/include_surface_classes.png

Hit the **Scene** button on the **Properties** Editor. Under the **Model
Objects** panel, hit **+**. Under **Define Surface Classes**, select **Include
Surface Classes** and **Include Modify Surface Regions**.

Under **CellBlender Project Settings**, select **Export CellBlender Project**.
Navigate to the directory where we will export the files
(**/home/user/mcell_tutorial/sc** where **user** is your user name) and hit
**OK** when it prompts you to make a new directory. Then select **Set Project
Directory**. Set the **Project Base** to **sc**. Then hit **Export CellBlender
Project**, navigate to same directory as before, and hit **Export MCell MDL**.

.. _surf_class_vm_mod_mdl:

Modify the MDL
---------------------------------------------

Create a file called **sc.rxn_output.mdl** and copy this into it::

    REACTION_DATA_OUTPUT
    {
        STEP=1e-6
        {COUNT[vol1,WORLD]}=> "./react_data/vol1.dat"
        {COUNT[vol2,WORLD]}=> "./react_data/vol2.dat"
    }


Create a file called **sc.viz_output.mdl** and copy this into it::

    VIZ_OUTPUT
    {
        MODE = ASCII
        FILENAME = "./viz_data/viz_output"
        MOLECULES 
        {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }   
    }

Create a file called **sc.surface_classes.mdl** and enter the following text
into it ::

    DEFINE_SURFACE_CLASSES 
    {
        absorb_vol2 {ABSORPTIVE = vol2}
    }

The command above creates a surface class called **absorb_vol2**. Since
**vol2** is the value set to the **ABSORPTIVE** command, this means that any
**vol2** molecules that touch a surface that has the **absorb_vol2** surface
class will be destroyed.

Now we actually have to apply the surface class to a surface region. Create a
file called **sc.mod_surf_regions.mdl**::

    MODIFY_SURFACE_REGIONS
    {
        Plane[above]
        {
            SURFACE_CLASS = absorb_vol2
        }   
    }

That's all there is to it. The other two surface class commands are
**REFLECTIVE** (the default state for surfaces) and **TRANSPARENT** (allows
molecules to freely pass through). Feel free to try these out on your own.

Save the file and run it with MCell by entering the command::

    mcell sc.main.mdl

Visualize the results with CellBlender just like was done in the
:ref:`visualize_molecules` section. See if you can notice the **vol2**
molecules being destroyed by the absorptive surface.

.. _surf_class_rxns:

Surface Classes and Reactions
=============================================

In the :ref:`surf_class_vol_mol` section, we learned that surface classes can
be used to give parts of meshes special properties. Surface classes can also be
used to provide extra specificity over how reactions occur.

.. _surf_class_rxns_mesh:

More Mesh Modifications
---------------------------------------------

Watch the following video tutorial or follow along with the instructions below.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="960" height="540" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/surf_reg_inside.ogg" type='video/ogg'/>
    </video>

If you watched the previous video tutorial, you can skip ahead to
:ref:`surf_class_rxns_mdl`.

We need to make a few more changes to our Blender model to complete the next
section (:ref:`surf_class_rxns_mdl`). We're picking up where we left off at the
end of :ref:`surf_class_vm_mod_mesh`. In fact, the instructions will be very
similar, aside from a few minor changes.

While still in **Object Mode**, hit **Shift-a**, select **Plane**, and
**Enter** to confirm. Hit the **Object** button on the **Properties** Editor.
Under the **Surface Regions** panel, hit **+**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/inside.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/inside_triangulated.png

Change the newly created surface region text field from **New Region** to
**inside**. Change into **Edit Mode** by hitting **Tab**. With the face of the
plane selected, hit **Ctrl-t** to triangulate it. Under **Define Surface
Regions**, click **Assign**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/define_surf2.png

Expand the **Define Molecules** panel and hit the **+** button. Left click
**New Molecule**. Change the **Molecule Name** to **surf2**, the **Molecule
Type** to **Surface Molecule**, and the **Diffusion Constant** to **0**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/sc_rxn.png

Expand the **Define Reaction** panel and hit the **+** button. Change
**Reactants** to **vol1, + surf2' @ empty'**. Change **Products** to **surf2' +
vol2'**. Change **Forward Rate** to **1e8**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/getting_started/surf2_rel.png

Under the **Molecule Release/Placement** panel and hit the **+** button. Select
**New Release Site** from the list, and change **Site Name** to **surf2_rel**.
Change **Molecule** to **surf2;**. Change **Release Shape** to
**Object/Region**. Change **Object/Region** to **Plane.001[inside]**. Change
**Quantity to Release** to **2000**.

Hit the **Scene** button in the **Properties** Editor. Under **CellBlender
Project Settings**, select **Export CellBlender Project**. Navigate to the
directory where we will export the files (``/home/user/mcell_tutorial/sc_rxn``
where **user** is your user name) and hit **OK** when it prompts you to make a
new directory. Then select **Set Project Directory**. Set the **Project Base**
to **sc_rxn**. Then hit **Export CellBlender Project**, navigate to same
directory as before, and hit **Export MCell MDL**.

.. _surf_class_rxns_mdl:

More MDL Modifications
---------------------------------------------

Open **sc_rxns.surface_classes.mdl** in the new **sc_rxns** directory. Change
the **DEFINE_SURFACE_CLASSES** section as follows:

.. code-block:: none
    :emphasize-lines: 4

    DEFINE_SURFACE_CLASSES
    {
        absorb_vol1 {ABSORPTIVE = vol1}
        empty {}
    }

This new surface class, **empty**, is the simplest case you can have for a
surface class. By itself, it's not very useful, but we can use it in reactions.
Let's look at the **sc_rxns.reactions.mdl** file:

.. code-block:: none
    :emphasize-lines: 4

    DEFINE_REACTIONS 
    {
        vol1, + surf1' -> surf1' + vol2' [1E8]
        vol1, + surf2' @ empty' -> surf2' + vol2' [1E8]
    }   

The above change means that **vol1** will only react with the **BOTTOM** of
**surf** at the **BACK** of the **empty** surface class. This means the
reaction won't occur when the surface molecules diffuse away from surface
regions that have this surface class applied (i.e. when it diffuses away from
**top**). 

Lastly, change the **sc_rxns.mod_surf_regions.mdl** like this:

.. code-block:: none
    :emphasize-lines: 7-10

    MODIFY_SURFACE_REGIONS 
    {
        Plane[above]
        {
            SURFACE_CLASS = absorb_vol1
        }
        Plane.001[inside]
        {
            SURFACE_CLASS = empty
        }
    }

Save the file and run it with MCell by enterting the command::

    mcell sc_rxn.main.mdl

Visualize the results with CellBlender like was done in the
:ref:`visualize_molecules` section. You should notice that there are **vol2**
molecules being created inside the box, but only in the upper portion of it,
despite the fact that the **surf2** molecules are facing both up *and* down.
The reason for this is because the reaction is only taking place at the
**BACK** of the **empty** surface class with the **BOTTOM** of **surf2**.
