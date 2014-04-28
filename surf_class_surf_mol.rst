.. _surf_class_surf_mol:

*********************************************
Surface Classes and Surface Molecules
*********************************************

.. Git Repo SHA1 ID: 3520f8694d61c81424ff15ff9e7a432e42f0623f

.. note::

    The simulations and visualizations in this tutorial were generated using
    Blender 2.70a and CellBlender 1.0. It may or may not work with other
    versions.

We have already discussed surface classes at length, but we haven't touched on
how they can affect the diffusion of surface molecules. Their effects are
manifested at the boundaries of the surface regions that they are applied to.
For example, if a surface is **Reflective** to **surf1**, then any **surf1**
can't get in or out of that that surface region. It acts as a fence of sorts
corralling the molecules in one region. The **Absorptive** surface class also
acts somewhat like a fence, but, instead of molecules harmlessly "bouncing" off
of it, they are destroyed whenever they touch it. **Transparent** surface
classes don't affect surface molecules, so we can ignore them in this context.

.. contents:: :local:

.. _surf_class_sm_mesh:

Set Project Directory
---------------------------------------------

Start Blender. Hit the **Scene** button in the **Properties Editor**. 

.. image:: ./images/scene_button.png

Let's save the file (and set the project directory) right now by hitting
**Ctrl-s**, typing **~/mcell_tutorial/sc_sm** (or **C:\\mcell_tutorial\\sc_sm**
on Windows) into the directory field, **sc_sm.blend** into the file name field,
and hit the **Save As Blender File** button.

Creating and Assigning Surface Regions
---------------------------------------------

With the default **Cube** selected, hit the **Object** button in the
**Properties Editor**.

.. image:: ./images/object_button.png

Expand the **Define Surface Regions** panel. Hit **+** twice so that you have
two new surface regions.

.. image:: ./images/surf_class_surf_mol/region_0_1.png

Click on the first one and change its name in the text field to **top**. Next,
click on the second entry and change its name to **bottom**.

.. image:: ./images/surf_class_surf_mol/bottom_top.png

Move your cursor to the **3D View** window and hit **Tab** to switch into
**Edit Mode**.  Hit **Ctrl-t** to triangulate the faces.

.. image:: ./images/triangulate.png

Then hit **Ctrl-Tab** and select **Face**.

.. image:: ./images/ctrl_tab.png

Hold **Shift** and **right click** on the top faces

.. image:: ./images/select_top.png

Select the **top** surface region from the list and click **Assign**.

.. image:: ./images/surf_class_surf_mol/bottom_top_assign.png

Next move your mouse back to the **3D View** window and hold the middle mouse
button down and drag upward so that the bottom faces are shown. Make sure
everything is deselected (Hit **a** until all the faces are gray). Then hold
**Shift** and **right click** on the bottom faces, select **bottom** from the
list of regions, and click **Assign**.


Add Cube to Model Objects List
---------------------------------------------

Hit the **Scene** button on the **Properties** Editor.

.. image:: ./images/scene_button.png

Expand the **Model Objects** panel. Hit the **+** button and **Cube** will
appear in the list.
 
.. image:: ./images/surf_class_surf_mol/model_objects.png

Set Simulation Parameters
---------------------------------------------

Next, expand the **Model Initialization** panel. Make the following changes:

* Change **Iterations** to **1000**.
* Change **Time Step** to **1e-4**.

.. image:: ./images/surf_class_surf_mol/model_init.png

Define a Surface Molecule
---------------------------------------------

Expand the **Define Molecules** panel and hit the **+** button.

* Change the **Molecule Name** to **surf1**.
* Change the **Molecule Type** to **Surface Molecule**.
* Change the **Diffusion Constant** to **1e-6**.

.. image:: ./images/surf_class_surf_mol/surf1.png

Define a Release Site
---------------------------------------------

Expand the **Molecule Release/Placement** panel and hit the **+** button.

* Change **Site Name** to **surf1_rel**.
* Change **Molecule** to **surf1**.
* Leave **Initial Orientation** set to **Top Front**.
* Leave **Release Shape** set to **Object/Region**.
* Change **Object/Region** to **Cube**.
* Change **Quantity to Release** to **1000**.

.. image:: ./images/surf_class_surf_mol/release_surf1.png

.. _scsm_add_surf_class:

Add the Surface Class
---------------------------------------------

Expand the **Define Surface Classes** panel. Then, hit the **+** button to
create a new surface class called **Surface_Class**. Rename it to
**absorb**.

Hit the **+** button beside the empty **absorb Properties** list.

* Select **surf1** from the **Molecule Name** field.
* Leave **Orientation** set to **Top/Front**.
* Leave **Type** set to **Absorptive**.

.. image:: ./images/surf_class_surf_mol/absorb.png

Repeat this process, except call the surface class **reflect** and change the
**Type** to **Reflective**.

.. image:: ./images/surf_class_surf_mol/reflect.png

.. _scsm_mod_surf_reg:

Modify the Surface Regions
---------------------------------------------

Now that we have created our surface class, we need to assign it to our mesh.
Expand the **Modify Surface Regions** panel. Hit the **+** to begin modifying a
surface region.

* In the **Surface Class Name** field, select **absorb**.
* Under **Object Name**, select the newly created **Cube** object.
* For **Region Name**, select **top**.

.. image:: ./images/surf_class_surf_mol/assign_absorb.png

Repeat this process, except select **reflect** for the **Surface Class Name**
and **bottom** for the region. 

.. image:: ./images/surf_class_surf_mol/assign_reflect.png

In this example, we have two surface classes, **absorb** and **reflect**.
**absorb** is applied to **top** and **reflect** is applied to **bottom**. The
faces in the middle do not have a surface region assigned to them. **surf1**
molecules are released all over the **Cube**, not just one surface region.

The effect of the **absorb** class is that all the **surf1** molecules are
destroyed when they hit the boundary between the **top** region and the
undefined middle section. The effect of the **reflect** class is that molecules
cannot pass the boundary between the **bottom** region and the undefined middle
section. Therefore, all the **surf1** molecules that start inside of the
**bottom** region never escape and the **surf1** molecules starting in the
middle section and **top** region will ultimately be destroyed.

.. _scsm_run_vis:

Run the Simulation and Visualize the Results
---------------------------------------------

Select **Export All** under **Visualization Output Settings**.

Save the Blender file (**Ctrl-s**) and hit the **Run Simulation** button under
the **Run Simulation** panel.

Once the simulation has finished running, hit **Read Viz Data** under the
**Visualize Simulation Results** panel. Hit **Alt-a** to play back the
animation. You should notice the **surf1** molecules being destroyed by the
absorptive surface boundary.
