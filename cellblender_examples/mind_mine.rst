.. _mind_mine:

===============
MinD/MinE System model
===============

Description
===========
This example recreates the MiN system in E. coli, where three proteins MinC, MinE and MinD are used to localize the septum prior to cell division. Further details of the model can be found here_ .
Volume molecules **mind** with a bound adp molecule (**mind_adp**) can phosphorylate to **mind_atp**, through the reaction **mind_adp** -> **mind_atp**. mind proteins in the atp-bound conformation (**mind_atp**) can further bind to the membrane, through the reaction **mind_atp@IN** + **surf** -> **mind_m**, where surf represent a surface class associated to the membrane. A number of other reactions also occur, that generates oscillating clusters of surface molecules **mind_m** and **mine_m** on the membrane.

.. _here: https://www.pnas.org/content/103/2/347.short

Demonstrated features
=====================

- Interaction between volume molecules and a surface class associated with the membrane of an object.
