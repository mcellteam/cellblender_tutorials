.. _d_duplicate:

**********
Duplicate
**********

Duplicate
=========

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Panel:    :menuselection:`Tool Shelf --> Tools --> Mesh Tools --> Add: Duplicate`
   | Menu:     :menuselection:`Mesh --> Add Duplicate`
   | Hotkey:   :kbd:`Shift-D`


This tool simply duplicates the selected elements,
without creating any connections with the rest of the mesh (unlike extrude, for example),
and places the duplicate at the location of the original. Once the duplication is done,
only the *new* duplicated elements are selected,
and you are automatically placed in grab/move mode, so you can translate your copy elsewhere...

In the *Tool Shelf* are settings for *Vector* offset, *Proportional Editing*,
*Duplication Mode* (non-functional?), and *Axis Constraints*.

Note that duplicated elements belong to the same
vertex groups as the "original" ones.
The same goes for the material indices ,
the edge's *Sharp* and *Seam* flags, and probably for the other vertex/edge/face properties...
