.. _lotka_volterra:

===============
Lotka Volterra Model
===============

Description
===========

A spatial Lotka Volterra Model is introduced in this example with a prey population that exponentially grows when not constrained and a population of predators that grows after consuming preys (details of how to implement the model in a torus are here: :ref:`lotka_volterra_torus`). Two examples are presented one in which the reaction rate limits the number of preys and predators (Reaction-Limited), and the other is an example where the diffusion coefficient limits the number of reactions (Diffusion-Limited). Both models are similar with the exception of the reaction rate constants. 


Demonstrated features
=====================

- Reactions between volume molecules.
- Usage of the NULL function in a reaction.
