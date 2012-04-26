.. _clamp:

.. index::
   single: CLAMP_CONC

*********************************************
Clamp Concentration
*********************************************

Clamp concentration lets you maintain a constant concentration of a molecule at a surface. This is done by creating and destroying molecules at the surface. **CLAMP_CONC** is created and applied like other surface classes (e.g. **ABSORPTIVE**). We'll begin by making two meshes, one which will have the **CLAMP_CONC** applied and the other will prevent molecules from diffusing away from the surface.

Start Blender. Hit **z** to switch to wireframe mode. With the **Cube** selected, hit **s**, **z**, **0.1**, and **Enter**. Hit **Shift-a**, select **Mesh>Plane**. Hit **s**, **0.9**, and **Enter**. Hit the **Material** button in the **Properties** window. Hit **New** and change the material name from **Material.001** to **clamp_sr**. Next, select **File>Export>Model Description Language (.mdl)**. Navigate to the directory where you want to create your file (e.g. **/home/user/mcell_tutorial/clamp_conc**). In the text field below the directory, type::

    clamp_conc.mdl

and hit **Export MDL**.

Now open **clamp_conc.mdl** and change **iterations** to **500**. Next, add in the following text after the **INCLUDE_FILE** commands::

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
    }

    DEFINE_SURFACE_CLASSES {
        clamp_sc {CLAMP_CONC vol1 = 1E-5}
    }  

    MODIFY_SURFACE_REGIONS {
        Plane[clamp_sr] {
            SURFACE_CLASS = clamp_sc
        }
    }

Finaly, add the following text to the end of the file::

    REACTION_DATA_OUTPUT {
        STEP=time_step
        {COUNT[vol1,World.Plane,ESTIMATE_CONC]}=> "./react_data/vol1.dat"
    }

Save and run the mdl by typing **mcell clamp_conc.mdl**. The only new commands here are **CLAMP_CONC** and **ESTIMATE_CONC**. **CLAMP_CONC** is applied like any other surface class, except that the molarity of a certain molecule is specified. **ESTIMATE_CONC** is used in a count statement after an object or region, and (unsurprisingly) estimates the concentration at that location. *Note:* The units for these two commands are different; **CLAMP_CONC** is M and **ESTIMATE_CONC** is uM.

In this example, we clamp the concentration of **vol1** at a molarity of **1E-5** M. When you plot the results, you'll notice that the concentration of molecules increases for a period of time and then reaches a steady state near 10 uM, which is what we would expect given what we asked for in the **CLAMP_CONC** command. 

