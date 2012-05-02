*********************************************
Test
*********************************************

**Exercise #1 - spherical_shells:**

In this exercise we use a set of concentric, transparent spherical shells and release molecules from a point source centered within the shells.  We count the molecules as they pass through the shells.  Previously we verified the agreement between the simulation results and the solution of Fick's 2nd Law for a point source and radial symmetry.  Now we will examine the noise properties of the counted molecules as they pass through the shells.

Use the makeMCellscript utility to run a set of simulations using different random number seeds.  Use the analyzeMCelldata utility to create summary data files for all of the concentric shells.  Graph the summary data and in particular plot the ratio of variance to the mean for the number of molecules in each shell.  Describe the results and what they indicate.

**Exercise #2 - sampling_cube:**

In this simulation a reflective box is created and filled with a specified concentration of diffusing particles in random locations.  A transparent box is placed inside the reflective box.  Note the relative volumes of the two boxes and run the simulation.  Use the statistics utility program on each of the reaction data files to obtain the mean and variance for the number of molecules in each box.  Decrease the size of the inner box relative to the outer box and rerun the simulation.  Do this repeatedly and note how the mean and variance values change.  What happens to the ratio of mean to variance as the volume of the inner box decreases?  Why? 

**Exercise #3 - irrev_unimol:**

steady_state - We now simulate an irreversible unimolecular reaction A :math:`\rightarrow` B with rate constant k1.  Molecules of A are initially distributed at random within a reflective box.  The simulation is run under steady state conditions. How?  Predict the expected reaction rate.  Run the simulation and plot the reaction data results for the number and concentration of B molecules as a function of time.  What is the expected form of these results?  Fit your results for the production of B and compare the obtained reaction rate to the expected value.  Increase the initial concentration of A, rerun the simulation and again fit the results.  How does the obtained rate now compare to the expected rate?

non_steady_state - Next simulate the irreversible reaction A :math:`\rightarrow` B under non-steady-state conditions.  Run the simulation and plot the reaction data results for the number and concentration of A and B molecules as a function of time.  What is the expected form of these results?  What is the time of an e-fold reduction of A?    Fit your results for the decay of A and compare the obtained value of k1 to the input value.  Run an XPPAUT simulation using the same reaction and parameter values.  Export the results for the decay of A and plot together with the results from the MCell simulation.

**Exercise #4 - rev_unimol:**

non-equilibrium - Here we simulate the reversible reaction A :math:`\leftrightarrow` B with rate constants k1 and k2 starting from non-equilibrium initial conditions (only A present at time 0).  Run the simulation and plot the results for A and B.  Run an XPPAUT simulation using the same reaction and parameter values. Export the results for A and B and plot together with the results from the MCell simulation.  Fit the MCell results for production of B.  What is the value of the fitted parameter, and what is its relationship to the values of k1 and k2?

equilibrium - Now we simulate the reversible reaction A :math:`\leftrightarrow` B starting from equilibrium conditions, i.e., under conditions where the average fractional amounts of A and B will remain constant.  How is this done?  Use the statistics utility program to obtain the variance for the number of B molecules.  Rerun the simulation while varying the fractional amounts of A and B.  In each case determine the variance for B, and plot the resulting values as a function of fractional amount of B.  What is the form of the resulting curve?

**Exercise #5 - irrev_bimol:**

steady_state - Simulate an irreversible bimolecular reaction A + R :math:`\rightarrow` AR with rate constant k1.  Molecules of A and R are initially distributed at random within a reflective box.  The simulation is run under steady state conditions.  How?  Predict the expected reaction rate.  Run the simulation and plot the reaction data results for the number and concentration of AR molecules as a function of time.  What is the expected form of these results? Fit your results for the production of AR and compare the obtained reaction rate to the expected value.  Increase the initial concentration of A and/or R, rerun the simulation and again fit the results.  How does the obtained rate now compare to the expected rate?

non_steady_state - Simulate the irreversible reaction A + R :math:`\rightarrow` AR under non-steady-state conditions.  Run the simulation and plot the reaction data results for the number and concentration of A, R, and AR molecules as a function of time.  Run an XPPAUT simulation using the same reaction and parameter values.  Export the results and plot together with the results from the MCell simulation.

**Exercise #6 - rev_bimol:**

non-equilibrium - Simulate the reversible bimolecular reaction A + R :math:`\leftrightarrow` AR with rate constants k1 and k2 starting from non-equilibrium initial conditions (only A and R present at time 0).  Run the simulation and plot the results for A, R, and AR.  Run an XPPAUT simulation using the same reaction and parameter values.  Export the results and plot together with the results from the MCell simulation.  Fit the MCell results for production of AR.  What is the value of the fitted parameter?

equilibrium - Simulate the reversible reaction A + R :math:`\leftrightarrow` AR starting from equilibrium conditions, i.e., under conditions where the average fractional amounts of A, R, and AR will remain constant.  How is this done?  Use the statistics utility program to obtain the variance for the number of AR molecules.  Rerun the simulation while varying the fractional amounts of A, R, and AR.  In each case determine the variance for AR, and plot the resulting values as a function of fractional amount of AR.  What is the form of the resulting curve?

**Bonus:**

Consider the plots of variance as a function of fractional occupancy in Exercises #4 and 6 under equilibrium conditions.  Explain the form of your results.  Could these results have been predicted?  If so, why and how?

