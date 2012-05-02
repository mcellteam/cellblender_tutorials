.. _fick:

*********************************************
Fick's 1st and 2nd Laws
*********************************************

Our goal in this tutorial is to evaluate Fick’s 1st and 2nd Laws using simulations of discrete diffusing particles. To do so, we design the simulation geometry and input conditions so that we obtain a concentration gradient and net flux along one dimension only. We will compare the simulation results to our expectations based on the expressions for Fick’s Laws, in particular Fick’s 2nd Law:

:math:`\frac{dc}{dt}=D\frac{d^2c}{dx^2}=D\frac{d}{dx}(\frac{dc}{dx})`

where D is the diffusion coefficient used for the particles in the simulation. We begin by designing the 3-D geometry as illustrated below:

**Question #1:**

Using the above geometry, we wish to introduce diffusing particles such that:

#. There will be a concentration gradient along the x-axis only.
#. After some elapsed time, the system will reach a steady state with an unchanging concentration gradient along the x-axis (e.g., a 10-fold difference along the length of the cylinder).

How can we do so? Hint: consider using MCell’s concentration clamp command. Set up your simulation and then visualize it with DReAMM to make sure your conditions are correct.

**Questions #2 – 5:**

As the concentration gradient is evolving along x, we wish to determine the rate of change in concentration (dC/dt) at each time point for the central sampling volume composed of the two subvolumes numbered 20 and 21. To see this clearly, you will probably want to run a series of simulations using different random number seeds, so you can average your results. You can do this using the provided psc-dx tools (makeMCellscript, analyzeMCelldata) to set up your simulations and analyze your output. Along with the data you’ll need for Questions 2 – 4 below, make sure that you output counts for molecules in subvolumes 1 and 40 (Question #5). Using MCell’s reaction data output, determination of the time course of dC/dt can be done in three ways.

**Question #2:**

The most direct method is simply to count the number of molecules in subvolumes 20 and 21 at each timestep, convert the sum to concentration, export the concentration values for each timestep, and then differentiate to obtain the time course of ∆C/∆t ≈ dC/dt. Do so using MCell’s COUNT statements, the combined volume of the sampling subvolumes, and xmgrace to do the differentiation and smoothing.

**Question #3:**

The next method is based on determination of the net fluxes into and out of the combined subvolumes 20 and 21. Again using MCell’s COUNT statements (Hint: specify forward and backward crossings), determine the net flux into the space across plane 19, as well as the net flux out of the space across plane 21. Use these results to compute the final net number of molecules in subvolumes 20 and 21 at each timestep, convert to concentration, and then output the result. Again use xmgrace to differentiate and smooth, and compare your result to what you obtained for Question #1.

**Question #4:**

Now we wish to calculate dC/dt based on Fick’s 2nd Law. For this we need to estimate the value of d2C/dx2 across the sampling volume, i.e., across subvolumes 20 and 21. Hence, you will need to determine dC/dx at plane 19, as well as dC/dx at plane 21, and then find the difference to obtain d2C/dx2. To do this you will need to determine the concentration in subvolumes 19 and 22, as well as in subvolumes 20 and 21. Once you have calculated d2C/dx2 using COUNT statements, you can multiply by D, output the result, smooth in xmgrace, and compare to the results from Questions 2 and 3. Which final result do you expect to show the most noise? Why?

**Question #5:**

Finally, plot the ratio of variance (from the analysis utility program) to mean number of molecules for subvolumes 1, 20, 21, and 40. What do you observe and why?
