.. _pbc:

*********************************************
Periodic Boundary Conditions
*********************************************

Overview
=============================================

There are two forms of periodic boundary conditions available in *MCell*:
traditional and mirrored geometry. 

With traditional PBCs, molecules simply wrap around when they hit the edge of
boundary. For instance, if a molecule hits the the positive X boundary of the
periodic box, then it will wrap around to the negative X boundary and continue
diffusing from there.

With the mirrored geometry form, the geometry is mirrored in adjacent boxes and
molecules do not wrap around. When a molecule hits a boundary, it will continue
diffusing in the mirrored adjacent geometry. _Note: this mirrored geometry does
not actually exist, but is made possible by keeping careful bookkeeping of all
the molecules and the location of the virtual box that they are in._

Usage
=============================================

Defining the Boundaries
---------------------------------------------

Periodic boundary conditions in *MCell* are used by defining a periodic box:

.. code-block:: mdl

    PERIODIC_BOX
    {
      CORNERS = [-0.2, -0.2, -0.2],[0.2, 0.2, 0.2]
      PERIODIC_TRADITIONAL = FALSE
      PERIODIC_X = TRUE
      PERIODIC_Y = TRUE
      PERIODIC_Z = TRUE
    }

Like a normal *MCell* **BOX** object, the **CORNERS** define the lower left and
upper right points of the box. Setting **PERIODIC_TRADITIONAL** to **FALSE**
will use the mirrored geometry form of periodic boundaries. Each axis can be
set to be periodic or not via the **PERIODIC_X/Y/Z** keywords.

There can only be one periodic box and you do **not** need to instantiate it.

Counting in Virtual Boxes
---------------------------------------------

Counting works very similarly to normal counting in MCell. However, if using
mirrored geometry, then you need to specify which "virtual" box that you're
counting in like this:

.. code-block:: mdl

    {COUNT[vm,Scene.cell,[1,-2,3]]}=> "./vm.000.dat"

Notice the section with the **[1,-2,3]**. The numbers refer to the X, Y, and Z
coordinates of the virtual box respectively. In this example, we are counting
all the vm molecules in Scene.cell that is one virtual box over in the positive
X direction, two virtual boxes over in the negative Y direction, and three
virtual boxes over in the positive Z direction.
