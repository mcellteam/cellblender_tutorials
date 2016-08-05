.. _dynamic_geomeotry_overview:


*********************************************
Dynamic Geometry
*********************************************

.. warning::

   The dynamic geometry interface is very new and subject to change.


Dynamic Geometry Overview
---------------------------------------------

The dynamic geometry additions to CellBlender support generation of MCell-compatible
dynamic geometry MDL. These additions allow CellBlender users to do the following:

    * Use Blender's shape keys to define dynamic geometry inside CellBlender
    * Run a Python script defining geometry as a function of iteration/time step inside CellBlender


Dynamic Geometry with Blender Shape Keys
---------------------------------------------

.. image:: ./images/dynamic_geometry_shape_keys.gif


Dynamic Geometry with Python Scripting
---------------------------------------------

.. image:: ./images/dynamic_geometry_scripted.gif

A dynamic geometry Python script is responsible for generating a Python description of
an object's geometry given the current iteration (frame number) and time_step. CellBlender
will call your script to generate the MDL required for an MCell simulation, and it will also
either use that MDL for display or it may optionally call your script for the display. For
these reasons, your script should be as efficient as you can make it to speed up both runs
and display.

The following script was used to generate the dynamic tapered cube / pyramid shown above:

::

    # This script gets both its inputs and outputs from the environment:
    #
    #  frame_number is the frame number indexed from the start of the simulation
    #  time_step is the amount of time between each frame (same as CellBlender's time_step)
    #  points[] is a list of points where each point is a list of 3 doubles: x, y, z
    #  faces[] is a list of faces where each face is a list of 3 integer indexes of points (0 based)
    #
    # This script must fill out the points and faces lists for the time given by frame_number and time_step.
    # CellBlender will call this function repeatedly to create the dynamic MDL and possibly during display.

    import math

    points.clear()
    faces.clear()

    min_length = 0.5
    max_length = 2.0
    period_frames = 200

    sx = min_length + ( (max_length-min_length) * ( (1 - math.cos ( 2 * math.pi * frame_number / period_frames )) / 2 ) )
    sy = min_length + ( (max_length-min_length) * ( (1 - math.cos ( 2 * math.pi * frame_number / period_frames )) / 2 ) )
    sz = min_length + ( (max_length-min_length) * ( (1 - math.sin ( 2 * math.pi * frame_number / period_frames )) / 2 ) )
    sz = 2 * sz

    # These define the coordinates of the rectangular box
    points.append ( [  sx,  sy, -sz ] )
    points.append ( [  sx, -sy, -sz ] )
    points.append ( [ -sx, -sy, -sz ] )
    points.append ( [ -sx,  sy, -sz ] )
    points.append ( [  sx,  sy,  sz ] )
    points.append ( [  sx, -sy,  sz ] )
    points.append ( [ -sx, -sy,  sz ] )
    points.append ( [ -sx,  sy,  sz ] )

    # These define the faces of the rectangular box
    faces.append ( [ 1, 2, 3 ] )
    faces.append ( [ 7, 6, 5 ] )
    faces.append ( [ 4, 5, 1 ] )
    faces.append ( [ 5, 6, 2 ] )
    faces.append ( [ 2, 6, 7 ] )
    faces.append ( [ 0, 3, 7 ] )
    faces.append ( [ 0, 1, 3 ] )
    faces.append ( [ 4, 7, 5 ] )
    faces.append ( [ 0, 4, 1 ] )
    faces.append ( [ 1, 5, 2 ] )
    faces.append ( [ 3, 2, 7 ] )
    faces.append ( [ 4, 0, 7 ] )

    # Taper the box to get a different shape
    for i in range(len(points)):
        if points[i][2] > 0:
            # z coordinate is greater than 0 so shrink x and y coordinates
            points[i][0] = points[i][0] * 0.2
            points[i][1] = points[i][1] * 0.2
        else:
            # z coordinate is less than or equal to 0 so expand x and y coordinates
            points[i][0] = points[i][0] * 2
            points[i][1] = points[i][1] * 2

This preliminary version gets frame_number, time_step, points[], and faces[] from the local environment.
This is likely to change in the near future.

