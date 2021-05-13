.. _lr_cbngl_mcell:

===============
LR CBNGL MCell Rules model
===============

Description
===========
In this example reactions between molecules with a specific number of bonds is introduced. Volume molecules **L** have three components **r** , **r** , **r** and volume molecules **V** have two components **l** and **l**.  Volume molecules **L** have three components **r** , **r** and **r**. Volume molecules **R** with one unbound components can react with volume molecules **L** with three unbound components to form a complex with one bond (through the following equation **R(l)** + **L(r,r,r)** -> **L(r!1,r,r).R(l!1)**). Furthermore, volume molecules **R(r)** with one unbound state can react with volume molecules **L(r,r,r!+)** with one bound state to generate with two bound states (through the reaction **R(l)** + **L(r,r,r!+)** -> L(r!1,r,r!+).R(l!1)). Finally volume molecule **L(r,r!+,r!+)** with two bound states can react with one volume molecule **R(l)** with one unbound state to form a complex **L(r!1,r!+,r!+).R(l!1)** (through the reaction **R(l)** + **L(r,r!+,r!+)** -> **L(r!1,r!+,r!+).R(l!1)**).


Demonstrated features
=====================

- Definition of molecules with components and states.
- Usage of BioNetGen compartments.
- Complexes are formed.
- Usage of bound states (!+) in reactions from BioNetGen notation.
