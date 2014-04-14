FAQ
---------------------------------------------

**What are the units in MCell and CellBlender?**

In MCell, the units of space are microns, the units of time are seconds,
diffusion constants are :math:`cm^2/s`, unimolecular reactions are
:math:`s^{-1}`, volume-volume/volume-surface bimolecular reactions are
:math:`M^{-1}s^{-1}` , and surface-surface bimolecular reactions are
:math:`{\mu}m^2N^{-1}s^{-1}`. M refers to molarity, and N is the number of
reactants. One `blender unit`_ in CellBlender is equivalent to one micron.

.. _blender unit: http://wiki.blender.org/index.php/User:Rayek/Doc:2.6/Manual/Interface/Units

**Can I simulate moving meshes in MCell?**

Currently, dynamic meshes in MCell can only be accomplished, in a very limited
way, via checkpointing (:ref:`checkpointing`). With checkpointing, surface
molecules will attempt to snap to the nearest possible location. To be safe, it
is best if the mesh moves in small steps. Using dynamic meshes with volume
molecules raises additional problems. Since the volume molecules have no real
concept of being inside or outside of compartments, checkpointing only works if
the mesh is expanding relative to the volume molecules inside of it. Otherwise,
volume molecules that were once inside a mesh can end up outside of the mesh,
and vice versa. We are planning on adding more robust support for dynamic
meshes in the future.

**Can I change the default molecule size?**

Often, people mistakenly assume that the INTERACTION_RADIUS corresponds to a
molecule's true radius. In reality, molecules are points in MCell. As such,
molecules can be infinitely close to each other. The interaction radius is only
used for finding reaction partners. Reasonably small changes to the interaction
radius won't have any significant effect, and there is usually no reason to
change the default value.

**Why is MCell running so slow?**

Your simulation could be running slow for any number of reasons. Check
:ref:`optimize` for some possible solutions for speeding up your simulation.
