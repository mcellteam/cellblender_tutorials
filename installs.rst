.. _install:

*********************************************
MCell for UNIX/all Mac
*********************************************

Download the desired binary file for your system (e.g., MCell v. 3.1.965 for Linux x86).

The binary file that you download is a gzip’ed file with a name that ends in ".gz". Your browser may think that it knows more than you do and automatically unzip the file without changing its name (this can lead to considerable confusion).

Assuming that your browser hasn't already done so, unzip the file, e.g.,

::

    [me@my_computer ~] $ gunzip mcell-3.1.965_x86.gz

If this succeeds, the file will no longer have the .gz suffix. If it fails and you get an error message, it's probably already been unzipped by your browser. In this case just continue with the next step, but remember to include the ".gz" suffix on the file name.

Rename the file to something more convenient and make it executable, e.g.,

::

    [me@my_computer ~] $ mv mcell-3.1.965_x86.gz mcell

    [me@my_computer ~] $ chmod a+x mcell

Depending on your preferences, you may want to put the resulting executable binary in an appropriate place for yourself or all the users of the machine (e.g., /usr/local/bin if you have root privileges).

Verify correct function by typing the name of the executable at a command prompt, e.g.,

::

    [me@my_computer ~] $ mcell

If you have put MCell in an appropriate directory included in your path for executables, you should see a startup message followed by an error that indicates no MDL (Model Description Language) file has been specified. MDL files are used to design and control MCell simulations (see MCell tutorials).
