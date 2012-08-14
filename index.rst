.. intro_tutorial documentation master file, created by
   sphinx-quickstart on Fri Apr 20 15:55:21 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====================
Introduction to MCell
=====================

In order to quickly show what can be done with MCell, we'll begin by generating a simple model and gradually add in more features. Our initial model will contain a cube that has diffusing surface and volume molecules that react with each other to create new molecules. Later, we'll add more complex reactions and surface properties. At that point, we'll begin to move on to some more advanced topics, like optimizing a simulation and analyzing data.

Much of the theory will be skipped over, as it's available elsewhere_. For a more detailed explanation of any given topic, please see the quick reference guide (pdf_, html_). 

The completed project files for sections 1-13 can be downloaded here_. You will generate these same files simply by following along with these tutorials, but they are provided here in case you need them for any reason.

.. _elsewhere: https://www.mcell.psc.edu/publications.html

.. _pdf: http://mcell.org/documentation/mcell3_qrg.pdf

.. _html: http://mcell.org/documentation/mcell3_qrg.xhtml

.. _here: https://www.mcell.org/tutorials/downloads/tutorials1-13.tgz

.. toctree::
   :numbered:
   :maxdepth: 4

   software
   getting_started
   examine_annotate
   visualize_plot
   surface_classes
   variable_rxn_rates
   surf_class_surf_mol
   checkpointing
   rel_pattern
   clamp
   optimize
   analyze
   seed
   ficks_laws
   irrev_rev_uni_bi
   mapk
   rat
   lotka_volterra

Although no longer actively maintained, the `legacy DReAMM and MCell tutorials`_ are still available. 

.. _legacy DReAMM and MCell tutorials: http://mcell.org/tutorials_old/tlist.htm

Please send any feedback concerning these tutorials to `jczech@psc.edu`_.

.. _jczech@psc.edu: jczech@psc.edu

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

This guide was last updated |today|.
