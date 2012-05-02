*****************************************************
(Ir)reversible Unimolecular and Bimolecular Reactions
*****************************************************

Download the blend files used for these tutorials here_. You will still have to export and modify the mdls created here. Alternatively, you can download the completed `project files`_, which contains the blends and fully annotated mdls. Whichever one you choose to use, extract the archive, which will create a directory called **irrev_rev_uni_bi_blend** or **irrev_rev_uni_bi_complete**.

.. _here: https://www.mcell.psc.edu/tutorials/mdl/main/irrev_rev_uni_bi_blend.tgz

.. _project files: https://www.mcell.psc.edu/tutorials/mdl/main/irrev_rev_uni_bi_blend.tgz

Exercise #1 - Diffusion Through Concentric Shells
-----------------------------------------------------

Exporting the Blend
=====================================================

Start Blender. Load the **sphere.blend** file in the **sphere** directory. You should see a set of concentric, transparent spherical shells. Several CellBlender properties have already been applied. We will now export these mdls and create a molecule release site centered within the shells. Select **File>Export>Model Description Language (.mdl)**.

Annotating the MDL
=====================================================

We will now modify the MDL, so that we count the molecules as they pass through the shells. Add the following variables at the beginning of your blend::

    number_of_A = 1000
    diffusion_coefficient = 50 /* microns squared per sec */

    iterations = 1000
    time_step = 1e-6

    vol_1 = 0.00415274 /* cubic microns */
    vol_2 = 0.0140155
    vol_3 = 0.0332219
    vol_4 = 0.0648864
    vol_5 = 0.112124
    vol_6 = 0.178048
    vol_7 = 0.265775
    vol_8 = 0.378419
    vol_9 = 0.519091

    shell_vol_1 = vol_2 - vol_1
    shell_vol_2 = vol_3 - vol_2
    shell_vol_3 = vol_4 - vol_3
    shell_vol_4 = vol_5 - vol_4
    shell_vol_5 = vol_6 - vol_5
    shell_vol_6 = vol_7 - vol_6
    shell_vol_7 = vol_8 - vol_7
    shell_vol_8 = vol_9 - vol_8

After the DEFINE_MOLECULES section, add the following::

    DEFINE_SURFACE_CLASS transp {
        TRANSPARENT = A
    }

Before the **INSTANTIATE** sections, add this::

    MODIFY_SURFACE_REGIONS {
            Sphere_1 {
                    SURFACE_CLASS = transp
            }
            Sphere_2 {
                    SURFACE_CLASS = transp
            }
            Sphere_3 {
                    SURFACE_CLASS = transp
            }
            Sphere_4 {
                    SURFACE_CLASS = transp
            }
            Sphere_5 {
                    SURFACE_CLASS = transp
            }
            Sphere_6 {
                    SURFACE_CLASS = transp
            }
            Sphere_7 {
                    SURFACE_CLASS = transp
            }
            Sphere_8 {
                    SURFACE_CLASS = transp
            }
            Sphere_9 {
                    SURFACE_CLASS = transp
            }
    }

Next, add the following reaction data to the end of the file::

    REACTION_DATA_OUTPUT {
        OUTPUT_BUFFER_SIZE = 200
        STEP = time_step*1
        {COUNT [A, World.Sphere_1]} => "./reaction_data/"&seed&"_inner_sphere.dat"
        {COUNT [A, World.Sphere_2] - COUNT [A, World.Sphere_1]} => "./reaction_data/"&seed&"_shell_1.dat"
        {COUNT [A, World.Sphere_3] - COUNT [A, World.Sphere_2]} => "./reaction_data/"&seed&"_shell_2.dat"
        {COUNT [A, World.Sphere_4] - COUNT [A, World.Sphere_3]} => "./reaction_data/"&seed&"_shell_3.dat"
        {COUNT [A, World.Sphere_5] - COUNT [A, World.Sphere_4]} => "./reaction_data/"&seed&"_shell_4.dat"
        {COUNT [A, World.Sphere_6] - COUNT [A, World.Sphere_5]} => "./reaction_data/"&seed&"_shell_5.dat"
        {COUNT [A, World.Sphere_7] - COUNT [A, World.Sphere_6]} => "./reaction_data/"&seed&"_shell_6.dat"
        {COUNT [A, World.Sphere_8] - COUNT [A, World.Sphere_7]} => "./reaction_data/"&seed&"_shell_7.dat"
        {COUNT [A, World.Sphere_9] - COUNT [A, World.Sphere_8]} => "./reaction_data/"&seed&"_shell_8.dat"
        {COUNT [A, World.Sphere_1]/vol_1} => "./reaction_data/"&seed&"_conc_inner_sphere.dat"
        {(COUNT [A, World.Sphere_2] - COUNT [A, World.Sphere_1])/shell_vol_1} => "./reaction_data/"&seed&"_conc_shell_1.dat"
        {(COUNT [A, World.Sphere_3] - COUNT [A, World.Sphere_2])/shell_vol_2} => "./reaction_data/"&seed&"_conc_shell_2.dat"
        {(COUNT [A, World.Sphere_4] - COUNT [A, World.Sphere_3])/shell_vol_3} => "./reaction_data/"&seed&"_conc_shell_3.dat"
        {(COUNT [A, World.Sphere_5] - COUNT [A, World.Sphere_4])/shell_vol_4} => "./reaction_data/"&seed&"_conc_shell_4.dat"
        {(COUNT [A, World.Sphere_6] - COUNT [A, World.Sphere_5])/shell_vol_5} => "./reaction_data/"&seed&"_conc_shell_5.dat"
        {(COUNT [A, World.Sphere_7] - COUNT [A, World.Sphere_6])/shell_vol_6} => "./reaction_data/"&seed&"_conc_shell_6.dat"
        {(COUNT [A, World.Sphere_8] - COUNT [A, World.Sphere_7])/shell_vol_7} => "./reaction_data/"&seed&"_conc_shell_7.dat"
        {(COUNT [A, World.Sphere_9] - COUNT [A, World.Sphere_8])/shell_vol_8} => "./reaction_data/"&seed&"_conc_shell_8.dat"
    }

Run the Simulation and Analyze the Results
=====================================================

Copy the file **run_seeds.py** and **avg_seeds.py** that was created in :ref:`seed` by typing the following commands::

    cp /home/user/mcell_tutorial/seed/avg_seeds.py /home/user/irrev_rev_uni_bi/sphere/
    cp /home/user/mcell_tutorial/seed/run_seeds.py /home/user/irrev_rev_uni_bi/sphere/

Run the file by typing::

    python run_seeds.py

When prompted, type::

    sphere.mdl

After the simulation finishes running, enter this command::

    python avg_seeds.py

Now we need to plot the ratio of variance to the mean for the number of molecules in each shell. Create a file called **var_to_mean.py** and copy the following text into it::

    #!/usr/bin/env python

Exercise #2 - Sampling Box
-----------------------------------------------------

Start Blender. Load the **sampling_box.blend** file in the **sampling_box** directory.

In this simulation a reflective box is created and filled with a specified concentration of diffusing particles in random locations. A transparent box is placed inside the reflective box. Note the relative volumes of the two boxes and run the simulation. Create a file called **mean_and_var.py** and copy the following text into it::

    #!/usr/bin/env python

Run the file by entering the following command::

    python mean_and_var.py

This script will give you the mean and variance for the number of molecules in each box. Decrease the size of the inner box relative to the outer box and rerun the simulation. Do this repeatedly and note how the mean and variance values change. 

Exercise #3 - Irreverisble Unimolecular Reaction
-----------------------------------------------------

Steady State 
=====================================================
We now simulate an irreversible unimolecular reaction A :math:`\rightarrow` B with rate constant k1. Molecules of A are initially distributed at random within a reflective box. The simulation is run under steady state conditions. How? Predict the expected reaction rate. Run the simulation and plot the reaction data results for the number and concentration of B molecules as a function of time. What is the expected form of these results? Fit your results for the production of B and compare the obtained reaction rate to the expected value. Increase the initial concentration of A, rerun the simulation and again fit the results.

Non-Steady State 
=====================================================
Next simulate the irreversible reaction A :math:`\rightarrow` B under non-steady-state conditions. Run the simulation and plot the reaction data results for the number and concentration of A and B molecules as a function of time. What is the expected form of these results? What is the time of an e-fold reduction of A?  Fit your results for the decay of A and compare the obtained value of k1 to the input value. Run an XPPAUT simulation using the same reaction and parameter values. Export the results for the decay of A and plot together with the results from the MCell simulation.

Exercise #4 - Reverisble Unimolecular Reaction
-----------------------------------------------------


Non-Equilibrium 
=====================================================

Here we simulate the reversible reaction A :math:`\leftrightarrow` B with rate constants k1 and k2 starting from non-equilibrium initial conditions (only A present at time 0). Run the simulation and plot the results for A and B. Run an XPPAUT simulation using the same reaction and parameter values. Export the results for A and B and plot together with the results from the MCell simulation. Fit the MCell results for production of B. What is the value of the fitted parameter, and what is its relationship to the values of k1 and k2?

Equilibrium 
=====================================================
Now we simulate the reversible reaction A :math:`\leftrightarrow` B starting from equilibrium conditions, i.e., under conditions where the average fractional amounts of A and B will remain constant. How is this done? Use the statistics utility program to obtain the variance for the number of B molecules. Rerun the simulation while varying the fractional amounts of A and B. In each case determine the variance for B, and plot the resulting values as a function of fractional amount of B. What is the form of the resulting curve?

Exercise #5 - Irreverisble Bimolecular Reaction
-----------------------------------------------------

Steady State 
=====================================================
Simulate an irreversible bimolecular reaction A + R :math:`\rightarrow` AR with rate constant k1. Molecules of A and R are initially distributed at random within a reflective box. The simulation is run under steady state conditions. How? Predict the expected reaction rate. Run the simulation and plot the reaction data results for the number and concentration of AR molecules as a function of time. What is the expected form of these results? Fit your results for the production of AR and compare the obtained reaction rate to the expected value. Increase the initial concentration of A and/or R, rerun the simulation and again fit the results. How does the obtained rate now compare to the expected rate?

Non-Steady State 
=====================================================
Simulate the irreversible reaction A + R :math:`\rightarrow` AR under non-steady-state conditions. Run the simulation and plot the reaction data results for the number and concentration of A, R, and AR molecules as a function of time. Run an XPPAUT simulation using the same reaction and parameter values. Export the results and plot together with the results from the MCell simulation.

Exercise #6 - Reverisble Bimolecular Reaction
-----------------------------------------------------

Non-Equilibrium 
=====================================================
Simulate the reversible bimolecular reaction A + R :math:`\leftrightarrow` AR with rate constants k1 and k2 starting from non-equilibrium initial conditions (only A and R present at time 0). Run the simulation and plot the results for A, R, and AR. Run an XPPAUT simulation using the same reaction and parameter values. Export the results and plot together with the results from the MCell simulation. Fit the MCell results for production of AR. What is the value of the fitted parameter?

Equilibrium 
=====================================================
Simulate the reversible reaction A + R :math:`\leftrightarrow` AR starting from equilibrium conditions, i.e., under conditions where the average fractional amounts of A, R, and AR will remain constant. How is this done? Use the statistics utility program to obtain the variance for the number of AR molecules. Rerun the simulation while varying the fractional amounts of A, R, and AR. In each case determine the variance for AR, and plot the resulting values as a function of fractional amount of AR. What is the form of the resulting curve?

Bonus
-----------------------------------------------------

Consider the plots of variance as a function of fractional occupancy in Exercises #4 and 6 under equilibrium conditions. Explain the form of your results. Could these results have been predicted? If so, why and how?

