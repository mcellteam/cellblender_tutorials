.. _rel_pattern:

*********************************************
Release Patterns
*********************************************

.. CellBlender Source ID = 55f468aa7b71e044b3b199786f5af1d83bb3cab8
   Git Repo SHA1 ID: 76c4b2c18c851facefad7398f3f9c86a0abb8cdc

.. note::
    The simulations and visualizations in this tutorial were generated using
    Blender 2.67 and CellBlender 0.1.57. It may or may not work with other
    versions.

Release patterns allow you to release molecules at specified time intervals.
One thing this can be useful for is simulating a synaptic vesicle releasing
neurotransmitter.

Eventually, it will be possible to create release patterns directly within
CellBlender. Until that time, you can still do it by manually hand-editing some
files.

First, type the following command in the main tutorial directory::

   mkdir -p release_pattern/release_pattern_files/mcell

.. note::

   CellBlender expects a certain directory structure for visualization. That is
   why we are creating these sub-directories in a very specific way.

Then within that directory (i.e.
**/home/user/mcell_tutorial/release_pattern/release_pattern_files/mcell**),
create a file called **release_pattern.mdl**. Add the following text to that
file:

.. code-block:: none
    :emphasize-lines: 6-13, 28

    time_step = 1E-6
    iterations = 1000
    ITERATIONS = iterations
    TIME_STEP = time_step

    DEFINE_RELEASE_PATTERN rel_pat1
    {
        DELAY = 50E-6
        RELEASE_INTERVAL = 50E-6
        TRAIN_DURATION = 200E-6
        TRAIN_INTERVAL = 300E-6
        NUMBER_OF_TRAINS = 3
    }

    DEFINE_MOLECULES
    {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
    }

    DEFINE_REACTIONS {
        vol1 -> NULL [1E5]
    }

    INSTANTIATE World OBJECT
    {
        vol1_rel RELEASE_SITE
        {
            SHAPE = SPHERICAL
            LOCATION = [0,0,0]
            SITE_DIAMETER = 0.0
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 100
            RELEASE_PATTERN = rel_pat1
        }
    }

    sprintf(seed,"%05g",SEED)

    VIZ_OUTPUT
    {
      MODE = CELLBLENDER
      FILENAME = "./viz_data/seed_" & seed & "/Scene"
      MOLECULES
      {
        NAME_LIST {vol1}
        ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
      }
    }

    REACTION_DATA_OUTPUT
    {
      STEP=1e-05
      {COUNT[vol1,WORLD]}=> "./react_data/seed_" & seed & "/vol1.World.dat"
    }


A release pattern consists of one or more "trains." Each train can last for a
certain period of time (**TRAIN_DURATION**), and an interval between trains can
be set(**TRAIN_INTERVAL**). Within a given train, you can release molecules at
specific intervals (**RELEASE_INTERVALS**). And lastly, the **DELAY** indicates
when the first train will start. This may sound more confusing than it really
is. Plotting the reaction data should help illustrate what's happening for this
specific release pattern.

Running the Simulation and Visualizing the Results
---------------------------------------------

Run the file by typing::

    mcell release_pattern.mdl

Start Blender. Save your blend file with the name **release_pattern.blend** in
**/home/user/mcell_tutorial/release_pattern**. Be careful to name it correctly,
as the directory structure we set up earlier depends upon it. Normally, this is
all handled automatically by CellBlender, but we must be careful when
hand-editing files. Delete the default **Cube** now (select and hit **x**),
since it's not actually a part of our simulation. Hit **Read Viz Data** under
the **Visualize Simulation Results** panel. Hit **Ctrl-a** to begin playing the
animation. At the origin, you should see small bursts of molecules being
created (due to the actions of the release site and release pattern) and
quickly decaying (from by the reaction).
