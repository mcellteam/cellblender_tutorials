.. _examine_output:

*********************************************
Examining the Output
*********************************************

In this section, we will run MCell on the MDL that we annotated in the previous section. This will generate visualization and reaction data (i.e. molecule counts), which we will then examine using DReAMM and some plotting software. 

.. _run_sim_again:

Run the Simulation again
=============================================

We've finished adding our changes. Let's rerun the simulation with MCell.

As before, navigate to the appropriate directory, enter the command:: 

    mcell intro.mdl

After it's finished running, enter the command::
    
    ls 

and you should see that a new directory called **react_data** has been created.

.. _visualize_molecules:

Visualize the Molecules
=============================================

Visualize molecules with DReAMM in this video tutorial.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/dreamm_pt2.ogg" type='video/ogg'/>
    </video>

Skip to the next section (`Customize Rendering Properties`_) if you just watched the video tutorial.

If you still have DReAMM open, hit the **Reimport** button and add the wireframe for **World.Cube** in the same way that you did in :ref:`visualize_mesh`. If you closed DReAMM, simply follow all the steps in :ref:`visualize_mesh` again. When you are finished, you should have the centered cube in the middle of the **DReAMM Image Window**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/volume_molecules.png

Select **Volume Molecules** in the **Import & Select Objects** window. Next, select **Add Filtered**. Click **Apply Operation**, and the volume molecules should appear in the  **DReAMM Image Window**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/surface_molecules.png

Select **Surface Molecules** in the **Import & Select Objects** window. **Add Filtered** should still be selected. Click **Apply Operation**, and the surface molecules should appear in the **DReAMM Image Window**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/play.png

Hit the Play button on the Sequencer and watch the molecules diffusing and reacting in the **DReAMM Image Window**.

*Note:* The "up" axis is the Z-axis in Blender, but the Y-axis in DReAMM, meaning that the **top** surface region is pointing straight toward you. You will probably want to rotate it to get a better view. **Left click** in the **DReAMM Image Window** and hit **Ctrl-R**. Now **left click and drag** upward until the **top** region is facing up. 

.. _custom_rendering:

Customize Rendering Properties
=============================================

Learn how to customize rendering properties with DReAMM in this video tutorial.

.. raw:: html

    <video id="my_video_1" class="video-js vjs-default-skin" controls
      preload="metadata" width="840" height="525" 
      data-setup='{"example_option":true}'>
      <source src="http://www.mcell.psc.edu/tutorials/videos/main/dreamm_rendering.ogg" type='video/ogg'/>
    </video>

Skip to the next section (`Graph the Reaction Data`_) if you just watched the video tutorial.

By default, every molecule just shows up as a white pixel. This might be fine if you only have one molecule in your simulation, but, for anything more complicated, you will probably want to be able to differentiate between them.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/set_rendering_prop.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/select_molecules.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/select_vol1.png

Hit the **Set Rendering Prop.** button. Select **Molecules** and then **vol1.**

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/set_red.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/sphere_height_radius.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/apply_op_once.png

Set the **(Front) Color** RGB values to **1,0,0** (for red). Change **Glyph** to **sphere(simple)**. Change **Height** and **Radius** to **0.02**. The hit the **Apply Operation Once** button. You should notice the change in the **DReAMM Image Window**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/select_vol2.png

Select **vol2** and deselect **vol1**. Change  the RGB value of the **(Front) Color** to **0,1,0** (for green). Hit **Apply Operation Once**. *Note*: The specific colors and values don't matter as long as we can easily tell everything apart.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/set_cyan.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/arrow.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/pt2/apply_op_once.png

Finally, we are going to add **surf1**, but we have a few more changes to make with this one since it is a surface molecule, and therefore has a directionality to it. First, select **surf1** and deselect **vol2**. Then change the RGB value to **0,1,1** (for cyan). Change the **Glyph** to **arrow(simple)**. Then, change the **Height** and **Radius** to **0.10** and **0.02** respectively. Finally, hit **Apply Operation Once**.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/main/dreamm/play.png

Hit the Play button on the Sequencer and watch the molecules diffusing and reacting in the **DReAMM Image Window**.

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

