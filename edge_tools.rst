.. _edge_tools:

***********
Edge Tools
***********

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Edges`
   | Hotkey:   :kbd:`Ctrl-E`


Make Edge/Face
==============

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Panel:    :menuselection:`Tool Shelf --> Tools --> Mesh Tools --> Add: Make Edge/Face`
   | Menu:     :menuselection:`Mesh --> Edges --> Make Edge/Face`
   | Hotkey:   :kbd:`F`


It will create an edge or some faces, depending on your selection.


Set Edge Attributes
===================

Edges can have several different attributes that affect how certain other tools affect the mesh.


Mark Seam and Clear Seam
------------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode (Vertex or Edge select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Mark Seam/Clear Seam`

Seams are a way to create separations, "islands", in UV maps.
See the UVTexturing section for more details.
These operators set or unset this flag for selected edges.


Mark Sharp and Clear Sharp
--------------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode (Vertex or Edge select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Mark Seam/Clear Seam` (or the same options in *Edge Specials* menu)

The *Sharp* flag is used by the dge Split Modifier,
which is part of the smoothing techniques.
As seams, it is a property of edges, and these operators set or unset it for selected ones.


.. _modeling-edges-bevel-weight:

Adjust Bevel Weight
-------------------

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode (Vertex or Edge select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Edge Bevel Weight`


This edge property, a value between (0.0 to 1.0),
is used by the Bevel Modifier to control the bevel intensity of the edges.
This operator enters an interactive mode (a bit like transform tools),
where by moving the mouse (or typing a value with the keyboard)
you can set the (average) bevel weight of selected edges.


.. _modeling-edges-crease-subdivision:

Edge Crease
-----------

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode (Vertex or Edge select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Edge Crease`
   | Hotkey:   :kbd:`Shift-E`


This edge property, a value between (0.0 to 1.0), is used by the
Subdivision Surface Modifier
to control the sharpness of the edges in the subdivided mesh.
This operator enters an interactive mode (a bit like transform tools),
where by moving the mouse (or typing a value with the keyboard) you can set the (average)
crease value of selected edges.
A negative value will subtract from the actual crease value, if present.
To clear the crease edge property, enter a value of -1.


.. _modeling-meshes-editing-edge-slide:

Edge Slide
==========

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode (Vertex or Edge select modes)
   | Panel:    :menuselection:`Tool Shelf --> Tools --> Mesh Tools --> Deform: Slide Edge`
   | Menu:     :menuselection:`Mesh --> Edges --> Slide Edge`

Slides one or more edges across adjacent faces with a few restrictions involving the selection
of edges (i.e. the selection *must* define a valid loop, see below.)

Even :kbd:`E`
   Forces the edge loop to match the shape of the adjacent edge loop.
   You can flip to the opposite vertex using :kbd:`F`. Use :kbd:`Alt-Wheel` to change the control edge.
Flip :kbd:`F`
   When Even mode is active, this flips between the two adjacent edge loops the active edge loop will match.
Clamp :kbd:`Alt` or :kbd:`C`
   Toggle clamping the slide within the edge extents.

In *Proportional* mode, :kbd:`Wheel`, or :kbd:`Left` and :kbd:`Right`
changes the selected edge for calculating a proportion.
Unlike *Percentage* mode, *Proportional*

Factor
   Determines the amount of slide performed.
   Negative values correspond to slides toward one face, while positive ones, refer to the other one.
   It is also displayed in the 3D View footer.
Mirror Editing
   Lets you propagate the operation to the symmetrical elements of the mesh (if present, in local X direction).
Correct UVs
   Corrects the corresponding UV coordinates, if these exist, to avoid image distortions.


Usage
-----

By default, the position of vertices on the edge loop move as a percentage of the distance
between their original position and the adjacent edge loop, regardless of the edges' lengths.

.. list-table::

   * - .. figure:: /images/blender_basics/edgeslide1.png
          :width: 320px

          Selected Edge Loop.

     - .. figure:: /images/blender_basics/edgeslide2.png
          :width: 320px

          Repositioned Edge Loop.


Even mode
^^^^^^^^^

*Even* mode keeps the shape of the selected edge loop the same as one of the edge loops adjacent to it,
rather than sliding a percentage along each perpendicular edge.

In *Even* mode, the tool shows the position along the length of the currently selected edge
which is marked in yellow, from the vertex that as an enlarged red marker.
Movement of the sliding edge loop is restricted to this length. As you move the mouse the
length indicator in the header changes showing where along the length of the edge you are.

To change the control edge that determines the position of the edge loop,
use the :kbd:`Alt-Wheel` to scroll to a different edge.

.. list-table::

   * - .. figure:: /images/blender_basics/edgeslide3.png
          :width: 320px

          Even Mode Enabled.

     - .. figure:: /images/blender_basics/edgeslide4.png
          :width: 320px

          Even Mode with Flip Enabled.


Moving the mouse moves the selected edge loop towards or away from the start vertex,
but the loop line will only move as far as the length of the currently selected edge,
conforming to the shape of one of the bounding edge loops.


Limitations & Workarounds
^^^^^^^^^^^^^^^^^^^^^^^^^

There are restrictions on the type of edge selections that can be operated upon.
Invalid selections are:

Loop crosses itself
   This means that the tool could not find any suitable faces that were adjacent to the selected edge(s).
   Fig. Loop crosses is an example that shows this by selecting two edges that share the same face.
   A face cannot be adjacent to itself.
Multiple edge loops
   The selected edges are not in the same edge loop, which means they do not have a common edge.
   You can minimize this error by always selecting edges end to end or in a "Chain".
   If you select multiple edges just make sure they are connected.
   This will decrease the possibility of getting looping errors.
Border Edge
   When a single edge was selected in a single sided object.
   An edge loop cannot be found because there is only one face.
   Remember, edge loops are loops that span two or more faces.

A general rule of thumb is that if multiple edges are selected they should be connected end to
end such that they form a continuous chain. This is *literally* a general rule because you
can still select edges in a chain that are invalid because some of the edges in the chain are
in different edge loops.


.. _modeling-meshes-editing-edges-rotate:

Rotate Edge
===========

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode (Vertex or Edge select modes)
   | Menu:     :menuselection:`Mesh --> Edges --> Rotate Edge CW / Rotate Edge CCW`


Rotating an edge clockwise or counter-clockwise spins an edge between two faces around their
vertices. This is very useful for restructuring a mesh's topology.
The tool can operate on one explicitly selected edge,
or on two selected vertices or two selected faces that implicitly share an edge between them.

.. list-table::

   * - .. figure:: /images/blender_basics/edgeflip1.png
          :width: 320px

          Selected Edge.

     - .. figure:: /images/blender_basics/edgeflip2.png
          :width: 320px

          Edge, rotated CW.


Using Face Selection
--------------------

To rotate an edge based on faces you must select two faces, Fig. Adjacent selected faces,
otherwise Blender notifies you with an error message,
``"ERROR: Could not find any select edges that can be rotated"``. Using either *Rotate Edge CW*
or *Rotate Edge CCW* will produce exactly the same results as if you had
selected the common edge shown in Fig. Selected edge rotated CW and CCW.


Edge Split
==========

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Edges --> Edge Split`


*Edge Split* is similar to the *Rip* tool. When two or more touching interior edges,
or a border edge is selected when using *Edge Split*,
a hole will be created, and the selected edges are duplicated to form the border of the hole.

.. list-table::

   * - .. figure:: /images/blender_basics/edgesplit1.png
          :width: 320px

          Selected Edges.

     - .. figure:: /images/blender_basics/edgesplit2.png
          :width: 320px

          Adjacent face moved to reveal hole left by split.


.. _modeling-meshes-editing-bridge-edge-loops:

Bridge Edge Loops
=================

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Edges --> Bridge Edge Loops`


*Bridge Edge Loops* connects multiple edge loops with faces.

Connect Loops
   Open Loop
      Loops connected with open ends.
   Closed Loop
      Tries to connect to a circular loop (where start and end is merged).
   Loop pairs
      Connects each even count of loops individually.
Merge
   ToDo.
Merge Factor
   ToDo.
Twist
   Determines which vertices in both loops are connected to each other.
Number of Cuts
   The number of intermediate edge loops used to bridge the distance between two loops.
Interpolation
   Linear, Blend Path, Blend Surface
Smoothness
   Smoothness of the *Blend Path* and *Blend Surface*.
Profile Factor
   ToDo.
Profile Shape
   ToDo. Compare to Proportional Editing Falloff.


Examples
--------

Simple example showing two closed edge loops.

.. list-table::

   * - .. figure:: /images/blender_basics/mesh_bridge_simple_before.png
          :width: 320px

          Input.

     - .. figure:: /images/blender_basics/mesh_bridge_simple_after.png
          :width: 320px

          Bridge Result.

Example of bridge tool between edge loops with different numbers of vertices.

.. list-table::

   * - .. figure:: /images/blender_basics/mesh_bridge_uneven_before.png
          :width: 320px

          Input.

     - .. figure:: /images/blender_basics/mesh_bridge_uneven_after.png
          :width: 320px

          Bridge Result.

Example using the bridge tool to punch holes in face selections and connect them.

.. list-table::

   * - .. figure:: /images/blender_basics/mesh_bridge_faces_before.png
          :width: 320px

          Input.

     - .. figure:: /images/blender_basics/mesh_bridge_faces_after.png
          :width: 320px

          Bridge Result.

Example showing how bridge tool can detect multiple loops and loft them in one step.

.. list-table::

   * - .. figure:: /images/blender_basics/mesh_bridge_multi_before.png
          :width: 320px

          Input.

     - .. figure:: /images/blender_basics/mesh_bridge_multi_after.png
          :width: 320px

          Bridge Result.

Example of the subdivision option and surface blending with UV's.

.. list-table::

   * - .. figure:: /images/blender_basics/mesh_bridge_advanced_before.png
          :width: 320px

          Input.

     - .. figure:: /images/blender_basics/mesh_bridge_advanced_after.png
          :width: 320px

          Bridge Result.
