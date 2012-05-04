.. _examine_output:

*********************************************
Visualize and Plot the Output
*********************************************

In this section, we will run MCell on the MDL that we annotated in the previous section. This will generate visualization and reaction data (i.e. molecule counts), which we will then examine using CellBlender and some plotting software. 

.. _visualize_molecules:

Visualize the Molecules
=============================================

Visualize molecules with CellBlender in this video tutorial.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/dreamm_pt2.ogg" type='video/ogg'/>
    </video>

Skip to the next section (:ref:`custom_glyphs`) if you just watched the video tutorial.

Begin by opening Blender. Then click the **Scene** button. Select the **Visualize Simulation Results** panel, and click the **Set Molecule Viz Directory** button. Navigate to `/home/user/mcell_tutorial/intro/viz_data/` and click **Read Molecule Files**. You should now see a number of molecules populating the surface of the **Cube**. 

Let's change the Cube to a wireframe view so we can see inside of it. Click the **Object** button on the **Properties Editor**. Under the **Display** panel, change **Type** to **Wire**.

Drag the green bar on the timeline back and forth to scrub through the simulation. You can see the molecules diffusion in and on surface of the cube, and new molecules being created outside the cube.

.. _custom_glyphs:

Customize Molecule Glyphs
=============================================

Learn how to use custom glyphs for molecules using CellBlender in this video tutorial.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/dreamm_rendering.ogg" type='video/ogg'/>
    </video>

Skip to the next section (`Graph the Reaction Data`_) if you just watched the video tutorial.

By default, every molecule just shows up as a sphere. This might be fine for volume molecules, but you might one to be able to tell the orientation of your surface molecules, which we can do by using an asymmetrical glyph.

Expand **molecules** in the **Outliner** by clicking the small **+** sign beside it. This expands to reveal **mol_surf1**, **mol_vol1**, and **mol_vol2**. These correspond to the molecules we created in our simulation: **surf1**, **vol1**, and **vol2**. If you click the plus beside each of these, you will see **mol_surf1_shape**, **mol_vol1_shape**, and **mol_vol2_shape**. These are the actual glyph objects that get mapped onto the molecule locations.

Select **mol_surf1_shape** in the **Outliner**. Then click the **Material** button and navigate down to **Molecule Shape**. The shape should be set to **Cone** in the **Molecule Shape** drop down box. Click **Set Molecule Shape** to apply the selection. All of the **surf1** molecule glyphs should now be changed to cones. You may want to zoom in to get a better view of them.

.. _graph_rxn_data:

Graph the Reaction Data
=============================================

Change into the **react_data** directory by typing::

    cd react_data 

and enter the command::

    ls

You should see two files, **vol1.dat**, and **vol2.dat**.

Plot **vol1.dat** and **vol2.dat** with the graphing software of your choice. For something as simple as this, xmgrace or gnuplot will suffice. Although we don't need all the power (and complexity) of numpy and matplotlib right now, we'll introduce it here anyways, since we will be using it for some more advanced tasks later. First create a file called **plot.py** and put the following text into it::

    #!/usr/bin/env python

    import numpy as np
    import matplotlib.pyplot as plt 

    x1 = np.genfromtxt("./react_data/vol1.dat", dtype=float)[:, 0]
    y1 = np.genfromtxt("./react_data/vol1.dat", dtype=float)[:, 1]
    x2 = np.genfromtxt("./react_data/vol2.dat", dtype=float)[:, 0]
    y2 = np.genfromtxt("./react_data/vol2.dat", dtype=float)[:, 1]
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.show()

Run the file by entering the command::

    python plot.py.

You should notice that **vol1.dat** is decreasing and **vol2.dat** is increasing as expected. This can be a quick way to verify that our simulation is working as expected.

