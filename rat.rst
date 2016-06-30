.. _rat:

*********************************************
Rat Neuromuscular Junction
*********************************************

.. Git Repo SHA1 ID: a1abdd291b75176d6581df41329781ae5d5e1b7d

.. note::

    The simulations and visualizations in this tutorial were generated using
    Blender 2.67 and CellBlender 1.0 RC. It may or may not work with other
    versions.

This tutorial is simply a follow-up to `Section 4.5, Example Model:
Acetylcholine Exocytosis and Miniature Endplate Current Generation at a
realistic Neuromuscular Junction
<http://papers.cnl.salk.edu/PDFs/Monte%20Carlo%20Methods%20for%20Simulating%20Realistic%20Synaptic%20Microphysiology%20Using%20MCell%202001-3290.pdf>`_
of Computational Neuroscience: Realistic Modeling for Experimentalists, ed. Dr.
Erik Schutter.

The MCell MDLs and Blend file for this model are available here as a `ZIP
archive`_. The MDLs in this project required some hand-editing, because release
patterns are not yet supported in CellBlender. As such, we have to be careful
we don't overwrite these hand-edited changes. Normally, when a user hits the
**Run Simulation** button, it is actually exporting the MDLs *and* then running
the simulation. However, there is an advanced option called **Decouple Export
and Run** under the **Preferences** panel that is very useful for exactly this
situation (i.e. when you need to run a simulation, but you don't want to
overwrite your existing MDLs). 

.. warning::

   Do *not* hit the **Export Project** button, unless you know what you are
   doing.  Otherwise, you will overwrite hand-edited changes made to the MDLs.

After extracting the zip file, open **rat_nmj.blend**. First, we need to tell
CellBlender where **MCell** is located. Under **Project Settings**, hit **Set
Path to MCell Binary**, navigate to where you have downloaded MCell, select it,
and hit the **Set MCell Binary** button. Next, hit the **Run Simulation**
button. Once the simulation has completed, hit the **Read Viz Data** button.
Hit **Alt-a** to play through the visualization data. 

.. _ZIP archive: https://www.mcell.psc.edu/tutorials/downloads/rat_nmj.zip
