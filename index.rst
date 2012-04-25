.. intro_tutorial documentation master file, created by
   sphinx-quickstart on Fri Apr 20 15:55:21 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction to MCell
=====================

In order to quickly show what can be done with MCell, we'll begin by generating a simple model and gradually add in more features. Our initial model will contain a cube that has diffusing surface and volume molecules that react with each other to create new molecules. Later, we'll add more complex reactions and surface properties. At that point, we'll begin to move on to some more advanced topics, like optimizing a simulation and analyzing data.

Much of the theory will be skipped over, as it's available elsewhere_. For a more detailed explanation of any given topic, please see the `quick reference guide`_. 

The completed project files for the tutorial can be downloaded here_. You will generate these same files simply by following along with the tutorial, but they are provided here in case you need them for any reason.

.. _elsewhere: https://www.mcell.psc.edu/publications.html

.. _quick reference guide: http://mcell.psc.edu/download/files/mcell3_qrg_092010.pdf

.. _here: https://www.mcell.psc.edu/tutorials/mdl/main/mcell_tutorial.tgz

.. toctree::
   :numbered:
   :maxdepth: 4

   software
   getting_started
   annotate
   examine_output
   surface_classes
   variable_rxn_rates
   surf_class_surf_mol
   checkpointing
   rel_pattern
   clamp
   optimize
   analyze
   seed

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

