.. _mcell_install_linux_osx:

Installing MCell (Linux/OS X)
---------------------------------------------

Extract MCell (Linux/OS X)
=============================================

The binary file that you download is a compressed file with a name that ends in
".gz". Open a terminal and navigate to where the file was downloaded (e.g. ``cd
/home/user/Downloads``). Alternatively, you can do this through a GUI file
manager like Nautilus in Ubuntu, but we won't show that here.

Now, unzip the file by typing the following at the command line::

    gunzip mcell-3.3_x86_64.gz

If this succeeds, the file will no longer have the ".gz" suffix.

Rename and Make Executable (Linux/OS X)
=============================================

Rename the file to something more convenient and make it executable, e.g.,

::

    mv mcell-3.3_x86_64 mcell
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
file has been specified.
