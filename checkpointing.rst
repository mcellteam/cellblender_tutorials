.. _checkpointing:

*********************************************
Checkpointing Overview
*********************************************

.. Git Repo SHA1 ID: a1abdd291b75176d6581df41329781ae5d5e1b7d

.. note::

    The simulations and visualizations in this tutorial were generated using
    Blender 2.67 and CellBlender 1.0 RC. It may or may not work with other
    versions.

Checkpointing allows you to stop a simulation at a specified iteration and
resume it at some later point. This can be beneficial for several different
reasons:

* You are using any sort of multi-user system that requires you to share time
  with others
* The computer you are using crashes or is shutdown unexpectedly
* There are parameters you want to change partway through a simulation

We'll cover how to set up checkpointing in the next several sections, starting
with a simple case where we modify a couple parameters.

.. contents:: :local:

.. _checkpointing_mdl:

Creating the MDL
---------------------------------------------

Eventually, it will be possible to use checkpointing directly within
CellBlender. Until that time, you can still do it by manually hand-editing some
files.

Inside of **/home/user/mcell_tutorial**, type the following command::

    mkdir -p change_dc/change_dc_files/mcell

.. note::

   CellBlender expects a certain directory structure for visualization. That is
   why we are creating these sub-directories in a very specific way.

Then within that directory (i.e.
**/home/user/mcell_tutorial/change_dc/change_dc_files/mcell**), create a file
called **change_dc1.mdl**. Add the following text to that file:

.. code-block:: mdl
    :emphasize-lines: 1-3

    CHECKPOINT_INFILE = "dc_chkpt"
    CHECKPOINT_OUTFILE = "dc_chkpt"
    CHECKPOINT_ITERATIONS = 100
    ITERATIONS = 200
    TIME_STEP = 1E-6

    DEFINE_MOLECULES
    {
      vol1 {DIFFUSION_CONSTANT_3D = 1E-7}
    }

    INSTANTIATE World OBJECT
    {
      vol1_rel RELEASE_SITE
      {
        SHAPE = SPHERICAL
        LOCATION = [0,0,0]
        SITE_DIAMETER = 0.0
        MOLECULE = vol1
        NUMBER_TO_RELEASE = 100
      }
    }

    sprintf(seed,"%05g",SEED)

    VIZ_OUTPUT
    {
      MODE = CELLBLENDER
      FILENAME = "./viz_data/seed_" & seed & "/Scene"
      MOLECULES
      {
        NAME_LIST {vol1}
        ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
      }
    }

:index:`\ <single:CHECKPOINT_INFILE>` :index:`\ <single:CHECKPOINT_OUTFILE>`
:index:`\ <single:CHECKPOINT_ITERATIONS>` There are three new commands in this
file (which have been highlighted): **CHECKPOINT_INFILE**,
**CHECKPOINT_OUTFILE**, and **CHECKPOINT_ITERATIONS**. As we mentioned earlier,
checkpointing allows you to stop a simulation and resume it later. This is
accomplished by means of a checkpoint file that is written
(**CHECKPOINT_OUTFILE**) when the simulation is temporarily stopped and later
read (**CHECKPOINT_INFILE**) when the simulation is resumed. The value assigned
to these two commands is the name of the file that is written or read. In this
case, they both have the same name, although that is not required.
**CHECKPOINT_ITERATIONS** indicates at what iteration the simulation is
temporarily stopped and the checkpoint file is created.

Now make a copy of **change_dc1.mdl** called **change_dc2.mdl** by entering the
command::

    cp change_dc1.mdl change_dc2.mdl

Then change the diffusion constant from **1E-7** to **1E-5** in the second mdl.
Once again, save and quit. 

Running the Simulation
---------------------------------------------

Now run the first mdl by entering the command::

    mcell change_dc1.mdl

When it is finished running, enter the command::

    ls

Notice that a file called **dc_chkpt** was created. This file stores the
information needed to recommence running the simulation. Let's finish it now by
entering the command::

    mcell change_dc2.mdl

Visualizing the Results
---------------------------------------------

Start Blender. Save your blend file with the name **change_dc.blend** in
**/home/user/mcell_tutorial/change_dc**. Be careful to name it correctly, as
the directory structure we set up earlier depends upon it. Normally, this is
all handled automatically by CellBlender, but we must be careful when
hand-editing files. Delete the default **Cube** now (select and hit **x**),
since it's not actually a part of our simulation. Hit **Read Viz Data** under
the **Visualize Simulation Results** panel. Hit **Alt-a** to begin playing back
the animation. You will notice that the molecules start off moving rather
slowly, and then speed up halfway through the simulation, coinciding with the
change in diffusion constant.

This is just a simple example of one parameter you can change. Here is a
partial list of some other parameters that you could change:

* **TIME_STEP**
* reaction rates
* **SURFACE_CLASS** properties (**ABSORPTIVE**, **TRANSPARENT**, **REFLECTIVE**)

Time Based Checkpointing
---------------------------------------------

Instead of checkpointing at a specific iteration, you can alternatively create
a checkpoint at a set time. To do this, replace **CHECKPOINT_ITERATIONS** with
**CHECKPOINT_REALTIME**. The value assigned to this is a series of numbers
separated by colons. The units and formatting are illustrated below:

* **days:hours:minutes:seconds**
* **hours:minutes:seconds**
* **minutes:seconds**
* **seconds**

For example, if you set **CHECKPOINT_REALTIME = 1:30**, then the simulation
would create a checkpoint after running for 1 minute and 30 seconds. Or if you
set **CHECKPOINT_ITERATIONS = 2:6:3:40**, then the simulation would create a
checkpoint after running for 2 days, 6 hours, 3 minutes, and 40 seconds.

If you want the simulation to automatically continue running after writing a
checkpoint file, you have to put the keyword **NOEXIT** at the end of the
**CHECKPOINT_REALTIME** command, like this: **CHECKPOINT_REALTIME = 1:30
NOEXIT**.

You will know that a checkpoint file has been created, because MCell will
report something like this while it is running::

    MCell: time = 1098, writing to checkpoint file chkpt (periodic).

Checkpointing with SIGUSR1 and SIGUSR2
---------------------------------------------

Sometimes, you need to end a simulation *right now*, but a lot of time can be
wasted if you haven't checkpointed recently. To deal with this problem, pass
the **SIGUSR1** or **SIGUSR2** flags to the **kill** command along with MCell's
PID. If you use **SIGUSR1**, MCell will create a checkpoint and continue
running. If you use **SIGUSR2**, MCell will create a checkpoint and end the
simulation. You can use the **top** or **ps** commands to find MCell's PID. For
example, if your MCell executable is called **mcell**, then type the following
command while MCell is running::

    ps -e | grep mcell

This will output something similar to this::

    7984 pts/4    00:00:10 mcell

The first number listed, **7984**, is the PID. Next, enter the following
command (using your own PID in place of **7984**)::

    kill -SIGUSR1 7984

This creates a checkpoint and keeps the simulation running. However, to create
a checkpoint and *kill* the simulation, you would enter the following command::

    kill -SIGUSR2 7984

You will know that these worked if MCell reports something like this::

    MCell: time = 1282, writing to checkpoint file chkpt (user signal detected).
