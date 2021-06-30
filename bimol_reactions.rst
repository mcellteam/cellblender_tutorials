.. _bimol_reactions: 

*********************************************************
Bimolecular Reactions
*********************************************************

Tutorial Overview
=================

This tutorial will define a single bimolecular reaction.

Initial Configuration
=====================

This tutorial builds upon what was done in :ref:`unimol_reactions`. Either complete
that tutorial yourself or use the `unimol_reactions.blend`_ file to get started.

.. _unimol_reactions.blend: ../../blends/unimol_reactions.blend

Save the File with a New Name in Your Working Directory
---------------------------------------------------------------

* Select **File** > **Save As...**
* Change **add_meshgeom.blend** to **bimol_reactions.blend**
* Click **Save As Blender File** button

Define a New Molecule Type
-----------------------------------

* Click the **Molecules** button

.. image:: ./images/shared/button_panels/molecules_panel_h.png

* Click the "plus" sign (**+**) to the right of the **Defined Molecules** box
* Click in the **Molecule Name** field, type the letter **b** and press the
  Enter key
* Click in the **Diffusion Constant** box, type **1e-6** and press the Enter key

.. image:: ./images/bimol_reactions/define_b.png

Release "b" Molecules into the Simulation
-----------------------------------------------------

* Click the **Molecule Placement** button

.. image:: ./images/shared/button_panels/release_placement_panel_h.png

* Click the "plus" sign (**+**) to the right of the **Release/Placement Sites** box
* Click in the **Molecule** field, type **b** and hit enter
* Change **Release Shape** to **Object/Region**
* Type **Icosphere** in the **Object/Region** field
* Click in the **Quantity to Release** field and set it to **1000**

.. image:: ./images/bimol_reactions/release_site2.png

Define a Bimolecular Reaction
-----------------------------------

* Click the **Reactions** button.

.. image:: ./images/shared/button_panels/reactions_panel_h.png

* Change the **Reactants** text field from **a** to **a + b**
* Type **1e8** in the **Forward Rates** text field

.. image:: ./images/bimol_reactions/change_reaction.png

Simulate the Model
--------------------------

* Click the **Run Simulation** button

.. image:: ./images/shared/button_panels/run_panel_h.png

* Change the **Time Step** to **1e-5**
* Click the **Export & Run** button

.. image:: ./images/single_molecule/run_sim.png

* Wait for the simulation to complete
* Press the "Reload Visualization Data" button to load the results of the
  simulation.

.. image:: ./images/shared/button_panels/reload_viz_h.png

Change the Shape of "b"
--------------------------------------

* Click the **Molecules** button

.. image:: ./images/shared/button_panels/molecules_panel_h.png

* Open the **Display Options** subpanel if it isn't already
* Change the **Sphere_1** to **Cube**
* Change the **Scale** to **2.5**
* Change the color to a bright red

View the Results
-------------------------

* Press the "Play" (|play|) button below the time line

.. |play| image:: ./images/single_molecule/play.png

Save Your File
-------------------------

* **File** > **Save**
