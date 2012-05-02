.. _variable_rxn_rates:

*********************************************
Variable Reaction Rates
*********************************************

Begin by creating a copy of the **surf_class_rxns** directory, by typing the following command at the terminal::

    cp -fr /home/user/mcell_tutorial/surf_class_rxns /home/user/mcell_tutorial/var_rxn_rate

Don't forget to replace **user** with your actual user name. In the new **var_rxn_rate** directory, create a new text file called **rxn_rate.txt**. Add the following text in the file::

    0      0
    5E-4   1E8

The first column is the time (seconds), and the second column is the reaction rate at that time. The units for the reaction rate are the same as used earlier in the :ref:`reactions` section. 

The example shown above is a very simple case where the reaction only changes once. You could just as well have it change every time step, like this::

    0      0
    1E-6   1.0E5
    2E-6   1.1E5
    3E-6   1.2E5
    ...

Save the file and quit. In **intro.mdl**, go to the reaction section and change the rate to **"rxn_rate.txt"** (with quotations), like in the following::

    DEFINE_REACTIONS {
        vol1, + surf1' -> surf1' + vol2' ["rxn_rate.txt"]
        vol1, + surf2' @ empty' -> surf2' + vol2' ["rxn_rate.txt"]
    }   

Save the file and run it with MCell by entering the command:: 

    mcell intro.mdl

