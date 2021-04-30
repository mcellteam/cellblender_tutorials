.. _lipid_raft:

===============
Lipid Raft Model
===============

Description
===========
In this example we emulate the formation of lipid rafts in a membrane. Using three types of surface molecules (**Rf**, **Rs**, and **chol**). Initially only **Rf** and **chol** are present and after their interaction **Rs** molecules are created (reaction **Rf** + **chol** -> **Rs** + **chol**). The lipid rafts are formed due to the slow diffusion of **Rs** molecules and a reflective surface class associated with **chol** molecules.

Demonstrated features
=====================

- Reactions between surface molecules.
- A reflective surface class is used to limit diffusion of one specific surface molecule to a limited region.
- Release of a defined number of molecules.
