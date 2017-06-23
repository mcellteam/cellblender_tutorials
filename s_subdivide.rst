.. _s_subdivide:

**********
Subdivide
**********

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Panel:    :menuselection:`Tool Shelf --> Tools --> Mesh Tools --> Add: Subdivide`
   | Menu:     :menuselection:`Mesh --> Edges --> Subdivide`,
     :menuselection:`Specials --> Subdivide/Subdivide Smooth`


Subdividing splits selected edges and faces by cutting them in half or more,
adding necessary vertices, and subdividing accordingly the faces involved,
following a few rules, depending on the settings:


- When only one edge of a face is selected (Triangle mode),
  triangles are subdivided into two triangles, and quads, into three triangles.
- When two edges of a face are selected:

  - If the face is a triangle, a new edge is created between the two new vertices,
    subdividing the triangle in a triangle and a quad.
  - If the face is a quad, and the edges are neighbors, we have *three* possible behaviors,
    depending on the setting of *Corner Cut Type* (the select menu next to the *Subdivide* button,
    in *Mesh Tools* panel) See below for details.
  - If the face is a quad, and the edges are opposite,
    the quad is just subdivided in two quads by the edge linking the two new vertices.

- When three edges of a face are selected:

  - If the face is a triangle, this means the whole face is selected and
    it is then sub-divided in four smaller triangles.
  - If the face is a quad, first the two opposite edges are subdivided as described above.
    Then, the "middle" edge is subdivided, affecting its new "sub-quad" as described above for only one edge.
- When four edges of a face (a quad) are selected, the face is subdivided into four smaller quads.


Options
=======

These options are available in the *Tool Panel* after running the tool;

Number of Cuts
   Specifies the number of cuts per edge to make.
   By default this is 1, cutting edges in half. A value of 2 will cut it into thirds, and so on.
Smoothness
   Displaces subdivisions to maintain approximate curvature,
   The effect is similar to the way the Subdivision Surface Modifier might deform the mesh.

   .. list-table::

      * - .. figure:: /images/blender_basics/subdivide-smooth-before.png
             :width: 200px

             Mesh before subdividing.

        - .. figure:: /images/blender_basics/subdivide-smooth-none.png
             :width: 200px

             Subdivided with no smoothing.

        - .. figure:: /images/blender_basics/subdivide-smooth-after.png
             :width: 200px

             Subdivided with smoothing of 1.


Quad/Tri Mode
   Forces subdivide to create triangles or quads instead of n-gons (see examples below).
   This mode doesn't allow the use of *Straight Cut* on quad corners.
Corner Cut Type
   This select menu controls the way quads with only two adjacent selected edges are subdivided.

   Fan
      The quad is sub-divided in a fan of four triangles,
      the common vertex being the one opposite to the selected edges.
   Inner vertices
      The selected edges are sub-divided, then an edge is created between
      the two new vertices, creating a small triangle.
      This edge is also sub-divided,
      and the "inner vertex" thus created is linked by another edge to the one opposite
      to the original selected edges. All this results in a quad sub-divided in a triangle and two quad.
   Path
      First an edge is created between the two opposite ends of the selected edges,
      dividing the quad in two triangles. Then, the same goes for the involved triangle as described above.
   Straight Cut
      .. (Todo) Au: Currently non functioning...

   .. list-table::

      * - .. figure:: /images/blender_basics/subdivide-twoedgesquad-fan2.png
             :width: 200px

             Fan cut type.

        - .. figure:: /images/blender_basics/subdivide-twoedgesquad-innervert.png
             :width: 200px

             Inner vertices cut type.

        - .. figure:: /images/blender_basics/subdivide-twoedgesquad-path.png
             :width: 200px

             Path cut type.


Fractal
   Displaces the vertices in random directions after the mesh is subdivided.

   .. list-table::

      * - .. figure:: /images/blender_basics/subdivide-fractal-before.png
             :width: 200px

             Plane before subdivision.

        - .. figure:: /images/blender_basics/subdivide-fractal-none.png
             :width: 200px

             Regular subdivision.

        - .. figure:: /images/blender_basics/subdivide-fractal-after1.png
             :width: 200px

             Same mesh with fractal added.


Along Normal
   Causes the vertices to move along the their normals, instead of random directions.

   .. figure:: /images/blender_basics/subdivide-fractal-alongnormal.png
      :width: 200px

      Along normal set to 1.


Random Seed
   Changes the random seed of the *Fractal* noise function, producing a different result for each seed value.

   .. figure:: /images/blender_basics/subdivide-fractal-after2.png
      :width: 200px

      Same mesh with a different seed value.


Examples
========

Below are several examples illustrating the various possibilities of the *Subdivide*
and *Subdivide Multi* tools. Note the selection after subdivision.

.. figure:: /images/blender_basics/subdivide-before.png
   :width: 300px

   The sample mesh.


One Edge
--------

.. list-table::

   * - .. figure:: /images/blender_basics/subdivide-oneedge.png
          :width: 250px

          One Edges.

     - .. figure:: /images/blender_basics/subdivide-oneedge-tri.png
          :width: 250px

          Quad/Tri Mode.


Two Tri Edges
-------------

.. list-table::

   * - .. figure:: /images/blender_basics/subdivide-twoedgestri.png
          :width: 250px

     - .. figure:: /images/blender_basics/subdivide-twoedgestri-tri.png
          :width: 250px

          Quad/Tri Mode.


Two Opposite Quad Edges
-----------------------

.. list-table::

   * - .. figure:: /images/blender_basics/subdivide-twoedgesopposite.png
          :width: 250px

     - .. figure:: /images/blender_basics/subdivide-twoedgesopposite-tri.png
          :width: 250px

          Quad/Tri Mode.


Two Adjacent Quad Edges
-----------------------

.. list-table::

   * - .. figure:: /images/blender_basics/subdivide-twoedgesquad-fan2.png
          :width: 250px

          Fan cut type.

     - .. figure:: /images/blender_basics/subdivide-twoedgesquad-fan.png
          :width: 250px

          Quad/Tri Mode.

.. list-table::

   * - .. figure:: /images/blender_basics/subdivide-twoedgesquad-innervert.png
          :width: 250px

          Innervert cut type.

     - .. figure:: /images/blender_basics/subdivide-twoedgesquad-innervert-tri.png
          :width: 250px

          Quad/Tri Mode.

.. list-table::

   * - .. figure:: /images/blender_basics/subdivide-twoedgesquad-path.png
          :width: 250px

          Path cut type.

     - .. figure:: /images/blender_basics/subdivide-twoedgesquad-path-tri.png
          :width: 250px

          Quad/Tri Mode.


Three Edges
-----------

.. list-table::

   * - .. figure:: /images/blender_basics/subdivide-threeedges.png
          :width: 250px

     - .. figure:: /images/blender_basics/subdivide-threeedges-tri.png
          :width: 250px

          Quad/Tri Mode.


Tri
---

.. list-table::

   * - .. figure:: /images/blender_basics/subdivide-threeedgestri.png
          :width: 250px

     - .. figure:: /images/blender_basics/subdivide-threeedgestri-tri.png
          :width: 250px

          Quad/Tri Mode.

Quad/Four Edges
---------------

.. list-table::

   * - .. figure:: /images/blender_basics/subdivide-fouredges.png
          :width: 250px

     - .. figure:: /images/blender_basics/subdivide-fouredges-tri.png
          :width: 250px

          Quad/Tri Mode.

Multicut
--------

.. list-table::

   * - .. figure:: /images/blender_basics/subdivide-tri-multi.png
          :width: 250px

          Tri with two cuts.

     - .. figure:: /images/blender_basics/subdivide-quad-multi.png
          :width: 250px

          Quad with two cuts

.. _mesh-unsubdivide:

Un-Subdivide
============

.. admonition:: Reference
   :class: refbox

   | Mode:     Edit Mode
   | Menu:     :menuselection:`Mesh --> Edges --> Un-Subdivide`

Unsubdivide functions as the reverse of subdivide by attempting to remove edges that were the
result of a subdivide operation.
If additional editing has been done after the subdivide operation,
unexpected results may occur.

Iterations
   How many subdivisions to remove.
