.. _lotka_volterra:

*********************************************
Lotka-Volterra in an Unconventional Space
*********************************************

This tutorial uses the `Lotka-Volterra`_ oscillating system to demonstrate the
difference between a diffusion-limited reaction and an actual physiologic
reaction. The project files for the following two examples are available here_.

.. _Lotka-Volterra: https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equation

.. _here: http://mcell.org/tutorials/downloads/LV.tgz

Diffusion-Limited Reaction
---------------------------------------------

A diffusion-limited reaction is a reaction which occurs whenever the species
meet. In other words, the probability of reaction is 1 (or greater), and the
only parameter limiting the reactions occurrence is the availability of the
reactant species (and how often they meet). In the MDL syntax, this effect is
achieved by making the rate constant so high as to push the probability of
reaction to be greater than 1. Running with a small starting number of
molecules from a point allows this model to show a firework pattern of the two
oscillating species (B and C) as they move through the tube. If you look at the
reaction data, there are no smooth regular oscillations as seen in the
physiologic model.

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/lv/diff_lim_sm.png

Physiologic Reaction
---------------------------------------------

This is the same model as the diffusion-limited reaction except that it starts
from well mixed conditions and the probabilities for the reactions are not
greater than 1. Now, the visualization will show the molecules changing
throughout the entire system (the tube will slowly change from B to C and
back). In the reaction data the oscillations will be smooth and regular (and
will closely match an ODE model given that this reaction adheres to well mixed
conditions).

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/lv/red_sm.png

.. image:: http://www.mcell.psc.edu/tutorials/tutimg/lv/green_sm.png
