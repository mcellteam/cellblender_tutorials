.. _fick:

*********************************************
Fick's 1st and 2nd Laws
*********************************************

Our goal in this tutorial is to evaluate Fick’s 1st and 2nd Laws using 
simulations of discrete diffusing particles. To do so, we design the 
simulation geometry and input conditions so that we obtain a concentration 
gradient and net flux along one dimension only. We will compare the 
simulation results to our expectations based on the expressions for Fick’s 
Laws, in particular Fick’s 2nd Law:

:math:`\frac{dc}{dt}=D\frac{d^2c}{dx^2}=D\frac{d}{dx}(\frac{dc}{dx})`

where D is the diffusion coefficient used for the particles in the simulation.
We begin by designing the 3-D geometry as illustrated below:

Using the above geometry, we wish to introduce diffusing particles such that:

#. There will be a concentration gradient along the x-axis only.
#. After some elapsed time, the system will reach a steady state with an 
   unchanging concentration gradient along the x-axis (e.g., a 10-fold 
   difference along the length of the cylinder).

How can we do this with MCell? Hint: Consider the concentration clamp
command introduced previously. 

But first let's create the mesh for the system.

Creating the Mesh
---------------------------------------------

Either watch the video tutorial shown here or follow along with the text 
and illustrations that follow.

If you have watched the movie, please skip ahead to :ref:`fick_annotate`. 

Otherwise, begin by starting Blender. Create a cylinder by hitting 
**Shift-a**, and selecting **Mesh>Cylinder**. Hit **s**, **0.2**, and 
**Enter** to confirm. This will be the main cylinder through which the 
molecules diffuse. Create two surface regions, **Left_end** and 
**Right_end**. Enter **Edit Mode** by hitting **Tab**. Select the left end 
of the cylinder by hitting **b**, **left click and drag** around the left end of the cylinder. Select **Left_end** from the list of surface regions and 
select **Assign**. Do the same with the right end of the cylinder, except 
select and assign the **Right_end** surface region.

We now need to create a series of shorter sampling cylinders inside 
the long one. To do so, hit **Shift-a** and once again select 
**Mesh>Cylinder**. We will make these sampling cylinders slightly smaller
than the main cylinder to avoid coincident meshes: Hit **s**, **0.199**, 
and **Enter**. Next, hit **s**, **x**, **0.125**, and **Enter**. Now, we
will use Blenders (very useful) array modifier to replicate this sampling
cylinder 40 times. To do so, hit the **Object Modifiers** button, and from 
the **Add Modifier** drop-down box, select **Array**. Change **Count** to 
**40**. Change the third entry field under **Relative Offset** to **1.005**.

Finally, we will create a series of sampling planes in the form of of 
circular planes that lie between each of these cylinders. Create a cylinder 
by hitting **Shift-a**, and selecting **Mesh>Plane**. Hit **s**, **0.199**, 
and **Enter**. Again, we will replicate this plane by using an array modifier in exactly the same way as we did previously with the cylinders (same exact 
settings, i.e. a **Count** of **40** and a **Relative Offset** of **1.005**). 

Adding the Other Model Parameters
---------------------------------

First, add a single volume molecule called *vm* via CellBlenders 
**Define Molecules** tab. Then, in the **Define Surface Classes** tab
check *Include Surface Classes* and *Include Modify Surface Regions* since
we will use surface classes and modify surface regions; in the 
**Reaction Output Settings** tab check *Include Reaction Output* and
in **Visualization Output Settings** check *Include Viz Output*.
Next, we need to tell CellBlender to export our model geometry. To do
so hit the **+** sign in the **Model Objects** tab. You should remove the
*Camera* and *Lamp* objects which we don't need to export by selecting
them and the hitting the *-* sign.


Exporting the Project
---------------------

We will now export these mdls. Under **CellBlender Project Settings**, 
set the **Project Base Name** to *ficks_law*. Then hit
**Export CellBlender Project**, select a directory to save your
project to, and hit **Export MCell MDL**.

.. _fick_annotate: 

Annotating the MDL
---------------------------------------------

We will now edit several of the exported MDL files and also add new ones
to set up our simulations. First at the top of **ficks_law.main.mdl** add
the following MDL commands (you will have to change the existing 
**ITERATION** and **TIME_STEP** statements)::

    iterations = 1 
    dt = 1e-06
    ITERATIONS = iterations
    TIME_STEP = dt
    
    area = 1.256e-9   /* cross-sectional area of cylinder in square cm */
    dx = 10e-6        /* width of sampling volumes 20 plus 21, in cm */
    sampling_vol = area*dx*0.5 /* volume of one sampling subvolume, in cubic cm */
    dc = 5e-6 /* diffusion coefficient [cm^2/sec] */
    
    PARTITION_X = [[-0.1 TO 2.1 STEP .05]]
    PARTITION_Y = [[-0.3 TO 0.3 STEP .05]]
    PARTITION_Z = [[-0.3 TO 0.3 STEP .05]]

Make sure you understand what these variables and MDL commands mean. Can
you guess why we introduce separate *iterations* and *dt* variables? Also,
since we do not have any reactions in our model comment out the line
which includes the reactions (**ficks_law.reactions.mdl**).
Next, open the file **ficks_law.molecules.mdl** and change the diffusion 
coefficient of our *vm* molecule to *dc*::

    DEFINE_MOLECULES {
            vm {DIFFUSION_CONSTANT_3D = dc} 
    }


So far so good. Now we have to think about how we can establish a
concentration gradient between the left and right end of the big
cylinder. As already hinted above, we can use MCell's surface clamp
to clamp the left end of the cylinder at a certain value and make
sure molecules get absorbed at the right end (why?). To this end,
create the file **ficks_law.surface_classes.mdl** and enter a
**DEFINE_SURFACE_CLASSES** block. You will have to complete the
template given below yourself::

    DEFINE_SURFACE_CLASSES {
            transp {TRANSPARENT = vm }

            /* define a clamp which release molecule at a concentration
               of 1E-5 toward the inside of the cylinder */
           
            /* define a surface class absorptive to vm */
    }

Now, we need to do some serious modifications to our existing geometry.
Both the sampling cylinders and sampling planes need to be made 
transparent to *vm* (why?). Also, we need to install the surface clamp
at the left end of the big cylinder and make sure molecules are absorbed
at the right. Below is a template for a **MODIFY_SURFACE_REGIONS** block
that you will have to complete yourself. Create the file 
**ficks_law.mod_surf_regions.mdl** and start editing::

    MODIFY_SURFACE_REGIONS {
        
        /* Hint: You need to add statements here to add 
           a concentration clamps at the left end of the cylinder
           and absorb molecules at the right. Remember the surface
           regions you created for this purposes when setting up the
           mesh in Blender */

       C01[ALL] {
           SURFACE_CLASS = transp
       }
       
       C02[ALL] {
           SURFACE_CLASS = transp
       }

       /* add statements for the remaining cylinders */


       Plane01[ALL] {
           SURFACE_CLASS = transp
       }
       Plane02[ALL] {
           SURFACE_CLASS = transp
       }

       /* add statements for the remaining planes */
    }


Next, we will add a reaction data output block. Again, you will need
to add additional statements to output the data needed to work on the
problems below. Create a file **ficks_law.rxn_output.mdl** and enter::

    sprintf(seed,"%03g", SEED)

    REACTION_DATA_OUTPUT {
        STEP = 1*dt
        /* Hint: These are examples.  You will need to add more to determine dC/dt. */
        {COUNT[vm,Scene.Cylinder]}=>"./react_data/"&seed&"_vm_Cylinder.dat"
        {COUNT[vm,Scene.C01]}=>"./react_data/"&seed&"_vm_C01.dat"
        {COUNT[vm,Scene.Plane01,FRONT_CROSSINGS]}=>"./react_data/"&seed&"_vm_Plane01_front.dat"
        /* more statements needed */
    }


Finally, we add a visualization data block so we can check our simulation
visually in CellBlender. Luckily, nothing needs to be added here and
you are good to go! Create the file **ficks_law.viz_output.mdl** and
enter::

    VIZ_OUTPUT {
        MODE = ASCII
        FILENAME = "viz_data/ficksSecondLaw"
        MOLECULES {
          NAME_LIST {ALL_MOLECULES}
          ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }
    }




**Questions #2 - 5:**

As the concentration gradient is evolving along x, we wish to determine the rate of change in concentration (dC/dt) at each time point for the central sampling volume composed of the two subvolumes numbered 20 and 21. To see this clearly, you will probably want to run a series of simulations using different random number seeds, so you can average your results. You can do this using the provided psc-dx tools (makeMCellscript, analyzeMCelldata) to set up your simulations and analyze your output. Along with the data you’ll need for Questions 2 – 4 below, make sure that you output counts for molecules in subvolumes 1 and 40 (Question #5). Using MCell’s reaction data output, determination of the time course of dC/dt can be done in three ways.

**Question #2:**

The most direct method is simply to count the number of molecules in subvolumes 20 and 21 at each timestep, convert the sum to concentration, export the concentration values for each timestep, and then differentiate to obtain the time course of ∆C/∆t ≈ dC/dt. Do so using MCell’s COUNT statements, the combined volume of the sampling subvolumes, and xmgrace to do the differentiation and smoothing.

**Question #3:**

The next method is based on determination of the net fluxes into and out of the combined subvolumes 20 and 21. Again using MCell’s COUNT statements (Hint: specify forward and backward crossings), determine the net flux into the space across plane 19, as well as the net flux out of the space across plane 21. Use these results to compute the final net number of molecules in subvolumes 20 and 21 at each timestep, convert to concentration, and then output the result. Again use xmgrace to differentiate and smooth, and compare your result to what you obtained for Question #1.

**Question #4:**

Now we wish to calculate dC/dt based on Fick’s 2nd Law. For this we need to estimate the value of d2C/dx2 across the sampling volume, i.e., across subvolumes 20 and 21. Hence, you will need to determine dC/dx at plane 19, as well as dC/dx at plane 21, and then find the difference to obtain d2C/dx2. To do this you will need to determine the concentration in subvolumes 19 and 22, as well as in subvolumes 20 and 21. Once you have calculated d2C/dx2 using COUNT statements, you can multiply by D, output the result, smooth in xmgrace, and compare to the results from Questions 2 and 3. Which final result do you expect to show the most noise? Why?

**Question #5:**

Finally, plot the ratio of variance (from the analysis utility program) to mean number of molecules for subvolumes 1, 20, 21, and 40. What do you observe and why?
