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

.. _fick_create_mesh: 

Creating the Mesh
---------------------------------------------

Either download the `blend file`_ or follow along with the instructions that follow.

.. _blend file: http://www.mcell.org/workshop2012/tutorials/blends/ficks_law/ficks_law.blend

Begin by starting Blender. Hit **x** and click **Delete** to delete the default Cube. Then, create a cylinder by hitting **Shift-a**, and selecting **Mesh>Cylinder**. Hit **s**, **Shift-z**, **0.2**, and **Enter** to confirm. Hit **r**, **x**, **90**, and **Enter** to rotate it 90 degrees around the x-axis. This will be the main cylinder through which the molecules diffuse. 

Create two surface regions, **Left_end** and **Right_end**. 

Then, enter **Edit Mode** by hitting **Tab**. Hit **Ctrl-t** to triangulate the mesh. Next, select the left end of the cylinder by hitting **b**, **left click and drag** around the left end of the cylinder. Select **Left_end** from the list of surface regions and select **Assign**. Do the same with the right end of the cylinder, except select and assign the **Right_end** surface region. Switch back to **Object Mode** by hitting **Tab**.

We now need to create a series of shorter sampling cylinders inside the long one. To do so, hit **Shift-a** and once again select **Mesh>Cylinder**. We will make these sampling cylinders slightly smaller than the main cylinder to avoid coincident meshes: Hit **s**, **Shift-z**, **0.199**, and **Enter**. Hit **r**, **x**, **90**, and **Enter**. Next, hit **s**, **y**, **0.024875**, and **Enter**. Hit **g**, **y**, and **-0.975** to move it very close to the left end of the end of larger cylinder (they don't touch though). 

Rename this smaller cylinder from **Cylinder.001** to **C**. Be sure to triangulate this mesh in the same way we did with the larger cylinder.

Now, we will use Blender's (very useful) array modifier to replicate this sampling cylinder 40 times. To do so, hit the **Object Modifiers** button, and from the **Add Modifier** drop-down box, select **Array**. Change **Count** to **40**. Enable **Absolute Offset** and change the third field under **Absolute Offset** to **-2.01005**. 

Now we need to make each cylinder a unique object. To do this, first hit the **Apply** button under the **Array** modifier. Then enter **Edit Mode**, hit **p**, and select **By loose parts** in the **Separate** menu. This will split each discontinuous mesh into a unique object. They wil be named C, C.001, C.002, etc. The last cylinder in the sequence should be named **C**. Rename it to **C.040**. This will make things cleaner when we want to count molecules in MCell later.

Finally, we will create a series of sampling planes in the form of of circular planes that lie between each of these cylinders. Create a cylinder by hitting **Shift-a**, and selecting **Mesh>Circle**. In the **Tool Shelf** (hit **t** to toggle it), hit **Fill** under **Add Circle**. Hit **s**, **0.199**, and **Enter**. Hit **r**, **x**, **90**, and **Enter**. Hit **g**, **y**, and **-0.95** to move it very close to the right side of our smaller cylinder. Once again, be sure to triangulate this mesh. 

Next, we will replicate this plane by using an array modifier in exactly the same way as we did previously with the cylinders (similar settings, i.e. a **Count** of **39** and an **Absolute Offset** of **-0.251255**). Also separate the object **By loose parts** in the same way you did with the small cylinder.  Finally rename the final plane from **Circle** to **Circle.040**.

.. _fick_add_params: 

Adding the Other Model Parameters
---------------------------------

First, add a single volume molecule called **vm** via CellBlender's **Define Molecules** panel. Then, in the **Define Surface Classes** panel, check **Include Surface Classes** and **Include Modify Surface Regions** since we will use surface classes and modify surface regions; in the **Reaction Output Settings** panel check **Include Reaction Output** and in **Visualization Output Settings** check **Include Viz Output**. Next, we need to tell CellBlender to export our model geometry. To do so hit the **+** sign in the **Model Objects** panel, making sure that only the **Cube** is selected.

.. _fick_export: 

Exporting the Project
---------------------

We will now export these mdls. Under **CellBlender Project Settings**, 
set the **Project Base Name** to *ficks_law*. Then hit
**Export CellBlender Project**, select a directory to save your
project to, and hit **Export MCell MDL**.

Also, make sure to save your project as a *.blend* project file
via **File->Save As** and giving it a meaningful name.

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

    area = <insert from Blender>  /* area of sampling volumes in dm^2 */
    dx   = <insert from Blender>  /* length of sampling volumes in dm */
    samplingVol = dx * area       /* volume of sampling volume in dm^3 = l*/
    dc = 5e-6 /* diffusion coefficient [cm^2/sec] */
    Na = 6.0221415e23  /* Avogardros Number */
    
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

       C.001[ALL] {
           SURFACE_CLASS = transp
       }
       
       C.002[ALL] {
           SURFACE_CLASS = transp
       }

       /* add statements for the remaining cylinders */


       Circle.001[ALL] {
           SURFACE_CLASS = transp
       }
       Circle.002[ALL] {
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
        {COUNT[vm,Scene.Cylinder]}=>"./react_data/vm_Cylinder."&seed&".dat"
        {COUNT[vm,Scene.C.001]}=>"./react_data/vm_C01."&seed&".dat"
        {COUNT[vm,Scene.Circle.001,FRONT_CROSSINGS]}=>"./react_data/vm_Circle01_front."&seed&".dat"
        /* more statements needed for Exercises 1 - 4 */
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

This concludes our initial setup. Now let's run the simulation and
see if everything checks out (the run will be quick since we are
only simulating for a single iteration during the setup phase)::

    mcell ficks_law.main.mdl


Congratulations, if everything went well. If you encountered
errors try to understand MCell's complaints and fix your errors.

Next, we need to figure out how long to simulate. We would like
to reach a steady state where the concentration gradient in the
cylinder remains constant (How would you determine if you reached
steady state?). Start with 1000 iterations initially and see if
this is enough. At this point it is **crucial** (as always really)
to load your model into blender and make sure everything looks fine.
You can use *gnuplot* for plotting: On the command line type *gnuplot*
and the enter for example::

    gnuplot> plot "react_data/001_vm_Cylinder.dat"

to view the total number of molecules in the large cylinder.

Once you're confident you have a model with a proper concentration
gradient we can finally tackle our examination of Fick's law.

.. _fick_gen_comments: 

General Comments
----------------

As the concentration gradient is evolving along x, we wish to determine 
the rate of change in concentration (dC/dt) at each time point for the 
central sampling volume composed of the two subvolumes numbered 20 and 21. 
To see this clearly, you will probably want to run a series of simulations 
using different random number seeds, so you can average your results. 

If you have done the :ref:`seed` section, then you can use the script
created there by copying the file **run_seeds.py** into your current 
directory::                                                                    
    cp /home/user/mcell_tutorial/seed/run_seeds.py /home/user/irrev_rev_uni_bi/spherical_shells/                                                            

Otherwise, create the **run_seeds.py** now. 
        
Along with the data you’ll need for Exercises 1 – 3 below, make sure that 
you output counts for molecules in subvolumes 1 and 40 (Exercise 4). 
Using MCell’s reaction data output, determination of the time course of 
dC/dt can be done in three ways which will explore now.

**Note:** Once you have verified your simulation it may be useful to
turn visualization output of to speed up your simulations.

.. _fick_exercise1: 

Exercise 1
----------

The most direct method is simply to count the number of molecules in 
subvolumes 20 and 21 at each timestep, convert the sum to concentration, 
export the concentration values for each timestep, and then differentiate 
to obtain the time course of :math:`\Delta C/ \Delta t \approx dC/dt`. 

Use MCell’s COUNT statements to output the concentration in
subvolume 20 and 21 directly. Then use the below sample python script to 
do the averaging, smoothing and differentiation. Examine the output and 
make sure you understand what is going on. You may need to increase the 
number of seeds you average over if the data is too noisy. The script 
allows you to plot different quantities by commenting/uncommenting certain 
lines - take a look:

.. code-block:: python

    #!/usr/bin/env python

    import numpy as np
    import matplotlib.pyplot as plt

    # name of files to average, smooth and differentiate
    name = "vm_conc_20_21"
    #name = "vm_conc_crossings"
    #name = "vm_conc_ficks_law"

    # number of seeds
    numSeeds = 50

    # this function does window smoothing
    # from <http://www.scipy.org/Cookbook/SignalSmooth>
    def smooth(x, window_len=11, window='hanning'):
        if x.ndim != 1:
            raise ValueError, "smooth only accepts 1 dimension arrays."
        if x.size < window_len:
            raise ValueError, "Input vector needs to be bigger than window size."
        if window_len<3:
            return x
        if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
            raise ValueError, ("Window is on of 'flat', 'hanning', 'hamming', \
                    'bartlett', 'blackman'")
        s=np.r_[2*x[0]-x[window_len-1::-1],x,2*x[-1]-x[-1:-window_len:-1]]
        if window == 'flat': #moving average
            w=np.ones(window_len,'d')
        else:  
            w=eval('np.'+window+'(window_len)')
        y=np.convolve(w/w.sum(),s,mode='same')
        return y[window_len:-window_len+1]


    # read data 
    mol_conc = None
    for seed in range(1,numSeeds):

        data = np.genfromtxt("./react_data/%s.%03d.dat" % 
                        (name, seed), dtype=float)
        timePoints = data[:, 0]
        rxn_data = data[:,1]

        if mol_conc is None:
            mol_conc = rxn_data
        else:
            # built up 2d array of molecule counts (one col/seed)
            mol_conc = np.column_stack((mol_conc, rxn_data))

    # compute the mean
    mol_conc = mol_conc.mean(axis=1)

    # smooth
    smoothed_conc = smooth(mol_conc, window_len=200)

    # differentiate data
    diff_conc = np.diff(smoothed_conc)

    # plot different results
    plt.plot(timePoints, mol_conc, 'b') 
    #plt.plot(timePoints[0:len(timePoints)-1], diff_conc, 'b') 

    plt.title("dC/dt in subvolumes 19 and 20")
    plt.show()                          

.. _fick_exercise2: 

Exercise 2
-----------

The next method is based on determination of the net fluxes into and out 
of the combined subvolumes 20 and 21. Again using MCell’s COUNT statements 
(Hint: specify forward and backward crossings), determine the net flux into 
the space across plane 19, as well as the net flux out of the space across 
plane 21. Use these results to compute the final net number of molecules in 
subvolumes 20 and 21 at each timestep, convert to concentration, and then 
output the result. Again use the above python script to differentiate and 
smooth, and compare your result to what you obtained for Exercise 1.

.. _fick_exercise3: 

Exercise 3
-----------

Now we wish to calculate :math:`dC/dt` based on Fick’s 2nd Law (make sure 
you understand how). For this we need to estimate the value of 
:math:`d$^2$C/dx$^2$` across the sampling volume, i.e., across subvolumes 20 
and 21. Hence, you will need to determine :math:`dC/dx` at plane 19, as well 
as dC/dx at plane 21, and then find the difference to obtain 
:math:`d$^2$C/dx$^2$`. To do this you will need to determine the 
concentration in subvolumes 19 and 22, as well as in subvolumes 20 and 21. 
Finally multiply by the diffusion coefficient $D$.
Once you have calculated :math:`d$^2$C/dx$^2$` using COUNT statements, you
can output the result, and again use the python script from above for
averaging, smoothing and differentiating. 

When considering the methods used to compute :math:`dC/dt` in Exercises 
1, 2 and 3 which final result do you expect to show the most noise? Why?
Do you results reflect this.

.. _fick_exercise4: 

Exercise 4
-----------

Finally, plot the ratio of variance to mean number of molecules for 
subvolumes 1, 20, 21, and 40. What do you observe and why? 

You can use the following python script to do the analysis::

    #!/usr/bin/env python

    import numpy as np
    import matplotlib.pyplot as plt
    import os

    startOfFileToAverage = "vm_C01"   # beginning of filenames to average
                                      # over

    mol_counts = None
    files = os.listdir('react_data')   # build a list of reaction data file names
    files.sort()                       # sort that list alphabetically

    for f in files:                    # iterate over the list of file names
        if f.startswith(startOfFileToAverage):
            rxn_data = np.genfromtxt("./react_data/%s" % f, dtype=float)
            rxn_data = rxn_data[:, 1]  # take the second column
            if mol_counts is None:
                mol_counts = rxn_data
            else:
                # built up 2d array of molecule counts (one col/seed)
                mol_counts = np.column_stack((mol_counts, rxn_data))
        else:
            pass

    mol_mean = mol_counts.mean(axis=1)  # take the mean of the rows
    mol_var = mol_counts.var(axis=1)    # compute the variance of the rows
    plt.plot(mol_mean/mol_var, 'g')     # plot ratio of mean and variance
    plt.show()


