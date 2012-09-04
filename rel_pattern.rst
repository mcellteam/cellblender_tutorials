.. _rel_pattern:

*********************************************
Release Patterns
*********************************************

Release patterns allow you to release molecules at specified time intervals.
One thing this can be useful for is simulating a synaptic vesicle releasing
neurotransmitter. First, create a directory called **release_pattern** in the
main tutorial directory. Inside the new directory, create a file called
**release_pattern.mdl** and add the following text to it:

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

    VIZ_OUTPUT 
    {
        MODE = CELLBLENDER
        FILENAME = "./viz_data/release_pattern"
        MOLECULES 
        {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }
    }
    REACTION_DATA_OUTPUT 
    {
        STEP=time_step
        {COUNT[vol1,WORLD]}=> "./react_data/vol1.dat"
    }

A release pattern consists of one or more "trains." Each train can last for a
certain period of time (**TRAIN_DURATION**), and an interval between trains can
be set(**TRAIN_INTERVAL**). Within a given train, you can release molecules at
specific intervals (**RELEASE_INTERVALS**). And lastly, the **DELAY** indicates
when the first train will start. This may sound more confusing than it really
is. Plotting the reaction data should help illustrate what's happening for this
specific release pattern.

Run the file by typing::

    mcell release_pattern.mdl

