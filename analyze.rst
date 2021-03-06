.. _analyze:

*********************************************
Analyzing Your Data
*********************************************

There are many tools available for plotting and analyzing data. We will make
use of python along with numpy and matplotlib. Using these tools, we will
generate a histogram of molecule locations relative to the origin, and also
find such things as the mean, min, and max. First, however, we need the mdl. In
the main tutorial directory, create a new directory called **hist**. Inside
that directory, create an mdl called **hist.mdl**, and insert the following
text into it:

.. code-block:: mdl

    TIME_STEP = 1.0e-6
    ITERATIONS = 1000
                     
    DEFINE_MOLECULES 
    {
        vol1 {DIFFUSION_CONSTANT_3D = 1e-7}
    }

    INSTANTIATE world OBJECT 
    { 
        vol1_rel SPHERICAL_RELEASE_SITE 
        {
            LOCATION = [0,0,0] 
            MOLECULE = vol1 
            NUMBER_TO_RELEASE = 5000
            SITE_DIAMETER = 0.0 
        }   
    }

    VIZ_OUTPUT 
    {
        MODE = ASCII
        FILENAME = "./viz_data/hist" 
        MOLECULES 
        { 
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}  
        }   
    } 

Run this mdl by entering the command::

    mcell hist.mdl

It will create a visualization directory called **viz_data**.

Create a file called **hist.py** and copy the following text into it::

    #!/usr/bin/env python

    import numpy as np
    import matplotlib.pyplot as plt

    mol_pos_file = "./viz_data/hist.ascii.1000.dat"
    data = np.genfromtxt(mol_pos_file)   # open molecule positions as 2d array
    data = data[:, 1]                    # create array from 1st column (X pos)
    print('The min is: %.3f' % np.min(data))
    print('The max is: %.3f' % np.max(data))
    print('The mean is: %.3f' % np.mean(data))
    print('The standard deviation is: %.3f' % np.std(data))
    plt.hist(data, 100)                  # create a histogram with 100 bins
    plt.xlabel('Distance (Microns)')     # add an x-axis label
    plt.ylabel('Molecules')              # add an y-axis label
    plt.show()                           # plot the data

Although the comments explain what is happening, let's break it down as simply
as possible. The file **hist.ascii.1000.dat** contains the positions of each
vol1 molecule at an iteration specified by the directory (e.g.
**iteration_1000**). Every line of the file contains the molecule name and
seven numbers each separated by a space. The first number is an ID. The second,
third, and fourth numbers represent the x, y, and z locations. The final three
numbers are irrelevant for our example here but would represent a vertex normal
if this was a surface molecule. Here are what the first few lines of
**hist.ascii.1000.dat** in the **iteration_1000** directory look like::

    vol1 0 -0.238189256 -0.0302122369 -0.0249790538 0 0 0
    vol1 1 -0.360854863 -0.185503773 0.0169416791 0 0 0
    vol1 2 0.0545683757 0.100612229 0.164147866 0 0 0
    vol1 3 0.0456457024 0.196103069 0.34263021 0 0 0

We are loading **hist.ascii.1000.dat** into a two dimensional array called
**data**. We then "slice" the second column which contains all the X locations.
Next, we print the min, max, mean, and standard deviation to the command line.
Lastly, we create the histogram with labels and plot (or show) it.

Run the file now by typing::

    python hist.py

