*********************************************************
Single Molecule Diffusion
*********************************************************

Required software
=================

This tutorial is designed for `Blender 2.74`_, `CellBlender 1.0 RC3`_, and `MCell
3.2.1`_.

.. _Blender 2.74: http://www.blender.org/download/
.. _CellBlender 1.0 RC3: http://mmbios.org/index.php/cellblender-all/cellblender-cellblender-1-0_rc3
.. _MCell 3.2.1: http://mmbios.org/index.php/mcell-3-2-1

.. note:: Other versions may work as well.


Tutorial Overview
=================

This tutorial will define a single molecule and show its diffusion.


Initial Configuration
=====================

Start with a "clean slate" by following the `Start with a Clean Slate Tutorial`_ then return here.

.. _`Start with a Clean Slate Tutorial`: start_with_clean_slate.html

Step 1: Save the file with a new name in your working directory
---------------------------------------------------------------

* File / Save As...
* Change "untitled.blend" to "single_molecule.blend"
* Click "Save As Blender File" button


Step 2: Define a Molecule "species"
-----------------------------------

* Click the "Molecules" button
* Click the "plus" sign (+) to the right of the "Defined Molecules" box
* Click in the Molecule Name field, type the letter 'a' and press the Enter key
* The new molecule "a" should have a green check mark in the "Defined Molecules" box
* Click in the "Diffusion Constant" box, type "1e-6" and press the Enter key

Step 3: Release a Single Molecule into the Simulation
-----------------------------------------------------

* Click the "Molecule Placement" button
* Click the "plus" sign (+) to the right of the "Release/Placement Sites" box
* Click in the Molecule field and select the "a" molecules
* Click in the "Quantity to Release" field and change set it to 1

Step 4: Simulate the Model
--------------------------

* Click the "Run Simulation" button
* Optionally change the "Command Line" to "Java Control" or another simulation runner
* Click the "Export & Run" button
* Wait for the simulation to complete and close any simulation runner window that popped up
* Press the "Reload Visualization Data" button to load the results of the simulation.

Step 5: Change settings to see results
--------------------------------------

* Hide the "Manipulator"
* Click the Molecules button
* Open the "Display Options" subpanel
* Change the "Cone" to "Torus"
* Change the Scale to 10
* Change the color to a bright yellow
* Press the "Play" button below the time line
* Use the scroll wheel to zoom in until you can see the moving torus

.. note:: You'll notice that there are actually 2 torus objects. One of them should be
  moving as the simulation is played, and the other should be stationary at the origin.
  The torus at the origin is really a "template" molecule used by Blender. There will
  generally be a template molecule at the origin for every molecule species you define.

Step 6: Use the Time Line
-------------------------

* Stop the simulation by clicking the "Pause" button below the time line
* Click at various locations on the time line to see the molecule state at that time
* Click and drag in the time line to "scrub" the simulation through time

Step 7: Save your File
-------------------------

* File / Save

