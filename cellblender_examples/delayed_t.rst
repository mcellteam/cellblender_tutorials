.. _delayed_t:

=======================
Delayed Transport Model
=======================

Description
===========

This example illustrates the usage of reactions with absolute orientation with delay. Volume molecules **v**
in the interior of a cube can bind to surface molecules **s**, producing surface molecules **sv** in the
surface of the cube (reaction **v@IN** + **s** -> **sv**). These molecules **sv** can further react, releasing **r** molecules in the exterior of the cube and generating new surface molecules **s** (reaction **sv** -> **s** + **r@OUT**).


Demonstrated features
=====================

- Reactions with absolute orientation.
