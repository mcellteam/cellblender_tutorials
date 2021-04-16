.. _fceri_mcell:

===============
FCERI MCell rule Model
===============

Description
===========
This example illustrates the implemenation of a BioNetGen model in MCell. As in BioNetGen molecules have components and states, here volume molecule **Lig** has two components **l** and **l**, surface molecule **Lyn** has two components **U** and **SH2**, volume molecule **Syk** has three components, **tSH2**, **l** and **a**, and components **l** and **a** can be in two states **Y** and **pY**, and finally surface molecule **Rec** has three components **a**, **b** and **g**, and component **b** and **g** can be in two states **Y** and **pY**. In BioNetGen notation this is written as **Lig(l,l)**, **Lyn(U, SH2)**, **Syk(tSH2,l~Y~pY,a~Y~pY)** and **Rec(a,b~y~pY,g~Y~Py)**. Complexes can be formed by linking two componens, for instance, molecules **Rec(a)** and **Lig(l,l)** form a complex throught the reaction **Rec(a)** + **Lig(l,l)** -> **Rec(a!1).Lig(l!1,l)**. Several reactions can occur in this example, see the tab reactions in the CellBlender model to view all of them. Complexes can also react, for instance **Lig(l!1,l!2).Lyn(U!3,SH2).Rec(a!2,b~Y!3).Rec(a!1,g~pY!4).Syk(tSH2!4,l~Y)** can form **Lig(l!1,l!2).Lyn(U!3,SH2).Rec(a!2,b~Y!3).Rec(a!1,g~pY!4).Syk(tSH2!4,l~pY)** where the component **Syk(tSH2!4,l~Y)** change to state **Syk(tSH2!4,l~pY)**.


.. link to more where all this is explained in detailed.
.. Jim uses different notation for the Y and pY in his presentations U and P.

Demonstrated features
=====================

- Import of a BioNetGen example in MCell.
- Definition of molecules with components and states.
- Reactions with absolute orientation.
- Usage of BioNetGen compartments.
- Complexes are formed.
- Count complexes.
