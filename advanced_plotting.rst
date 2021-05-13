.. _advanced_plotting:

*********************************************
Advanced Plotting
*********************************************

.. warning::

   The following sections describe advanced features that are not intended for
   the average user.

Installing Plotting Plug-Ins
---------------------------------------------

CellBlender supports a variety of plotting plug-ins that may be installed in
the "data_plotters" folder under the cellblender addon folder (for example on a Mac it would be something like: /Applications/Blender-2.79-CellBlender/blender.app/Contents/Resources/2.79/scripts/addons/cellblender/data_plotters). Each
plotting plug-in will have its own folder in that directory, and within that
folder must (at least) be a file named **__init__.py**. As an example, the
xmgrace plug-in will be found at
/Applications/Blender-2.79-CellBlender/blender.app/Contents/Resources/2.79/scripts/addons/cellblender/data_plotters/xmgrace*.
There may be other files required in that folder. For example, the Java Plotter
requires the file **PlotData.jar** to be there, and the matplotlib plotter
requires the files **mpl_plot.py** and **mpl_defaults.py**. The number and
purposes of these additional files depends completely on the plotting plug-in.

Installing a new plotting plug-in only requires the creation of a new directory
in the **data_plotters** directory (the name can be whatever you feel is
appropriate), and the installation of the associated files (which must include
an **__init__.py** file.

Here's an example of a simple plotting plug-in for xmgrace::

    import os
    import subprocess

    def find_in_path(program_name):
        for path in os.environ.get('PATH','').split(os.pathsep):
            full_name = os.path.join(path,program_name)
            if os.path.exists(full_name) and not os.path.isdir(full_name):
                return full_name
        return None


    def get_name():
        return ( "XmGrace Plotter" )


    def requirements_met():
        path = find_in_path ( "xmgrace" )
        if path == None:
            print ( "Required program \"xmgrace\" was not found" )
            return False
        else:
            return True


    def plot ( data_path, plot_spec ):
        program_path = os.path.dirname(__file__)
        
        # XmGrace expects plain file names so translate:
        
        plot_cmd = find_in_path ( "xmgrace" )
        
        for plot_param in plot_spec.split():
            if plot_param[0:2] == "f=":
                plot_cmd = plot_cmd + " " + plot_param[2:]
        
        pid = subprocess.Popen ( plot_cmd.split(), cwd=data_path )

.. warning:: 

    This plotting api is still being developed and changes are expected!


Writing Plotting Plug-Ins
---------------------------------------------

CellBlender's plotting plug-in API is still very immature, so drastic changes
may be anticipated. But for those who need to write their own plotting plug-in,
the current specification is as follows...

Each plotting plug-in must have an **__init__.py** file containing the following
functions:

* get_name()
* requirements_met()
* plot ( data_path, plot_spec )

These are described in separate sections below.

get_name()
-----------------------------------
The **get_name()** function simply returns the name of this plug-in in the form
of a normal python string. This is used for the user interface.

requirements_met()
-----------------------------------
The **requirements_met()** function is called to determine if the operating
environment meets the requirements for this plug-in to work. For example, if
the plug-in is written in Java, then the requirements_met function should
check to see that a suitable Java Virtual Machine is installed. This function
returns True if the requirements are met, and false otherwise.

plot ( data_path, plot_spec )
-----------------------------------
The **plot()** function actually performs the plot. The plot function takes
two parameters:

* data_path - a path to where the data files exist (added to each file)
* plot_spec - a list of files and modifiers that describe the plotting

The data_path is fairly self-explanatory, but the plot_spec requires a little
bit of explanation.

The fundamental plot specification is just a list of file names immediately
prefixed with "f=" and separated by spaces::

  f=mol1v1.dat f=mol1v2.dat f=mol1s1.dat f=mol2s1.dat

Every plotting plug-in should recognize the "f=" prefix as specifying the name
of a file where the file itself contains two columns of numbers (time and count)
in ASCII text format. As a minimum, the plug-in should be able to plot all such
files in a single plot.

At this point, all additional parameters are optional ... but certainly useful!

Among the optional parameters are the separators "page" and "plot". These are
inserted between file names to produce either a new page or a new plot. For
example, the previous specification could plot the volume and surface molecules
in two separate plots within the same page using this command::

  f=mol1v1.dat f=mol1v2.dat plot f=mol1s1.dat f=mol2s1.dat
  
Alternatively, the the following command will put each of those plots on their
own pages::

  f=mol1v1.dat f=mol1v2.dat page f=mol1s1.dat f=mol2s1.dat

This command creates two pages and creates 2 plots on each page::

  f=mol1v1.dat plot f=mol1v2.dat page f=mol1s1.dat plot f=mol2s1.dat

Finally, here is the current plotting plug-in API (**SUBJECT TO CHANGE**)

* defs=filename        ... Loads default parameters from a python file
* page                 ... Starts a new page (figure in matplotlib)
* plot                 ... Starts a new plot (subplot in matplotlib)
* color=#rrggbb        ... Selects a color via Red,Green,Blue values
* color=color_name     ... Selects a color via standard color names
* title=title_string   ... Sets the title for each plot
* pagetitle=string     ... Sets the title for each page
* xlabel=label_string  ... Sets the label for the x axis
* ylabel=label_string  ... Sets the label for the y axis
* legend=code          ... Adds a legend with code = 0..10 (-1=none)
* n=name               ... Name used to over-ride file name in legend
* f=filename           ... Plots the file with current settings


