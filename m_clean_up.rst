.. _m_clean_up:

********
Clean up
********

These tools are to help cleanup degenerate geometry and fill in missing areas of a mesh.


Decimate Geometry
=================

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Clean up --> Decimate Geometry`


The Decimate Geometry tool allows you to reduce the vertex/face count of a mesh with minimal shape changes.

Ratio
   Ratio of triangles to reduce to.
Vertex Group
   Use the active vertex group as an influence.

   Weight
      Strength of the vertex group.
   Invert
      Inverts the vertex group.
Symmetry
   Maintain symmetry on either the *X*, *Y*, or *Z* axis.

.. seealso::

   This tool works similar to the Decimate Modifier.


Fill Holes
==========

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Clean up --> Fill Holes`


This tool is can take a large selection and detect the holes in the mesh, filling them in.

This is different from the face creation operator in three important respects:

- Holes are detected, so there is no need to manually find and select the edges around the holes.
- Holes can have a limit for the number of sides (so only quads or tris are filled in for example).
- Mesh data is copied from surrounding geometry (UVs, vertex-colors, multi-res, all layers),
  since manually creating this data is very time consuming.


Make Planar Faces
======================

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Clean up --> Make Planar Faces`


Split Non-Planar Faces
======================

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Clean up --> Split Non-Planar Faces`


This tool avoids ambiguous areas of geometry by splitting non-flat faces when they are bent
beyond a given limit.


Split Concave Faces
======================

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Clean up --> Split Concave Faces`

ToDo


Delete Loose Geometry
=====================

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Clean up --> Delete Loose`


This tool removes disconnected vertices and edges (optionally faces).


Degenerate Dissolve
===================

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Clean up --> Degenerate Dissolve`

This tool collapses / removes geometry which you typically will not want.

- Edges with no length.
- Faces with no areas (faces on a point or thin faces).
- Face corners with no area.
