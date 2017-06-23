.. _make_edge_face:

***************
Make Edge/Face
***************

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Faces --> Make Face/Edge`
   | Hotkey:   :kbd:`F`


This is a context-sensitive tool which creates geometry by filling in the selection.
When only two vertices are selected it will create an edge, otherwise it will create faces.


The typical use case is to select vertices and press :kbd:`F`,
however, Blender also supports creating faces from different selections to help quickly build
up geometry.


Methods
=======

The following methods are used automatically depending on the context.


Isolated vertices
------------------

.. list-table::

   * - .. figure:: /images/blender_basics/bmesh_make_face_verts_simple_before.png
          :width: 200px

          Before.

     - .. figure:: /images/blender_basics/bmesh_make_face_verts_simple_after.png
          :width: 200px

          After.


Isolated edges
--------------

.. list-table::

   * - .. figure:: /images/blender_basics/bmesh_make_face_edges_simple_before.png
          :width: 200px

          Before.

     - .. figure:: /images/blender_basics/bmesh_make_face_edges_simple_after.png
          :width: 200px

          After.


N-gon from edges
----------------

When there are many edges Blender will make an n-gon,
note that this does not support holes, to support holes you need to use the
:ref:`modeling-meshes-editing-fill` Faces tool.

.. list-table::

   * - .. figure:: /images/blender_basics/bmesh_make_face_edges_ngon_before.png
          :width: 200px

          Before.

     - .. figure:: /images/blender_basics/bmesh_make_face_edges_ngon_simple_after.png
          :width: 200px

          After.


Mixed vertices/edges
--------------------

Existing edges are used to make the face as well as an extra vertex.

.. list-table::

   * - .. figure:: /images/blender_basics/bmesh_make_face_mix_simple_before.png
          :width: 200px

          Before.

     - .. figure:: /images/blender_basics/bmesh_make_face_mix_simple_after.png
          :width: 200px

          After.


Edge-Net
--------

Sometimes you may have many connected edges without interior faces.

.. list-table::

   * - .. figure:: /images/blender_basics/bmesh_make_face_net_before.png
          :width: 200px

          Before.

     - .. figure:: /images/blender_basics/bmesh_make_face_net_after.png
          :width: 200px

          After.


Point Cloud
------------

When there are many isolated vertices,
Blender will calculate the edges for an n-gon.

.. list-table::

   * - .. figure:: /images/blender_basics/bmesh_make_face_cloud_before.png
          :width: 200px

          Before.

     - .. figure:: /images/blender_basics/bmesh_make_face_cloud_after.png
          :width: 200px

          After.


Single Vertex Selection
-----------------------

With a single vertex selected on a boundary,
the face will be created along the boundary,
this saves manually selecting the other two vertices.
Notice this tool can run multiple times to continue creating faces.

.. figure:: /images/blender_basics/mesh_face_create_boundary.png
