.. _variable_rxn_rates:

*********************************************
Variable Reaction Rates
*********************************************

Eventually, it will be possible to set up variable reaction rates directly
within CellBlender. Until that time, you can still do it by manually
hand-editing some files.

Begin by creating a copy of the **sc_rxns** directory, by typing the following
command at the terminal::

    cp -fr /home/user/mcell_tutorial/sc_rxns /home/user/mcell_tutorial/var_rxn_rate

Don't forget to replace **user** with your actual user name. Change into the
new directory now by entering the following command at the terminal::

    cd /home/user/mcell_tutorial/var_rxn_rate/sc_rxns_files/mcell

.. note::

   We have copied the entire directory of sc_rxns, so the blend file and the
   MDL sub-directory still retain the original names (i.e. sc_rxns.blend and
   sc_rxns_files, not var_rxn_rates.blend and var_rxn_rates_files).

In this directory, create a new text file called **rxn_rate.txt**. Add the
following text in the file::

    0      0
    5E-4   1E8

The first column is the time (seconds), and the second column is the reaction
rate at that time. The units for the reaction rate are the same as used earlier
in the :ref:`reactions` section. 

The example shown above is a very simple case where the reaction only changes
once. You could just as well have it change every time step, like this::

    0      0
    1E-6   1.0E5
    2E-6   1.1E5
    3E-6   1.2E5
    ...

Save the file and quit.

Open **sc_rxns.reactions.mdl**, go to the reaction section and change the rate
to **"rxn_rate.txt"** (with quotations), like in the following:

.. code-block:: none
    :emphasize-lines: 3,4

    DEFINE_REACTIONS
    {
        vol1, + surf1' -> surf1' + vol2' ["rxn_rate.txt"]
        vol1, + surf2' @ empty' -> surf2' + vol2' ["rxn_rate.txt"]
    }   

Save the file and run it with MCell by entering the command:: 

    mcell Scene.main.mdl

If you did not follow the directions listed in :ref:`installs` and put MCell in
a directory that is visible to your PATH_, you might see the following
command::

    mcell: command not found

.. _PATH: https://en.wikipedia.org/wiki/PATH_%28variable%29

Once MCell successfully runs, you can visualize the data by opening the blend
(i.e. ``/home/mcell_tutorial/var_rxn_rate/sc_rxns.blend``) and hitting the
**Read Viz Data** button under **Visualize Simulation Results**.
