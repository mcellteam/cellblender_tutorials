.. _direct_t_cmp:

===============
Direct Transport with Compartments Model
===============

Description
===========

Similarly as in the :ref:`direct_t`, here we exemplified the usage of reactions with absolute orientation but this time also using compartments. Volume molecules **V**
in the interior of a cube react with surface molecules **S**, producing volume molecules **V** in the
exterior of the cube, inside the World (reaction **v@Cube** + **s@Membrane** -> **s@Membrane** + **V@World**).
The surface areas of the cube and the World (another cube) are made reflective to emulate a bigger surrounding environment, and keep the number of molecules constant in the interior of the World.

Demonstrated features
=====================

- Reactions with absolute orientation.
- A surface classes is used to make objects reflective.
