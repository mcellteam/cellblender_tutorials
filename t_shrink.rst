.. _t_shrink:

*************
Shrink Fatten
*************

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Panel:    :menuselection:`Tool Shelf --> Tools --> Transform --> Shrink/Fatten`
   | Menu:     :menuselection:`Mesh --> Transform --> Shrink/Fatten`
   | Hotkey:   :kbd:`Alt-S`


This tool translates selected vertices/edges/faces along their own normal
(perpendicular to the face), which, on "standard normal meshes", will shrink/fatten them.

This transform tool does not take into account the pivot point or transform orientation.

.. list-table::

   * - .. figure:: /images/blender_basics/shrinkflatten1.png
          :width: 200px

          Mesh before shrink/flatten.

     - .. figure:: /images/blender_basics/shrinkflatten2.png
          :width: 200px

          Inflated using a positive value.

     - .. figure:: /images/blender_basics/shrinkflatten3.png
          :width: 200px

          Shrunk using a negative value.