.. _parameters:

**********
Parameters
**********

Overview
=========

    * The parameter system is used to create cellblender variables. They're just like normal programming variables such that one variable is used for multiple objects and is user defined. This tutorial will run through a basic molecule simulation using the **Sweeping Parameter** feature.

    	* The inital Parameter setup, the expression can be set to either a value or a math expression. You can also enable sweeping expressions that go through a series of values (1:10 goes through the values 1 to 10). The **Units** and **Description** are user defined for better variable organizing.

			.. image:: ./images/parameters/parameter_init.png    		

    * Select the **Parameter button**.

         .. image:: ./images/shared/button_panels/parameters_panel_h.png

    * Create a new **parameter**, and press the **Enable Sweep** button.

         .. image:: ./images/parameters/parameters_create.png

    * Different options

    	* Name the parameter **var**.

    	* Set the sweep expression to **1e-6,1e-7,1e-8**. 

    	.. image:: ./images/parameters/parameters_set.png

    * Create a molecule.

    	* Name the molecule **mol_1** and set the **Diffusion Const** to the parameter **var**.

    	.. image:: ./images/parameters/parameters_molecule.png

    * Create a release site for the molecule you just created.

        * Keep the name **Release_site_1**.
        * Use **mol_1**.
    	* Set the **Quanity to release** to **1000**.

    	.. image:: ./images/parameters/parameter_molecule_place.png

    * Set up the simulation.    	

    	* Click on the **Output/Control Options** and click on the **Mcell via Queue Runne** drop down.

    		.. image:: ./images/parameters/parameter_sim.png

    	* Set the simulation to **MCell via Sweep runner**.

    		.. image:: ./images/parameters/parameter_sweep_runner.png

    	* The final product should look something like the following, with the simulation going through the different **Diffusion Constants** in the same run.

        .. image:: ./images/parameters/parameter_molecule_clump.png

