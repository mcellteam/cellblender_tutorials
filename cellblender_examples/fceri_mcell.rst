.. _fceri_mcell:

===============
FCERI MCell rule Model
===============

Description
===========
This example illustrates the implementation of a BioNetGen model in MCell (details of the model can be found  `here <https://www.jimmunol.org/content/170/7/3769>`__.). As in BioNetGen molecules can have components and states, here volume molecules **Lig** have two components **l** and **l**, surface molecules **Lyn** have two components **U** and **SH2**, volume molecules **Syk** have three components, **tSH2**, **l** and **a**, and components **l** and **a** can be in two states **Y** and **pY**, and finally surface molecules **Rec** have three components **a**, **b** and **g**, and components **b** and **g** can be in two states **Y** and **pY**. In BioNetGen notation this is written as **Lig(l,l)**, **Lyn(U, SH2)**, **Syk(tSH2,l~Y~pY,a~Y~pY)** and **Rec(a,b~y~pY,g~Y~Py)**. Complexes can be formed by linking two components, for instance, molecules **Rec(a)** and **Lig(l,l)** form a complex through the reaction **Rec(a)** + **Lig(l,l)** -> **Rec(a!1).Lig(l!1,l)**. Several reactions drive the dynamic of this system, see the tab reactions in the CellBlender version of this model to find all of them. Complexes can also react, for instance **Lig(l!1,l!2).Lyn(U!3,SH2).Rec(a!2,b~Y!3).Rec(a!1,g~pY!4).Syk(tSH2!4,l~Y)** can form **Lig(l!1,l!2).Lyn(U!3,SH2).Rec(a!2,b~Y!3).Rec(a!1,g~pY!4).Syk(tSH2!4,l~pY)** where the component **Syk(tSH2!4,l~Y)** change to state **Syk(tSH2!4,l~pY)**.


.. link to more where all this is explained in detailed.
.. Jim uses different notation for the Y and pY in his presentations U and P.

Demonstrated features
=====================

- Definition of molecules with components and states as in BioNetGen.
- Reactions with absolute orientation.
- Usage of BioNetGen compartments.
- Complexes are formed.
- Count complexes.
