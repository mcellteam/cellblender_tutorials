.. _install:

+++++++++++++++++++++++++++++++++++++++++++++
Software Installation
+++++++++++++++++++++++++++++++++++++++++++++

.. _mcell_install:

*********************************************
MCell Installation
*********************************************

MCell Overview
---------------------------------------------

MCell is available for Linux, OS X, and Windows. You can download it from the
`MMBioS web site`_. In the past, MCell was run exclusively from the command
line. With the development of CellBlender, this is no longer necessary
(although it can still be very useful). MCell, by itself, does not have a
graphical user interface and cannot be run by double-clicking an icon (Windows
users take note). 

.. note::

    Some of the following instructions make use of the command line. These
    sections will not apply to Windows users.

.. _MMBioS web site: http://mmbios.org/index.php/mcell-3-2-download

Installing MCell for Linux/OS X
---------------------------------------------

Download and Extract MCell
=============================================

Download the desired binary file for your system (e.g., MCell v. |release| for
Linux x86).

The binary file that you download is a compressed file with a name that ends in
either ".gz" or ".zip". Your browser may think that it knows more than you do
and automatically unzip the file without changing its name (this can lead to
considerable confusion).

Assuming that your browser hasn't already done so, unzip the file, e.g.,

::

    gunzip mcell-3.2_x86.gz

If this succeeds, the file will no longer have the .gz suffix. If it fails and
you get an error message, it's probably already been unzipped by your browser.
In this case just continue with the next step, but remember to include the
".gz" suffix on the file name.

Rename and Make Executable
=============================================

Rename the file to something more convenient and make it executable, e.g.,

::

    mv mcell-3.2_x86 mcell
    chmod a+x mcell

Put MCell in a PATH Directory
=============================================

Depending on your preferences, you may want to put the resulting executable
binary in an appropriate place for yourself or all the users of the machine
(e.g., ``sudo mv mcell /usr/local/bin`` if you have root privileges). If you do
not have root privileges, then you can put it in your home directory (e.g.
``mkdir /home/user/bin; mv mcell home/user/bin`` where **user** is your user
name). However, you need to make sure that the directory you put it in is
either in your PATH_ or that you add it to your PATH. You can do this by typing
``export PATH=$PATH:/home/user/bin`` (once again, **user** should be your user
name)

.. _PATH: https://en.wikipedia.org/wiki/PATH_%28variable%29

Verify correct function by typing the name of the executable at a command
prompt, e.g.,

::

    mcell

If you have put MCell in an appropriate directory included in your path for
executables, you should see a startup message followed by an error that
indicates no MDL (Model Description Language) file has been specified. MDL
files are used to design and control MCell simulations (see MCell tutorials).

.. _cellblender_install:

*********************************************
CellBlender Installation
*********************************************

Installing CellBlender
---------------------------------------------

Startup Blender and go to the **File->User Preferences** menu. In the **User
Preferences** control panel choose the **Addons** tab. Click the **Install from
File** button at the bottom of the window. Navigate to the unextracted zip file
that you downloaded (cellblender_v1.0_RC.zip), select it, and click the
**Install from File** button near the upper-right hand corner.

.. note::

    If you need to install a newer version of CellBlender, the installation
    process is the same. The new version of CellBlender should cleanly install
    over the existing version.

Activating CellBlender in Blender
---------------------------------------------

Scroll down until you see **Cell Modeling: CellBlender** and select the
checkbox to enable it. Then, click **Save as Default** to enable the addon
permanently in Blender.

*********************************************
DReAMM and PSC DX Installation
*********************************************

DReAMM and PSC DX are no longer actively developed, but will remain available
for download. The installation instructions can be found here_.

.. _here: https://www.mcell.psc.edu/tutorials_old/installs.html
