.. _d_insert_faces:

************
Insert Faces
************

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Panel:    :menuselection:`Tool Shelf --> Tools --> Mesh Tools --> Add: Inset Faces`
   | Menu:     :menuselection:`Mesh --> Faces --> Inset Faces`
   | Hotkey:   :kbd:`I`


This tool takes the currently selected faces and creates an inset of them,
with adjustable thickness and depth. Think of it as like creating an edge loop,
but relative to the selected edges, even in complex meshes.

The tool is modal, such that when you activate it,
you may adjust the thickness with your mouse position. You may also adjust the depth of the
inset during the modal operation by holding :kbd:`Ctrl`.

.. list-table::

   * - .. figure:: /images/blender_basics/mesh_tool_inset_before.png
          :width: 320px

          Selection to inset.

     - .. figure:: /images/blender_basics/mesh_tool_inset_after.png
          :width: 320px

          Selection with inset.

Options
=======

.. figure:: /images/blender_basics/mesh_tool_inset_settings.png

   Inset Operator Settings.

Boundary
   Determines whether open edges will be inset or not.
Offset Even
   Scale the offset to give more even thickness.
Offset Relative
   Scale the offset by surrounding geometry.
Thickness
   Set the size of the offset.
Depth
   Raise or lower the newly inset faces to add depth.
Outset
   Create an outset rather than an inset.
   Causes the geometry to be created surrounding selection (instead of within).
Select Outer
   Toggle which side of the inset is selected after operation.
Individual
   By default the Inset tool operates on the region around selected faces,
   but with this option each selected face can be inset on its own.
Interpolate
   Interpolate mesh data: e.g. UV's, vertex colors, weights... etc.
