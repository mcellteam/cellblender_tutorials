.. _seed:

*********************************************
Running Multiple Seed Values
*********************************************

.. warning::

   This tutorial has not yet been updated for CellBlender 1.0 RC. Therefore,
   some things might not work exactly as described.

In MCell, diffusion (amongst other things) happen stochastically. However, the
results are replicable as long as one provides the same seed value. Given this
stochastic nature, you can expect the data generated from a simulation to look
noisy, especially if the number of reacting molecules is small. We can overcome
this problem by running many different simulations, each with a different seed
value, and then averaging the results of all the simulations.

We'll begin by creating a directory called **seed**. Inside it, create an MDL
called **seed.mdl** with this text:

.. code-block:: none
    :emphasize-lines: 31,35-37

    iterations = 1000 
    time_step = 5e-6 
    ITERATIONS = iterations
    TIME_STEP = time_step

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol2 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol3 {DIFFUSION_CONSTANT_3D = 1E-6}
    }   

    DEFINE_REACTIONS {
        vol1 + vol2 -> vol1 + vol3 [1E7]
        vol1 + vol3 -> vol2 + vol3 [1E6]
    }   

    INSTANTIATE World OBJECT {
        Cube BOX {CORNERS = [-0.1,-0.1,-0.1],[0.1,0.1,0.1]}
        vol1_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 100 
        }   
        vol2_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = vol2
            NUMBER_TO_RELEASE = 100 
        }   
    }   

    sprintf(seed,"%04g",SEED)

    REACTION_DATA_OUTPUT {
        STEP=time_step
        {COUNT[vol1,WORLD]}=> "./react_data/vol1." & seed & ".dat"
        {COUNT[vol2,WORLD]}=> "./react_data/vol2." & seed & ".dat"
        {COUNT[vol3,WORLD]}=> "./react_data/vol3." & seed & ".dat"
    }

.. index::
    single: SEED

All the syntax should be familiar except for the line
**sprintf(seed,"%04g",SEED)**. This assigns the value of the **SEED** to the
variable **seed**. The **%04g** formats it so that there are four leading
zeros.

Next, create the following python script called **run_seeds.py**::

    #!/usr/bin/env python

    import os, sys
    
    if len(sys.argv) >= 2:
        mdl = sys.argv[1]
    else:
        mdl = raw_input('What mdl do you want to run?\n')

    for i in range(1, 21):
        os.system("mcell -seed %i %s" % (i, mdl))

This file is similar to the **scaling.py** file that we created in the
checkpointing section. This will run MCell twenty different times, each time
incrementing the seed value by one. Save and run this file. You should now have
sixty files in the **react_data** directory (20 for each molecule). Now we will
begin the process of averaging these results. Create a python script called
**avg_seeds.py** with the following text in it::

    #!/usr/bin/env python

    import numpy as np
    import matplotlib.pyplot as plt
    import os

    startOfFileToAverage = "vol1"      # beginning of filenames to average
                                       # over

    mol_counts = None
    files = os.listdir('react_data')   # build a list of reaction data file names
    files.sort()                       # sort that list alphabetically

    for f in files:                    # iterate over the list of file names
        if f.startswith(startOfFileToAverage):
            rxn_data = np.genfromtxt("./react_data/%s" % f, dtype=float)
            rxn_data = rxn_data[:, 1]  # take the second column
            plt.plot(rxn_data, '0.5')  # plot the results as a gray line
            if mol_counts is None:
                mol_counts = rxn_data
            else:
                # built up 2d array of molecule counts (one col/seed)
                mol_counts = np.column_stack((mol_counts, rxn_data))
        else:
            pass

    mol_counts = mol_counts.mean(axis=1)  # take the mean of the rows
    plt.plot(mol_counts, 'r')             # plot the results as a red line
    plt.show()                            # show the plot

This script will load (and plot) each of the twenty **vol1.####.dat** files
into a two dimensional array, take the mean of the rows, and plot the results.

Run the first script by typing the following commands::

    python run_seeds.py seed.mdl

Finally, run the second script by typing::

    python avg_seeds.py
