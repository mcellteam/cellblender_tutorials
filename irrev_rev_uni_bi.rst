*****************************************************
(Ir)reversible Unimolecular and Bimolecular Reactions
*****************************************************

Download the blend files used for these tutorials here_. You will still 
have to export and modify the mdls created. Alternatively, you can download 
the completed `project files`_, which contains the blends and fully annotated
mdls. Whichever one you choose to use, extract the archive, which will create
a directory called **irrev_rev_uni_bi_blend** or **irrev_rev_uni_bi_complete**
.

.. _here: https://www.mcell.psc.edu/tutorials/mdl/main/irrev_rev_uni_bi_blend.tgz

.. _project files: https://www.mcell.psc.edu/tutorials/mdl/main/irrev_rev_uni_bi_blend.tgz

Diffusion Through Concentric Shells
=====================================================

In the previous exercise we had verified the agreement of our 
MCell simulations and the solution to Fick's 2nd law. Here, we will
further examine the noise properties of the counted molecules as they
diffuse through a series of **TRANSPARENT** concentric shells.


Exporting the Blend
-----------------------------------------------------

Start Blender. Load the **spherical_shells/spherical_shells.blend** file 
in the main project directory which contains the already prepared
model geometry. Normally, you would have to create the geometry yourself. 
You should see a set of concentric, transparent spherical shells. Several 
CellBlender properties have already been applied. We will now export this 
geometry as MDL and create a molecule release site in the center of the 
shells. Under **CellBlender Project Settings**, select 
**Export CellBlender Project**. Navigate to **spherical_shells** and 
select **Set Project Directory**. Set the **Project Base** to 
**spherical_shells**. Then hit **Export CellBlender Project**, navigate to 
same directory as before, and hit **Export MCell MDL**.  You have now
exported your project as MDL.


Annotating the MDL
-----------------------------------------------------

We will now add additional MDL commands to the files exported by CellBlender 
that is needed to count the molecules as they pass through the spherical
shells. Since in this case we would also like to output the molecular 
concentrations in addition to raw counts we first compute the volume 
(in cubic microns) of each shell. This, add the following variables at 
the beginning of your **spherical_shells.main.mdl**::

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


Since meshes (including our concentric shells) are by default reflective to
all diffusion molecules we need to make them transparent via a surface
class. Thus, create a file called **spherical_shells.surface_classes.mdl** 
with the following content::

    DEFINE_SURFACE_CLASS transp {
        TRANSPARENT = vol1
    }

Next, we use the **MODIFY_SURFACE_REGIONS** modifier to apply this surface
class to all concentric shells. This method allows you to modify surface
meshes without ever needing to touch the (often large) mesh files themselves.
Create a file called **spherical_shells.mod_surf_regions.mdl** with the following text::

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

Finally, we need to define a **REACTION_DATA_OUTPUT** block to measure the
molecular concentration in each shell. To do so, create a file called 
**spherical_shells.rxn_output.mdl** and enter the following text into it::

    sprintf(seed,"%03g", SEED)

    REACTION_DATA_OUTPUT {
        OUTPUT_BUFFER_SIZE = 200
        STEP = 1e-6
        {COUNT [vol1, World.Sphere_1]} => "./react_data/inner_sphere."&seed&".dat"
        {COUNT [vol1, World.Sphere_2] - COUNT [vol1, World.Sphere_1]} => "./react_data/shell_1."&seed&".dat"
        {COUNT [vol1, World.Sphere_3] - COUNT [vol1, World.Sphere_2]} => "./react_data/shell_2."&seed&".dat"
        {COUNT [vol1, World.Sphere_4] - COUNT [vol1, World.Sphere_3]} => "./react_data/shell_3."&seed&".dat"
        {COUNT [vol1, World.Sphere_5] - COUNT [vol1, World.Sphere_4]} => "./react_data/shell_4."&seed&".dat"
        {COUNT [vol1, World.Sphere_6] - COUNT [vol1, World.Sphere_5]} => "./react_data/shell_5."&seed&".dat"
        {COUNT [vol1, World.Sphere_7] - COUNT [vol1, World.Sphere_6]} => "./react_data/shell_6."&seed&".dat"
        {COUNT [vol1, World.Sphere_8] - COUNT [vol1, World.Sphere_7]} => "./react_data/shell_7."&seed&".dat"
        {COUNT [vol1, World.Sphere_9] - COUNT [vol1, World.Sphere_8]} => "./react_data/shell_8."&seed&".dat"
        {COUNT [vol1, World.Sphere_1]/vol_1} => "./react_data/conc_inner_sphere."&seed&".dat"
        {(COUNT [vol1, World.Sphere_2] - COUNT [vol1, World.Sphere_1])/shell_vol_1} => "./react_data/conc_shell_1."&seed&".dat"
        {(COUNT [vol1, World.Sphere_3] - COUNT [vol1, World.Sphere_2])/shell_vol_2} => "./react_data/conc_shell_2."&seed&".dat"
        {(COUNT [vol1, World.Sphere_4] - COUNT [vol1, World.Sphere_3])/shell_vol_3} => "./react_data/conc_shell_3."&seed&".dat"
        {(COUNT [vol1, World.Sphere_5] - COUNT [vol1, World.Sphere_4])/shell_vol_4} => "./react_data/conc_shell_4."&seed&".dat"
        {(COUNT [vol1, World.Sphere_6] - COUNT [vol1, World.Sphere_5])/shell_vol_5} => "./react_data/conc_shell_5."&seed&".dat"
        {(COUNT [vol1, World.Sphere_7] - COUNT [vol1, World.Sphere_6])/shell_vol_6} => "./react_data/conc_shell_6."&seed&".dat"
        {(COUNT [vol1, World.Sphere_8] - COUNT [vol1, World.Sphere_7])/shell_vol_7} => "./react_data/conc_shell_7."&seed&".dat"
        {(COUNT [vol1, World.Sphere_9] - COUNT [vol1, World.Sphere_8])/shell_vol_8} => "./react_data/conc_shell_8."&seed&".dat"
    }

Lastly, create a file called **spherical_shells.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
        MODE = ASCII
        FILENAME = "./viz_data/spherical_shells"
        MOLECULES {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }   
    }

Run the Simulation and Analyze the Results
-----------------------------------------------------

If you have done the :ref:`seed` section, then copy the file **run_seeds.py** and **avg_seeds.py** that was created in that section by typing the following commands::

    cp /home/user/mcell_tutorial/seed/run_seeds.py /home/user/irrev_rev_uni_bi/spherical_shells/
    cp /home/user/mcell_tutorial/seed/avg_seeds.py /home/user/irrev_rev_uni_bi/spherical_shells/

Otherwise, create both of the scripts listed in :ref:`seed` right now.

Run the first script by typing::

    python run_seeds.py

When prompted, enter::

    spherical_shells.main.mdl

After the simulation finishes running, enter this command::

    python avg_seeds.py

Now we need to plot the ratio of variance to the mean for the number of molecules in each shell. Create a file called **var_to_mean.py** and copy the following text into it::

    #!/usr/bin/env python

    #need to finish this

Sampling Box
=====================================================

In this example, volume molecules will diffuse around inside of two boxes, one nested very closely inside of the other. Afterwards, we will do some analysis on the results.

Exporting the Blend
-----------------------------------------------------

Start Blender. Load the **sampling_box/sampling_box.blend** file in the main project directory. You should see two boxes, one nested very closely inside of another. Several CellBlender properties have already been applied. We will now export these mdls and make a few small modifications. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to **sampling_boxes** and select **Set Project Directory**. Set the **Project Base** to **sampling_boxes**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

Annotating the MDL
-----------------------------------------------------

Add the following to the beginning of **sampling_box.main.mdl**::

    box_volume = 0.05 /* cubic microns, volume of the box used to contain the A molecules */
    sampling_box_volume = 0.99*box_volume
    side_length = box_volume^(1/3)
    half_length = side_length/2.0
    sampling_side_length = sampling_box_volume^(1/3)
    sampling_half_length = sampling_side_length/2.0

    PARTITION_X = [[-1.001*half_length TO 1.001*half_length STEP 0.04]]
    PARTITION_Y = [[-1.001*half_length TO 1.001*half_length STEP 0.04]]
    PARTITION_Z = [[-1.001*half_length TO 1.001*half_length STEP 0.04]]

Create a file called **sampling_box.surface_classes.mdl** and paste the following text into it::

    DEFINE_SURFACE_CLASS transp {
       TRANSPARENT = vol1
    }

Create a file called **sampling_box.mod_surf_regions.mdl** with the following text::

    MODIFY_SURFACE_REGIONS {
            sampling_box[all] {
                    SURFACE_CLASS = transp
            }
    }

Next, create a filed called **sampling_box.rxn_output.mdl** like this::

    REACTION_DATA_OUTPUT {
       OUTPUT_BUFFER_SIZE = 1000  
       STEP = 1e-6 
       {COUNT [vol1, WORLD]} => "./reaction_data/vol1.dat"
       {COUNT [vol1, Scene.sampling_box]} => "./reaction_data/vol1_sampled.dat"
    }

Lastly, create a file called **sampling_box.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
        MODE = ASCII
        FILENAME = "./viz_data/sampling_box"
        MOLECULES {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }   
    }

Run the Simulation and Analyze the Results
-----------------------------------------------------

Run the simulation by typing the following command::

    mcell main.geometry.mdl

Create a file called **mean_and_var.py** and copy the following text into it::

    #!/usr/bin/env python

    #need to finish this

Run the file by entering the following command::

    python mean_and_var.py

This script will give you the mean and variance for the number of molecules in each box. Decrease the size of the inner box relative to the outer box and rerun the simulation. Do this repeatedly and note how the mean and variance values change. 

Irreverisble Unimolecular Reaction
=====================================================

Steady State 
-----------------------------------------------------

We will now simulate an irreversible unimolecular reaction A :math:`\rightarrow` B with rate constant k1. Molecules of A are initially distributed at random within a reflective box. The simulation is run under steady state conditions. 

Start Blender. Load the **irrev_uni/steady_state/irrev_uni_steady.blend** file. Several CellBlender properties have already been applied. We will now export these mdls. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to **irrev_uni/steady_state** and select **Set Project Directory**. Set the **Project Base** to **irrev_uni_steady**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

Add the following text to the beginning of **irrev_uni_steady.main.mdl**::

    box_volume = 0.05 /* cubic microns, volume of the box used to contain the A and B molecules */
    box_volume_liters = box_volume * 1e-15 /* convert from cubic microns to liters */
    Na = 6.022e23 /* Avogadro's number, molecules per mole */

    side_length = box_volume^(1/3)
    half_length = side_length/2.0
    partition = half_length*0.999

    PARTITION_X = [-partition, partition]
    PARTITION_Y = [-partition, partition]
    PARTITION_Z = [-partition, partition]

Next create a file callled **irrev_uni_steady.rxn_output.mdl** and copy this text into it::

    REACTION_DATA_OUTPUT {
       OUTPUT_BUFFER_SIZE = 1000  
       STEP = 1e-5 
       {COUNT [A, WORLD]} => "./reaction_data/A.dat"
       {COUNT [B, WORLD]} => "./reaction_data/B.dat"
       {COUNT [B, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_B.dat"
    }

Lastly, create a file called **irrev_uni_steady.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
        MODE = ASCII
        FILENAME = "./viz_data/irrev_uni_steady"
        MOLECULES {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }   
    }

Run the simulation by typing the following command::

    mcell irrev_uni_steady.main.mdl

Next, plot the reaction data results for the number and concentration of B molecules as a function of time. Fit your results for the production of B and compare the obtained reaction rate to the expected value. Increase the initial concentration of A, rerun the simulation and again fit the results.

Non-Steady State 
-----------------------------------------------------

Next we will simulate the irreversible reaction A :math:`\rightarrow` B under non-steady-state conditions. 

Start Blender. Load the **irrev_uni_nonsteady_state.blend** file in the **irrev_uni_nonsteady_state** directory. Several CellBlender properties have already been applied. We will now export these mdls. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to **irrev_uni/nonsteady_state** and select **Set Project Directory**. Set the **Project Base** to **irrev_uni_nonsteady**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.


Open **irrev_uni_nonsteady.main.mdl** and add in the following text at the top of the mdl::

    box_volume = 0.05 /* cubic microns, volume of the box used to contain the A and B molecules */
    box_volume_liters = box_volume * 1e-15 /* convert from cubic microns to liters */
    Na = 6.022e23 /* Avogadro's number, molecules per mole */

    side_length = box_volume^(1/3)
    half_length = side_length/2.0

    partition = half_length*0.999

    PARTITION_X = [-partition, partition]
    PARTITION_Y = [-partition, partition]
    PARTITION_Z = [-partition, partition]

Next create a file callled **irrev_uni_nonsteady.rxn_output.mdl** and copy this text into it::

    REACTION_DATA_OUTPUT {
       OUTPUT_BUFFER_SIZE = 1000  
       STEP = 1e-5
       {COUNT [A, WORLD]} => "./reaction_data/A.dat"
       {COUNT [A, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_A.dat"
       {COUNT [B, WORLD]} => "./reaction_data/B.dat"
       {COUNT [B, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_B.dat"
    }

Lastly, create a file called **irrev_uni_nonsteady.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
        MODE = ASCII
        FILENAME = "./viz_data/main"
        MOLECULES {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }   
    }

Run the simulation by typing the following command::

    mcell irrev_uni_steady.main.mdl

Plot the reaction data results for the number and concentration of A and B molecules as a function of time. Fit your results for the decay of A and compare the obtained value of k1 to the input value.

Reverisble Unimolecular Reaction
=====================================================

Non-Equilibrium 
-----------------------------------------------------

Here we will simulate the reversible reaction A :math:`\leftrightarrow` B with rate constants k1 and k2 starting from non-equilibrium initial conditions (only A present at time 0).

Start Blender. Load the **rev_uni_nonequil.blend** file in the **rev_uni/nonequil** directory. Several CellBlender properties have already been applied. We will now export these mdls. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to **rev_uni/nonequil** and select **Set Project Directory**. Set the **Project Base** to **rev_uni_nonequil**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

Open **rev_uni_nonequil.main.mdl** and add in the following text at the top of the mdl::

    fractional_concentration_of_A = 0.1
    fractional_concentration_of_B = 1.0 - fractional_concentration_of_A
    total_concentration = 1e-5 /* moles per liter; summed concentrations of A and B */
    k1_plus_k2 = 100 /* per second, sum of rate constants for conversion of A to B and B to A */
    k1 = fractional_concentration_of_B * k1_plus_k2  /* per second, rate constant for conversion of A to B */
    k2 = k1_plus_k2 - k1 /* per second, rate constant for conversion of B to A */
    concentration_of_A = fractional_concentration_of_A * total_concentration /* moles per liter, concentration of molecule A in the box */
    concentration_of_B = total_concentration - concentration_of_A /* moles per liter, concentration of molecule A in the box */
    box_volume = 0.05 /* cubic microns, volume of the box used to contain the A and B molecules */
    box_volume_liters = box_volume * 1e-15 /* convert from cubic microns to liters */
    Na = 6.022e23 /* Avogadro's number, molecules per mole */
    side_length = box_volume^(1/3)
    half_length = side_length/2.0
    partition = half_length*0.999

    PARTITION_X = [-partition, partition]
    PARTITION_Y = [-partition, partition]
    PARTITION_Z = [-partition, partition]

Modify **rev_uni_nonequil.reactions.mdl** like this::

    DEFINE_REACTIONS {
       A -> B [k1]
       B -> A [k2]
    }

Now, create a file called **rev_uni_nonequil.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
       MODE = ASCII
       FILENAME = "./viz_data/rev_uni_nonequil"
       MOLECULES {
          NAME_LIST {ALL_MOLECULES}
          ITERATION_NUMBERS {ALL_DATA @ [[0 TO 100000 STEP 1000]]}
       }
    }

Next, create a file callled **rev_uni_nonequil.rxn_output.mdl** and copy this text into it::

    REACTION_DATA_OUTPUT {
       OUTPUT_BUFFER_SIZE = 1000  
       STEP = 1e-5
       {COUNT [A, WORLD]} => "./reaction_data/A.dat"
       {COUNT [A, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_A.dat"
       {COUNT [B, WORLD]} => "./reaction_data/B.dat"
       {COUNT [B, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_B.dat"
    }

Run the simulation by typing the following command::

    mcell rev_uni_nonequil.main.mdl

Plot the results from the simulation. Fit the MCell results for production of B. 

Equilibrium 
-----------------------------------------------------

Now we will simulate the reversible reaction A :math:`\leftrightarrow` B starting from equilibrium conditions, i.e., under conditions where the average fractional amounts of A and B will remain constant. 

Start Blender. Load the **rev_uni_equil.blend** file in the **rev_uni/equil** directory. Several CellBlender properties have already been applied. We will now export these mdls. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to **rev_uni/equil** and select **Set Project Directory**. Set the **Project Base** to **rev_uni_equil**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.


Open **rev_uni_equil.main.mdl** and add in the following text at the top of the mdl::

    fractional_concentration_of_A = 0.1
    fractional_concentration_of_B = 1.0 - fractional_concentration_of_A
    total_concentration = 1e-5 /* moles per liter; summed concentrations of A and B */
    k1_plus_k2 = 100 /* per second, sum of rate constants for conversion of A to B and B to A */
    k1 = fractional_concentration_of_B * k1_plus_k2  /* per second, rate constant for conversion of A to B */
    k2 = k1_plus_k2 - k1 /* per second, rate constant for conversion of B to A */
    concentration_of_A = fractional_concentration_of_A * total_concentration /* moles per liter, concentration of molecule A in the box */
    concentration_of_B = total_concentration - concentration_of_A /* moles per liter, concentration of molecule A in the box */
    box_volume = 0.05 /* cubic microns, volume of the box used to contain the A and B molecules */
    box_volume_liters = box_volume * 1e-15 /* convert from cubic microns to liters */
    Na = 6.022e23 /* Avogadro's number, molecules per mole */
    side_length = box_volume^(1/3)
    half_length = side_length/2.0
    partition = half_length*0.999

    PARTITION_X = [-partition, partition]
    PARTITION_Y = [-partition, partition]
    PARTITION_Z = [-partition, partition]

Now, create a file called **rev_uni_nonequil.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
       MODE = ASCII
       FILENAME = "./viz_data/rev_uni_nonequil"
       MOLECULES {
          NAME_LIST {ALL_MOLECULES}
          ITERATION_NUMBERS {ALL_DATA @ [[0 TO 100000 STEP 1000]]}
       }
    }

Next, create a file callled **rev_uni_nonequil.rxn_output.mdl** and copy this text into it::

    REACTION_DATA_OUTPUT {
       OUTPUT_BUFFER_SIZE = 1000  
       STEP = 1e-5
       {COUNT [A, WORLD]} => "./reaction_data/A.dat"
       {COUNT [A, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_A.dat"
       {COUNT [B, WORLD]} => "./reaction_data/B.dat"
       {COUNT [B, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_B.dat"
    }

Run the simulation by typing the following command::

    mcell rev_uni_equil.main.mdl

Use the statistics utility program to obtain the variance for the number of B molecules. Rerun the simulation while varying the fractional amounts of A and B. In each case determine the variance for B, and plot the resulting values as a function of fractional amount of B.

Irreverisble Bimolecular Reaction
=====================================================

Steady State 
-----------------------------------------------------

We will now simulate an irreversible bimolecular reaction A + R :math:`\rightarrow` AR with rate constant k1. Molecules of A and R are initially distributed at random within a reflective box. The simulation is run under steady state conditions.

Start Blender. Load the **irrev_bi_steady.blend** file in the **irrev_bi_steady** directory. Several CellBlender properties have already been applied. We will now export these mdls. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to **irrev_bi/steady** and select **Set Project Directory**. Set the **Project Base** to **irrev_bi_steady**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

Open **irrev_bi_steady.main.mdl** and add in the following text at the top of the mdl::
    
    box_volume = 0.05 /* cubic microns, volume of the box used to contain the A and B molecules */
    diffusion_coefficient = 1e-6 /* cm^2 per second, diffusion coefficient used for molecules of A and R */
    box_volume_liters = box_volume * 1e-15 /* convert from cubic microns to liters */
    Na = 6.022e23 /* Avogadro's number, molecules per mole */
    side_length = box_volume^(1/3)
    half_length = side_length/2.0
    partition = half_length*0.999

    PARTITION_X = [-partition, partition]
    PARTITION_Y = [-partition, partition]
    PARTITION_Z = [-partition, partition]

Now, create a file called **irrev_bi_steady.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
       MODE = ASCII
       FILENAME = "./viz_data/irrev_bi_steady"
       MOLECULES {
          NAME_LIST {ALL_MOLECULES}
          ITERATION_NUMBERS {ALL_DATA @ [[0 TO 5000 STEP 100]]}
       }
    }

Next, create a file callled **irrev_bi_steady.rxn_output.mdl** and copy this text into it::

    REACTION_DATA_OUTPUT {
       OUTPUT_BUFFER_SIZE = 1000  
       STEP = 1e-5
       {COUNT [A, WORLD]} => "./reaction_data/A.dat"
       {COUNT [A, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_A.dat"
       {COUNT [R, WORLD]} => "./reaction_data/R.dat"
       {COUNT [R, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_R.dat"
       {COUNT [AR, WORLD]} => "./reaction_data/AR.dat"
       {COUNT [AR, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_AR.dat"
    }

Run the simulation by typing the following command::

    mcell irrev_bi_steady.main.mdl

Plot the reaction data results for the number and concentration of AR molecules as a function of time. Fit your results for the production of AR and compare the obtained reaction rate to the expected value. Increase the initial concentration of A and/or R, rerun the simulation and again fit the results. How does the obtained rate now compare to the expected rate?

Non-Steady State 
-----------------------------------------------------

Now, we'll simulate the irreversible reaction A + R :math:`\rightarrow` AR under non-steady-state conditions.

Start Blender. Load the **irrev_bi_nonsteady.blend** file in the **irrev_bi_nonsteady** directory. Several CellBlender properties have already been applied. We will now export these mdls. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to **irrev_bi/nonsteady** and select **Set Project Directory**. Set the **Project Base** to **irrev_bi_nonsteady**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

Open **irrev_bi_nonsteady.main.mdl** and add in the following text at the top of the mdl::
    
    box_volume = 0.05 /* cubic microns, volume of the box used to contain the A and B molecules */
    diffusion_coefficient = 1e-6 /* cm^2 per second, diffusion coefficient used for molecules of A and R */
    box_volume_liters = box_volume * 1e-15 /* convert from cubic microns to liters */
    Na = 6.022e23 /* Avogadro's number, molecules per mole */
    side_length = box_volume^(1/3)
    half_length = side_length/2.0
    partition = half_length*0.999

    PARTITION_X = [-partition, partition]
    PARTITION_Y = [-partition, partition]
    PARTITION_Z = [-partition, partition]

Now, create a file called **irrev_bi_nonsteady.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
       MODE = ASCII
       FILENAME = "./viz_data/irrev_bi_nonsteady"
       MOLECULES {
          NAME_LIST {ALL_MOLECULES}
          ITERATION_NUMBERS {ALL_DATA @ [[0 TO 5000 STEP 100]]}
       }
    }

Next, create a file callled **irrev_bi_nonsteady.rxn_output.mdl** and copy this text into it::

    REACTION_DATA_OUTPUT {
       OUTPUT_BUFFER_SIZE = 1000  
       STEP = 1e-5
       {COUNT [A, WORLD]} => "./reaction_data/A.dat"
       {COUNT [A, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_A.dat"
       {COUNT [R, WORLD]} => "./reaction_data/R.dat"
       {COUNT [R, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_R.dat"
       {COUNT [AR, WORLD]} => "./reaction_data/AR.dat"
       {COUNT [AR, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_AR.dat"
    }

Run the simulation by typing the following command::

    mcell irrev_bi_nonsteady.main.mdl

Plot the reaction data results for the number and concentration of A, R, and AR molecules as a function of time.

Reverisble Bimolecular Reaction
=====================================================

Non-Equilibrium 
-----------------------------------------------------

Next, we will simulate the reversible bimolecular reaction A + R :math:`\leftrightarrow` AR with rate constants k1 and k2 starting from non-equilibrium initial conditions (only A and R present at time 0).

Start Blender. Load the **rev_bimol_nonequil.blend** file in the **rev_bimol_nonequil** directory. Several CellBlender properties have already been applied. We will now export these mdls. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to **rev_bi/nonequil** and select **Set Project Directory**. Set the **Project Base** to **rev_bi_nonequil**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

Open **rev_bi_nonequil.main.mdl** and add in the following text at the top of the mdl::
    box_volume = 0.05 /* cubic microns, volume of the box used to contain the A and R molecules */
    box_volume_liters = box_volume * 1e-15 /* convert from cubic microns to liters */
    Na = 6.022e23 /* Avogadro's number, molecules per mole */
    side_length = box_volume^(1/3)
    half_length = side_length/2.0
    partition = half_length*0.999

    PARTITION_X = [-partition, partition]
    PARTITION_Y = [-partition, partition]
    PARTITION_Z = [-partition, partition]
  
Now, create a file called **rev_bi_nonequil.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
       MODE = ASCII
       FILENAME = "./viz_data/irrev_bi_nonequil"
       MOLECULES {
          NAME_LIST {ALL_MOLECULES}
          ITERATION_NUMBERS {ALL_DATA @ [[0 TO 5000 STEP 100]]}
       }
    }

Next, create a file callled **rev_bi_nonequil.rxn_output.mdl** and copy this text into it::

    REACTION_DATA_OUTPUT {
       OUTPUT_BUFFER_SIZE = 1000  
       STEP = 1e-5
       {COUNT [A, WORLD]} => "./reaction_data/A.dat"
       {COUNT [A, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_A.dat"
       {COUNT [R, WORLD]} => "./reaction_data/R.dat"
       {COUNT [R, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_R.dat"
       {COUNT [AR, WORLD]} => "./reaction_data/AR.dat"
       {COUNT [AR, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_AR.dat"
    }

Run the simulation by typing the following command::

    mcell rev_bi_nonequil.main.mdl

Plot the results for A, R, and AR. Fit the MCell results for production of AR.

Equilibrium 
-----------------------------------------------------

We will simulate the reversible reaction A + R :math:`\leftrightarrow` AR starting from equilibrium conditions, i.e., under conditions where the average fractional amounts of A, R, and AR will remain constant. 

Start Blender. Load the **rev_bimol_equil.blend** file in the **rev_bimol_equil** directory. Several CellBlender properties have already been applied. We will now export these mdls. Under **CellBlender Project Settings**, select **Export CellBlender Project**. Navigate to **rev_bi/nonequil** and select **Set Project Directory**. Set the **Project Base** to **rev_bi_nonequil**. Then hit **Export CellBlender Project**, navigate to same directory as before, and hit **Export MCell MDL**.

Open **rev_bi_equil.main.mdl** and add in the following text at the top of the mdl::

    k1 = 1e8 /* liters per mole per second, rate constant for binding of A to R */
    k2 = 1e4 /* per second, rate constant for unbinding */
    KD = k2/k1
    total_concentration = 1e-5 /* moles per liter; summed concentrations of R and AR */
    concentration_of_A = 9.0 * KD /* moles per liter, concentration of molecule A in the box */
    fractional_concentration_of_AR = concentration_of_A/(concentration_of_A + KD) 
    fractional_concentration_of_R = 1.0 - fractional_concentration_of_AR
    concentration_of_AR = total_concentration * fractional_concentration_of_AR /* moles per liter, concentration of molecule R in the box */
    concentration_of_R = total_concentration * fractional_concentration_of_R /* moles per liter, concentration of molecule R in the box */
    box_volume = 0.05 /* cubic microns, volume of the box used to contain the A and R molecules */
    diffusion_coefficient = 1e-6 /* cm^2 per second, diffusion coefficient used for molecules of A and R */
    box_volume_liters = box_volume * 1e-15 /* convert from cubic microns to liters */
    Na = 6.022e23 /* Avogadro's number, molecules per mole */
    side_length = box_volume^(1/3)
    half_length = side_length/2.0
    partition = half_length*0.999
    step = 0.055

    PARTITION_X = [[-partition TO partition STEP step]]
    PARTITION_Y = [[-partition TO partition STEP step]]
    PARTITION_Z = [[-partition TO partition STEP step]]

Modify the **INSTANTIATE** section, so that it looks like this::

    INSTANTIATE Scene OBJECT {
       box OBJECT box {}
       A_release RELEASE_SITE {
          SHAPE = Scene.box[all]
          MOLECULE = A 
          CONCENTRATION = concentration_of_A
       }   
       R_release RELEASE_SITE {
          SHAPE = Scene.box[all]
          MOLECULE = R 
          CONCENTRATION = concentration_of_R
       }   
       AR_release RELEASE_SITE {
          SHAPE = Scene.box[all]
          MOLECULE = AR
          CONCENTRATION = concentration_of_AR
       }   
    }


Now, create a file called **rev_bi_equil.viz_output.mdl** with the following text::

    VIZ_OUTPUT {
       MODE = ASCII
       FILENAME = "./viz_data/irrev_bi_nonsteady"
       MOLECULES {
          NAME_LIST {ALL_MOLECULES}
          ITERATION_NUMBERS {ALL_DATA @ [[0 TO 20000 STEP 100]]}
       }
    }

Next, create a file callled **rev_bi_equil.rxn_output.mdl** and copy this text into it::

    REACTION_DATA_OUTPUT {
       OUTPUT_BUFFER_SIZE = 1000  
       STEP = 1e-5
       {COUNT [A, WORLD]} => "./reaction_data/A.dat"
       {COUNT [A, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_A.dat"
       {COUNT [R, WORLD]} => "./reaction_data/R.dat"
       {COUNT [R, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_R.dat"
       {COUNT [AR, WORLD]} => "./reaction_data/AR.dat"
       {COUNT [AR, WORLD]/Na/box_volume_liters} => "./reaction_data/conc_AR.dat"
    }

Run the simulation by typing the following command::

    mcell rev_bi_nonequil.main.mdl

Use the statistics utility program to obtain the variance for the number of AR molecules. Rerun the simulation while varying the fractional amounts of A, R, and AR. In each case determine the variance for AR, and plot the resulting values as a function of fractional amount of AR. 
