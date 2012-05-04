.. _checkpointing:

*********************************************
Checkpointing Overview
*********************************************

Checkpointing allows you to stop a simulation at a specified iteration and resume it at some later point. This can be beneficial for several different reasons:

* You are using any sort of multi-user system that you must share time with on with others
* The computer you are using crashes or is shutdown unexpectedly
* There are parameters you want to change partway through a simulation

We'll cover how to set up checkpointing in the next two sections, starting with a simple case where we modify a couple parameters. Then we will follow this up with a more interesting case where we have a mesh changing shape over time and molecules that will react to it.

.. contents:: :local:

.. _checkpointing_mdl:

Creating the MDL
---------------------------------------------
inside of **/home/user/mcell_tutorial**, create a directory called **change_dc**. Inside that directory, create a file called **change_dc1.mdl**. Add the following text to that file::

    CHECKPOINT_INFILE = "dc_chkpt"
    CHECKPOINT_OUTFILE = "dc_chkpt"
    CHECKPOINT_ITERATIONS = 100 
    ITERATIONS = 200 
    TIME_STEP = 1E-6

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-7}
    }   

    INSTANTIATE World OBJECT {
        vol1_rel RELEASE_SITE {
            SHAPE = SPHERICAL
            LOCATION = [0,0,0]
            SITE_DIAMETER = 0.0 
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 100 
        }   
    }   

    VIZ_OUTPUT {
        FILENAME = "change_dc"
        MOLECULES {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }   
    } 

:index:`\ <single:CHECKPOINT_INFILE>` :index:`\ <single:CHECKPOINT_OUTFILE>` :index:`\ <single:CHECKPOINT_ITERATIONS>` There are three new commands in this file: **CHECKPOINT_INFILE**, **CHECKPOINT_OUTFILE**, and **CHECKPOINT_ITERATIONS**. As we mentioned earlier, checkpointing allows you to stop a simulation and resume it later. This is accomplished by means of a checkpoint file that is written (**CHECKPOINT_OUTFILE**) when the simulation is temporarily stopped and later read (**CHECKPOINT_INFILE**) when the simulation is resumed. The value assigned to these two commands is the name of the file that is written or read. In this case, they both have the same name, although that is not required. **CHECKPOINT_ITERATIONS** indicates at what iteration the simulation is temporarily stopped and the checkpoint file is created.

Now make a copy of **change_dc1.mdl** called **change_dc2.mdl** by entering the command::

    cp change_dc1.mdl change_dc2.mdl

Then change the diffusion constant from **1E-7** to **1E-5** in the second mdl. Once again, save and quit. 

Running the Simulation
---------------------------------------------

Now run the first mdl by entering the command::

    mcell change_dc1.mdl

When it is finished running, enter the command::

    ls

Notice that a file called **dc_chkpt** was created. This file stores the information needed to recommence running the simulation. Let's finish it now by entering teh command::

    mcell change_dc2.mdl

Visualize the results with CellBlender. When you playback the animation, you will notice that the molecules start off moving rather slowly, and then speed up halfway through the simulation, coinciding with the change in diffusion constant.

This is just a simple example of one parameter you can change. Here is a partial list of some other parameters that you could change:

* **TIME_STEP**
* reaction rates
* **SURFACE_CLASS** properties (**ABSORPTIVE**, **TRANSPARENT**, **REFLECTIVE**)

