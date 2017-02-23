.. _mcell_install_linux_osx:

Installing MCell (Linux/OS X)
---------------------------------------------

.. note::

    MCell is included in the CellBlender 1.1 bundle (linux_, windows_). You
    only need to install MCell separately if you would like to run it outside
    of CellBlender or if you are setting up CellBlender from scratch (as is
    needed on OSX).

.. _linux: http://mcell.org/download/files/cellblender1.1_bundle_linux.zip
.. _osx: http://mcell.org/download/files/cellblender1.1_bundle_osx.zip
.. _windows: http://mcell.org/download/files/cellblender1.1_bundle_windows.zip

Extract MCell (Linux/OS X)
=============================================

The binary file that you download is a compressed file with a name that ends in
".zip". Open a terminal and navigate to where the file was downloaded (e.g.
``cd /home/user/Downloads``). Alternatively, you can do this through a GUI file
manager like Nautilus in Ubuntu, but we won't show that here.

Now, unzip the file by typing the following at the command line::

    unzip mcell_3.4_linux.zip

If this succeeds, the file will no longer have the ".gz" suffix.

Rename and Make Executable (Linux/OS X)
=============================================

Rename the file to something more convenient and make it executable, e.g.,

::

    mv mcell_3.4_linux mcell
    chmod a+x mcell

Put MCell in a PATH Directory (Linux/OS X)
=============================================

Depending on your preferences, you may want to put the resulting executable
binary in an appropriate place for yourself or all the users of the machine
(e.g., ``sudo mv mcell /usr/local/bin`` if you have root privileges). If you do
not have root privileges, then you can put it in your home directory (e.g.
``mkdir /home/user/bin; mv mcell home/user/bin`` where **user** is your user
name). However, you need to make sure that the directory you put it in is
either in your PATH_ or that you add it to your PATH. You can add it to your
PATH by typing ``export PATH=$PATH:/home/user/bin`` (once again, **user**
should be your user name). To make this change permanent, add this command to
the **.bash_profile** file located in your home directory. If this file does
not exist, create it and add the line.

.. _PATH: https://en.wikipedia.org/wiki/PATH_%28variable%29

Test MCell (Linux/OS X)
=============================================

Verify that MCell is working by typing the following at the terminal::

    mcell

If you have successfully put MCell in your PATH, you should see a startup
message followed by an error that indicates no MDL (Model Description Language)
file has been specified::

    MCell: command-line argument syntax error: No MDL file name specified
    MCell 3.4 (commit: 275420e  date: Thu, 29 Sep 2016 14:07:12 -0400)
      Running on washburne at Fri Jan 27 11:14:11 2017

      Copyright (C) 2006 - 2016 by
        The National Center for Multiscale Modeling of Biological Systems,
        The Salk Institute for Biological Studies, and
        Pittsburgh Supercomputing Center, Carnegie Mellon University,


    **********************************************************************
    MCell development is supported by the NIGMS-funded (P41GM103712)
    National Center for Multiscale Modeling of Biological Systems (MMBioS).
    Please acknowledge MCell in your publications.
    **********************************************************************

    Usage: ./mcell_3.4_linux [options] mdl_file_name

      options:
         [-help]                  print this help message
         [-version]               print the program version and exit
         [-fullversion]           print the detailed program version report and exit
         [-seed n]                choose random sequence number (default: 1)
         [-iterations n]          override iterations in mdl_file_name
         [-logfile log_file_name] send output log to file (default: stdout)
         [-logfreq n]             output log frequency
         [-errfile err_file_name] send errors log to file (default: stderr)
         [-checkpoint_infile checkpoint_file_name]   read checkpoint file
         [-checkpoint_outfile checkpoint_file_name]  write checkpoint file
         [-quiet]                 suppress all unrequested output except for errors
         [-with_checks ('yes'/'no', default 'yes')]   performs check of the geometry for coincident walls

