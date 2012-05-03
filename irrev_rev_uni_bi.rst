*****************************************************
(Ir)reversible Unimolecular and Bimolecular Reactions
*****************************************************

Download the blend files used for these tutorials here_. You will still have to export and modify the mdls created. Alternatively, you can download the completed `project files`_, which contains the blends and fully annotated mdls. Whichever one you choose to use, extract the archive, which will create a directory called **irrev_rev_uni_bi_blend** or **irrev_rev_uni_bi_complete**.

.. _here: https://www.mcell.psc.edu/tutorials/mdl/main/irrev_rev_uni_bi_blend.tgz

.. _project files: https://www.mcell.psc.edu/tutorials/mdl/main/irrev_rev_uni_bi_blend.tgz

Exercise #1 - Diffusion Through Concentric Shells
-----------------------------------------------------

Exporting the Blend
=====================================================

Start Blender. Load the **sphere.blend** file in the **sphere** directory. You should see a set of concentric, transparent spherical shells. Several CellBlender properties have already been applied. We will now export these mdls and create a molecule release site centered within the shells. Under **CellBlender Project Settings**, select **Export CellBlender Project**.

Annotating the MDL
=====================================================

We will now modify the MDL, so that we count the molecules as they pass through the shells. Add the following variables at the beginning of your blend::

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

    PARTITION_X = [[-0.501 TO 0.501 STEP 0.04]]
    PARTITION_Y = [[-0.501 TO 0.501 STEP 0.04]]
    PARTITION_Z = [[-0.501 TO 0.501 STEP 0.04]]

After the DEFINE_MOLECULES section, add the following::

    DEFINE_SURFACE_CLASS transp {
        TRANSPARENT = vol1
    }

Before the **INSTANTIATE** sections, add this::

    MODIFY_SURFACE_REGIONS {
            Sphere_1[all] {
                    SURFACE_CLASS = transp
            }
            Sphere_2[all] {
                    SURFACE_CLASS = transp
            }
            Sphere_3[all] {
                    SURFACE_CLASS = transp
            }
            Sphere_4[all] {
                    SURFACE_CLASS = transp
            }
            Sphere_5[all] {
                    SURFACE_CLASS = transp
            }
            Sphere_6[all] {
                    SURFACE_CLASS = transp
            }
            Sphere_7[all] {
                    SURFACE_CLASS = transp
            }
            Sphere_8[all] {
                    SURFACE_CLASS = transp
            }
            Sphere_9[all] {
                    SURFACE_CLASS = transp
            }
    }

Next, create a file called **sphere.rxn_output.mdl** and enter the following text into it::

    sprintf(seed,"%03g", SEED)

    REACTION_DATA_OUTPUT {
        OUTPUT_BUFFER_SIZE = 200
        STEP = time_step*1
        {COUNT [A, World.Sphere_1]} => "./react_data/"&seed&"_inner_sphere.dat"
        {COUNT [A, World.Sphere_2] - COUNT [A, World.Sphere_1]} => "./react_data/shell_1."&seed&".dat"
        {COUNT [A, World.Sphere_3] - COUNT [A, World.Sphere_2]} => "./react_data/shell_2."&seed&".dat"
        {COUNT [A, World.Sphere_4] - COUNT [A, World.Sphere_3]} => "./react_data/shell_3."&seed&".dat"
        {COUNT [A, World.Sphere_5] - COUNT [A, World.Sphere_4]} => "./react_data/shell_4."&seed&".dat"
        {COUNT [A, World.Sphere_6] - COUNT [A, World.Sphere_5]} => "./react_data/shell_5."&seed&".dat"
        {COUNT [A, World.Sphere_7] - COUNT [A, World.Sphere_6]} => "./react_data/shell_6."&seed&".dat"
        {COUNT [A, World.Sphere_8] - COUNT [A, World.Sphere_7]} => "./react_data/shell_7."&seed&".dat"
        {COUNT [A, World.Sphere_9] - COUNT [A, World.Sphere_8]} => "./react_data/shell_8."&seed&".dat"
        {COUNT [A, World.Sphere_1]/vol_1} => "./react_data/conc_inner_sphere."&seed&"..dat"
        {(COUNT [A, World.Sphere_2] - COUNT [A, World.Sphere_1])/shell_vol_1} => "./react_data/conc_shell_1.dat"
        {(COUNT [A, World.Sphere_3] - COUNT [A, World.Sphere_2])/shell_vol_2} => "./react_data/conc_shell_2.dat"
        {(COUNT [A, World.Sphere_4] - COUNT [A, World.Sphere_3])/shell_vol_3} => "./react_data/conc_shell_3.dat"
        {(COUNT [A, World.Sphere_5] - COUNT [A, World.Sphere_4])/shell_vol_4} => "./react_data/conc_shell_4.dat"
        {(COUNT [A, World.Sphere_6] - COUNT [A, World.Sphere_5])/shell_vol_5} => "./react_data/conc_shell_5.dat"
        {(COUNT [A, World.Sphere_7] - COUNT [A, World.Sphere_6])/shell_vol_6} => "./react_data/conc_shell_6.dat"
        {(COUNT [A, World.Sphere_8] - COUNT [A, World.Sphere_7])/shell_vol_7} => "./react_data/conc_shell_7.dat"
        {(COUNT [A, World.Sphere_9] - COUNT [A, World.Sphere_8])/shell_vol_8} => "./react_data/conc_shell_8.dat"
    }

Lastly, create a file called **sphere.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
        MODE = ASCII
        FILENAME = "./viz_data/sphere"
        MOLECULES {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }   
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

    #need to finish this

Exercise #2 - Sampling Box
-----------------------------------------------------

Start Blender. Load the **sampling_box.blend** file in the **sampling_box** directory. You should see two boxes, one nested very closely inside of another. Several CellBlender properties have already been applied. We will now export these mdls and make a few small modifications. Under **CellBlender Project Settings**, select **Export CellBlender Project**.

Open the mdl, and paste the following text after the **DEFINE_MOLECULES** sections::

    DEFINE_SURFACE_CLASS transp {
       TRANSPARENT = vol1
    }

Before the **INSTANTIATE** section, add the following text::

    MODIFY_SURFACE_REGIONS {
            sampling_box[all] {
                    SURFACE_CLASS = transp
            }
    }

Create a file called **mean_and_var.py** and copy the following text into it::

    #!/usr/bin/env python

    #need to finish this

Run the file by entering the following command::

    python mean_and_var.py

This script will give you the mean and variance for the number of molecules in each box. Decrease the size of the inner box relative to the outer box and rerun the simulation. Do this repeatedly and note how the mean and variance values change. 

Exercise #3 - Irreverisble Unimolecular Reaction
-----------------------------------------------------

Steady State 
=====================================================
Start Blender. Load the **irrev_uni_steady_state.blend** file in the **irrev_uni_steady_state** directory.

We will now simulate an irreversible unimolecular reaction A :math:`\rightarrow` B with rate constant k1. Molecules of A are initially distributed at random within a reflective box. The simulation is run under steady state conditions. How? Predict the expected reaction rate. Run the simulation and plot the reaction data results for the number and concentration of B molecules as a function of time. What is the expected form of these results? Fit your results for the production of B and compare the obtained reaction rate to the expected value. Increase the initial concentration of A, rerun the simulation and again fit the results.

Non-Steady State 
=====================================================
Start Blender. Load the **irrev_uni_nonsteady_state.blend** file in the **irrev_uni_nonsteady_state** directory.

Next we will simulate the irreversible reaction A :math:`\rightarrow` B under non-steady-state conditions. Run the simulation and plot the reaction data results for the number and concentration of A and B molecules as a function of time. What is the expected form of these results? What is the time of an e-fold reduction of A? Fit your results for the decay of A and compare the obtained value of k1 to the input value.

Exercise #4 - Reverisble Unimolecular Reaction
-----------------------------------------------------

Non-Equilibrium 
=====================================================
Start Blender. Load the **rev_uni_nonequil.blend** file in the **rev_uni_nonequil** directory.

Here we simulate the reversible reaction A :math:`\leftrightarrow` B with rate constants k1 and k2 starting from non-equilibrium initial conditions (only A present at time 0). Run the simulation and plot the results for A and B. Run an XPPAUT simulation using the same reaction and parameter values. Export the results for A and B and plot together with the results from the MCell simulation. Fit the MCell results for production of B. What is the value of the fitted parameter, and what is its relationship to the values of k1 and k2?

Equilibrium 
=====================================================
Start Blender. Load the **rev_uni_equil.blend** file in the **rev_uni_equil** directory.

Now we simulate the reversible reaction A :math:`\leftrightarrow` B starting from equilibrium conditions, i.e., under conditions where the average fractional amounts of A and B will remain constant. How is this done? Use the statistics utility program to obtain the variance for the number of B molecules. Rerun the simulation while varying the fractional amounts of A and B. In each case determine the variance for B, and plot the resulting values as a function of fractional amount of B. What is the form of the resulting curve?

Exercise #5 - Irreverisble Bimolecular Reaction
-----------------------------------------------------

Steady State 
=====================================================
Start Blender. Load the **irrev_uni_steadystate.blend** file in the **irrev_uni_steadystate** directory.

Simulate an irreversible bimolecular reaction A + R :math:`\rightarrow` AR with rate constant k1. Molecules of A and R are initially distributed at random within a reflective box. The simulation is run under steady state conditions. How? Predict the expected reaction rate. Run the simulation and plot the reaction data results for the number and concentration of AR molecules as a function of time. What is the expected form of these results? Fit your results for the production of AR and compare the obtained reaction rate to the expected value. Increase the initial concentration of A and/or R, rerun the simulation and again fit the results. How does the obtained rate now compare to the expected rate?

Non-Steady State 
=====================================================
Start Blender. Load the **irrev_uni_nonsteadystate.blend** file in the **irrev_uni_nonsteadystate** directory.

Simulate the irreversible reaction A + R :math:`\rightarrow` AR under non-steady-state conditions. Run the simulation and plot the reaction data results for the number and concentration of A, R, and AR molecules as a function of time.

Exercise #6 - Reverisble Bimolecular Reaction
-----------------------------------------------------

Non-Equilibrium 
=====================================================
Start Blender. Load the **rev_bimol_nonequil.blend** file in the **rev_bimol_nonequil** directory.

Simulate the reversible bimolecular reaction A + R :math:`\leftrightarrow` AR with rate constants k1 and k2 starting from non-equilibrium initial conditions (only A and R present at time 0). Run the simulation and plot the results for A, R, and AR. Run an XPPAUT simulation using the same reaction and parameter values. Export the results and plot together with the results from the MCell simulation. Fit the MCell results for production of AR. What is the value of the fitted parameter?

Equilibrium 
=====================================================
Start Blender. Load the **rev_bimol_equil.blend** file in the **rev_bimol_equil** directory.

Simulate the reversible reaction A + R :math:`\leftrightarrow` AR starting from equilibrium conditions, i.e., under conditions where the average fractional amounts of A, R, and AR will remain constant. How is this done? Use the statistics utility program to obtain the variance for the number of AR molecules. Rerun the simulation while varying the fractional amounts of A, R, and AR. In each case determine the variance for AR, and plot the resulting values as a function of fractional amount of AR. What is the form of the resulting curve?
