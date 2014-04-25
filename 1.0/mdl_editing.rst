.. _editing_mdls:

Editing MDLs and Analysis with Python
---------------------------------------------

MCell can be thought of as a simulation engine for CellBlender. In other words,
after you design your model in CellBlender, it is MCell which actually carries
out the simulation itself (i.e. the diffusion and reaction of molecules). And
MDL (Model Description Language) is the file format which MCell uses. With the
help of CellBlender, some users may never need to hand-edit an MDL or even know
that they exist. But for the users who need that extra flexibility and control,
editing MDLs or even writing them from scratch can be invaluable. And for those
with a programming background, the syntax might be familiar as it shares some
similarities with C-style languages. Don't worry if you are not a programmer
however; MDL is not that difficult to understand. The first example here will
examine the MDLs that were created way back in :ref:`getting_started`. From
there, we will move onto some other advanced concepts like checkpointing.
Finally, we will end this section by showing how to do some simple analysis
using Python and matplotlib.

.. note::

   It is assumed that you have already gone through tutorials 1-4 prior to
   attempting these.

.. toctree::

   examine_mdls
   checkpointing
   seed
   analyze
