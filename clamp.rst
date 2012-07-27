.. _clamp:

.. index::
   single: CLAMP_CONC

*********************************************
Clamp Concentration
*********************************************

Clamp concentration lets you maintain a constant concentration of a molecule at a surface. This is done by creating and destroying molecules at the surface. **CLAMP_CONC** is created and applied like other surface classes (e.g. **ABSORPTIVE**). We'll begin by making two meshes, one which will have the **CLAMP_CONC** applied and the other will prevent molecules from diffusing away from the surface.

Creating the Model with Blender
---------------------------------------------
Start Blender. Hit **z** to switch to wireframe mode.
 
.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/clamp/scale_cube.png

With the **Cube** selected, hit **s**, **z**, **0.1**, and **Enter**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/clamp/triangulate_cube.png

Hit **Tab** to change into **Edit Mode**. Hit **Ctrl-t** to triangulate the faces of the **Cube**. Hit **Tab** to switch back into **Object Mode**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/clamp/plane.png

Hit **Shift-a**, select **Mesh>Plane**. Hit **s**, **0.9**, and **Enter**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/clamp/clamp_sr.png

Hit the **Object** button in the **Properties Editor**. Scroll to the bottom of the Editor. Expand the **Define Surface Regions** panel. Hit the **+** button and **New Region** should appear in the list of regions. Change the text field which reads **New Region** to **clamp_sr**. 

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/clamp/triangulate_plane.png

Move the cursor to the **3D View Editor**. Hit **Tab** to change into **Edit Mode**. Hit **Ctrl-t** to triangulate the faces.

Under the **Define Surface Regions** panel, click **Assign**. Hit **Tab** to change back into **Object Mode**. Hit the **Scene** button in the **Properties Editor**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/clamp/select_both.png

The **Plane** should still be selected, but we also want to select the **Cube**. Hold **Shift** and **right click** on the **Cube**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/clamp/model_objects_init.png

Expand the **Model Objects** panel and hit the **+** button. This will add the **Cube** and the **Plane** to the list of mesh objects to be exported and initialized. Expand the **Model Initialization** panel. Change **Simulation Iterations** to **500**. Change **Simulation Time Step** to **1e-6**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/clamp/define_molec.png

Expand the **Define Molecules** panel and hit the **+** button. Change the **Molecule Name** to **vol1**, the **Molecule Type** to **Volume Molecule**, and the **Diffusion Constant** to **1e-6**.

Under **Define Surface Classes**, select **Include Surface Classes** and **Include Modify Surface Regions**. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to the directory where we will export the files (**/home/user/mcell_tutorial/intro** where **user** is your user name) and hit **OK** when it prompts you to make a new directory. Then select **Set Project Directory**. Set the **Project Base** to **intro**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

Annotating the MDL
---------------------------------------------

Now create a file called **clamp_conc.surface_classes.mdl** with the following text:

.. code-block:: none
    :emphasize-lines: 3

    DEFINE_SURFACE_CLASSES 
    {
        clamp_sc {CLAMP_CONC vol1 = 1E-5}
    }

Now create a file called **clamp_conc.mod_surf_regions.mdl** with the following text:

.. code-block:: none
    :emphasize-lines: 5

    MODIFY_SURFACE_REGIONS 
    {
        Plane[clamp_sr] 
        {
            SURFACE_CLASS = clamp_sc
        }
    }

Finally, create a file called **clamp_conc.rxn_output.mdl** with the following text:

.. code-block:: none
    :emphasize-lines: 4

    REACTION_DATA_OUTPUT 
    {
        STEP=time_step
        {COUNT[vol1,World.Plane,ESTIMATE_CONC]}=> "./react_data/vol1.dat"
    }

Save and run the mdl by enter the following command::

    mcell clamp_conc.main.mdl

The only new commands here are **CLAMP_CONC** and **ESTIMATE_CONC**. **CLAMP_CONC** is applied like any other surface class, except that the molarity of a certain molecule is specified. **ESTIMATE_CONC** is used in a count statement after an object or region, and (unsurprisingly) estimates the concentration at that location. *Note:* The units for these two commands are different; **CLAMP_CONC** is M and **ESTIMATE_CONC** is uM.

In this example, we clamp the concentration of **vol1** at a molarity of **1E-5** M. When you plot the results, you'll notice that the concentration of molecules increases for a period of time and then reaches a steady state near 10 uM, which is what we would expect given what we asked for in the **CLAMP_CONC** command. 

