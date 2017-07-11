.. _pbc:

*********************************************
Periodic Boundary Conditions
*********************************************

Overview
=============================================

There are two forms of periodic boundary conditions available in *MCell*:
traditional and mirrored geometry. 

With traditional PBCs, molecules simply wrap around when they hit the edge of
boundary. For instance, if a molecule hits the the positive X boundary of the
periodic box, then it will wrap around to the negative X boundary and continue
diffusing from there.

With the mirrored geometry form, the geometry is mirrored in adjacent boxes and
molecules do not wrap around. When a molecule hits a boundary, it will continue
diffusing in the mirrored adjacent geometry. 

.. note::

    The mirrored geometry does not actually exist but is made possible by
    keeping careful bookkeeping of all the molecules and the location of the
    virtual box that they are in.

Usage
=============================================

Getting started
---------------------------------------------
        * Define the molecule

            * Create a molecule by pressing the **Plus** button and name it **vm**.
            * Change the diffusion constant to **1e-6**.

              .. image:: ./images/pbc/defined_molecules.png

        * Place the molecule

            * Create a release site by pressing the **Plus** button and name it **rel_vm**.
            * Set the molecule to **vm**.
            * Set the release location to **.495**.
            * Set the quantity to release **1000**.

              .. image:: ./images/pbc/molecule_release.png

        * Create the sampling box  

            * Create a new cube by selecting the **cube object** button 
            * Add it by selecting the **Plus** button. 
            * Select the **Diffuse material** button.

               .. image:: ./images/pbc/add_samplingbox.png

            * Change the options of the cube.

                * Change the draw type to **Textured**.
                * Check the **Object Transparent** box.
                * Check the **Material Transparent** box.
                * Change **Alpha** to **0.250**

                .. image:: ./images/pbc/sampling_box_options.png

        * Set the sampling box dimensions 

                * With the cursor in the 3D window switch to edit mode[**Tab key**], keep the cursor in the 3D window and press the **s** key then press the **x** key and then type in **.5**. Then press the **s** key again and press **x** and type in **.498**.

                * Then press the **s** key and press **y** and type in **.5**, then press **s** again and press **y**  and type in **0.198**.
                * Then press the **s** key and press **z** and type in **.5**, then press **s** again and press **z**  and type in **0.198**.

                * **You may need to set the x location to [.250] or such to line it up within the wire(box)**.

        * Create the plane object

                * Select **plane object** button 
                * Add it by selecting the **plus** button
                * Select the **Diffuse material** button 

                .. image:: ./images/pbc/add_plane.png

                * Change the options of the plane.

                  * Change the draw type to **Textured**.
                  * Check the **Object Transparent** box.
                  * Check the **Material Transparent** box.
                  * Change **Alpha** to **0.250**

                  .. image:: ./images/pbc/plane_object_options.png      

        * Set the plane's dimensions 

                * With the cursor in the 3D window switch to edit mode[**Tab key**], keep the cursor in the 3D window and press the **s** key and press **y** and type in **.5**, then press **s** again and press **y**  and type in **0.220**.

                * Then press the **s** key and press **z** and type in **.5**, then press **s** again and press **z**  and type in **0.220**.          

                * **Note** you may need to alter the rotation of an axis to align the plane with the cube. 

        * Create the (cube)wire box

                * Select the **Cube object** button.
                * Add it by selecting the **Plus** button.

                .. image:: ./images/pbc/add_wired_cube.png  
                
                * Change the draw type to **Textured**.

                .. image:: ./images/pbc/wire_cube_options.png   

        * Set the cube(wire) dimensions 

                * With the cursor in the 3D window switch to edit mode[**Tab key**], keep the cursor in the 3D window and press the **s** key then press the **x** key and then type in **.5**. 

                * Then press the **s** key and press **y** and type in **.5**, then press **s** again and type in **0.2**. 
                * Then press the **s** again and press **z** and type in **.5**, then press **s** again and type in **0.2**.

        * Then remove it from the object list by having the cube object selected and press the **Minus** button.

                .. image:: ./images/pbc/remove_cube_object.png              

        * create a surface class

            * Press the **Plus** Button and rename it to **Transp**.

            .. image:: ./images/pbc/add_transp.png

            * Add the **Transp** properties by selecting the **Plus** button.
            * Change molecules to **All Molecules**.
            * Change orientation to **Ignore**.
            * Change Type to **Transparent**.

            .. image:: ./images/pbc/transp_properties.png

        *  Assign the surface class 

            * Add a new one by selecting the **Plus** button.
            * Change the **Surface Class Name** to **transp**.
            * Change **Object Name** to **sampling_box**.

            .. image:: ./images/pbc/assign_surface_class.png

        * Count the molecules.

            * In the world.

              * Press the **Plus button** to add a new counter
              * Set the molecule to **vm**.

                 .. image:: ./images/pbc/count_vm_world.png              

            * In the sampling box.

              * Press the **Plus button** to add a new counter
              * Set the molecule to **vm**.
              * Select **Object**. 
              * Change  object to **sampling_box**.              

                 .. image:: ./images/pbc/count_vm_samplingbox.png

Defining the Boundaries
---------------------------------------------

**First make sure that all objects are lined up. The plane should be vertical in the middle of the wire box, and the sampling box should take up half of the wire box.**

Periodic boundary conditions in *MCell* are used by defining a periodic box:

* First select the **Periodic boundary conditions** Button

   .. image:: ./images/pbc/pbc_sel.png

* Select the include checkbox

   .. image:: ./images/pbc/pbc_include.png

* Make sure that these boxes are checked

   .. image:: ./images/pbc/checked_true.png

* Set the Bounds of the condition:

  * **X-Start** = -0.5, **Y-Start** = -0.1, **Z-Start** = -0.1 
  * **X-End**   = 0.5,  **Y-End**   = 0.1,  **Z-End**   = 0.1 

   .. image:: ./images/pbc/pbc_values.png   

Like a normal *MCell* **BOX** object, the **CORNERS** define the lower left and
upper right points of the box. Setting **PERIODIC_TRADITIONAL** to **FALSE**
will use the mirrored geometry form of periodic boundaries. Each axis can be
set to be periodic or not via the **PERIODIC_X/Y/Z** keywords.

There can only be one periodic box and you do **not** need to instantiate it.

**Export and run the simulation, then reload the visualization.**

..Counting in Virtual Boxes
..---------------------------------------------

..Counting works very similarly to normal counting in MCell. However, if using
..mirrored geometry, then you need to specify which "virtual" box that you're
..counting in like this:


..Notice the section with the **[1,-2,3]**. The numbers refer to the X, Y, and Z
..coordinates of the virtual box respectively. In this example, we are counting
..all the vm molecules in Scene.cell that is one virtual box over in the positive
..X direction, two virtual boxes over in the negative Y direction, and three
..virtual boxes over in the positive Z direction.