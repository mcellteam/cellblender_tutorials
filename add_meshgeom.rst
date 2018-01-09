.. _add_meshgeom: 

*********************************************************
Add Simple Mesh Geometry
*********************************************************

Tutorial Overview
=================

In this tutorial, a sphere will be added to the simulation around the diffusing
molecules.

Initial Configuration
=====================

This tutorial builds upon what was done in :ref:`unimol_reactions`. Either
complete that tutorial yourself or use the `unimol_reactions.blend`_ file to
get started.

.. _unimol_reactions.blend: ./blends/unimol_reactions.blend

Save the File with a New Name in Your Working Directory
---------------------------------------------------------------

* Select **File** > **Save As...**
* Change **unimol_reactions.blend** to **add_meshgeom.blend**
* Click **Save As Blender File** button

Add a Sphere
---------------------------------------------------------------

* Click the **Model Objects** button to open the Model Objects panel

.. image:: ./images/add_meshgeom/add_icosphere_model_object1.png

When you create new objects, Blender will place them at the location
of the 3D cursor (|cursor3d|). To create a new sphere object at the
origin, be sure to center the 3D cursor in all 3 dimensions. The Model
Objects panel includes a convenient button for that purpose:

.. |cursor3d| image:: ./images/shared/blender_3d_cursor_icon_20.png

.. image:: ./images/add_meshgeom/add_icosphere_model_object2.png

* With the cursor centered, click the **icosphere** button to create a new icosphere at the 3D cursor location

.. image:: ./images/add_meshgeom/add_icosphere_model_object3.png

* The **Add Ico Sphere** options panel will appear in the lower left corner
* Change **Subdivisions** to **3**
* Change **Size** to **0.5**
* Change each **Location** (**X**, **Y**, and **Z**) to **0.0** if it isn't set
  already.

.. image:: ./images/add_meshgeom/add_icosphere2.png

Add the new Sphere to the Model Objects
---------------------------------------------------------------

* Click the "plus" sign (**+**) to the right of the **Model Objects** box
* Expand the **Icosphere Display Options** panel
* Select **Wire** from the drop-down menu (may originally show "Solid").

.. image:: ./images/add_meshgeom/model_objects.png

Release Molecules inside Sphere
---------------------------------------------------------------

* Click the **Molecule Placement** button
* Select **Release_Site_1** (should already be selected)
* Change **Release Shape** to **Object/Region**
* Type "**Icosphere**" in the **Object/Region** field
* Change **Quantity to Release** to **1000**

.. image:: ./images/add_meshgeom/sphere_release.png

Simulate the Model
--------------------------

* Click the **Run Simulation** button

.. image:: ./images/single_molecule/run_sim_button.png

* Click the **Export & Run** button

.. image:: ./images/single_molecule/run_sim.png

* Wait for the simulation to complete
* Press the "Reload Visualization Data" button to load the results of the
  simulation.

.. image:: ./images/single_molecule/reload_viz_data.png

View the Results
-------------------------

* Press the "Play" (|play|) button below the time line

.. image:: ./images/add_meshgeom/diffuse_in_sphere.png

.. |play| image:: ./images/single_molecule/play.png

Save Your File
-------------------------

* **File** > **Save**
