===============
Organelle Model
===============


Description
===========

In this example we show the interaction between volume and surface molecules, and how through their interactions they can be transported to different compartments and new molecules are created. Tree compartments are considered: a cell with two organelles inside. Two volume molecules **a** and **b** are initially placed, molecules **a** inside the cell and molecule **b** inside organelle 1. Surface molecules **t1** and **t2** are initially placed in a small area of organelle 1 and 2 respectively. Through their interactions with **t1** surface molecules, some **a** molecules are transported inside organelle 1 (reaction **a**' + **t1**' -> **a**, + **t1**'), where they can further interact with molecule **b** to create volume molecules **c** (reaction **a** + **b** -> **c**). **c** molecules can be translocated to the interior of the cell through their reaction with surface molecules **t1** (reaction **c**,+ **t1**' -> **c**' + **t1**,) where they can additionally interact with surface molecules **t2**, and create volume molecules **d** inside organelle 2 (reaction **c**' + **t2**' -> **d**, + **t2**').


Demonstrated features
=====================

- Reactions between volume molecules.
- Reactions between surface and volume molecules with transport.
- Release of surface and volume molecules in specific compartments and regions.
