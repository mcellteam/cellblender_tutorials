.. _annotate:

*********************************************
Examining and Annotating the MDL
*********************************************

.. contents:: :local:


.. _examine_mdl:

Examining the Main MDL
---------------------------------------------

To start out with, open **intro.main.mdl** with your favorite text editor (try gedit or kedit if you aren't sure what to use)::

    ITERATIONS = 1000
    TIME_STEP = 1e-06

    INCLUDE_FILE = "intro.molecules.mdl"

    INCLUDE_FILE = "intro.reactions.mdl"

    INCLUDE_FILE = "intro.geometry.mdl"

    INSTANTIATE Scene OBJECT
    {
      Cube OBJECT Cube {}
      vol1_rel RELEASE_SITE
      {
       SHAPE = Scene.Cube
       MOLECULE = vol1
       NUMBER_TO_RELEASE = 2000
       RELEASE_PROBABILITY = 1
      }
      surf1_rel RELEASE_SITE
      {
       SHAPE = Scene.Cube[top]
       MOLECULE = surf1'
       NUMBER_TO_RELEASE = 2000
       RELEASE_PROBABILITY = 1
      }
    }

The first two lines are :ref:`init_commands` that we'll cover in the next section.

:index:`\ <single:INCLUDE_FILE>` **INCLUDE_FILE** commands let you break up MDLs into multiple sections. **intro.molecules.mdl** contains molecule definitions, **intro.reactions.mdl** contains reaction definitions, and **intro.geometry.mdl** contains the the vertices and faces that make up our **Cube**.

In addition to simply *including* meshes, you also have to :index:`\ <single:INSTANTIATE>` **INSTANTIATE** meshes to make them exist and interact in the simulation. Later, we'll talk about instantiating other types of objects, like molecule :ref:`rel_sites`.

.. _init_commands:

Initialization Commands
---------------------------------------------
:index:`\ <single:TIME_STEP>`
:index:`\ <single:ITERATIONS>`
At the beginning of the file are the initialization commands, **TIME_STEP** and **ITERATIONS**. As the names imply, these commands control how many **ITERATIONS** the simulation runs for, with each iteration lasting one **TIME_STEP** (units are seconds). 

Notice that **ITERATIONSu** is set to **1000** and **TIME_STEP** to **5e-6**. This means that the simulation will run for 1000 iterations at a time step of **5e-6** seconds (total time: 1000*5e-6=5e-3 seconds).

.. _molec_def:

Geometry Files
---------------------------------------------

Let's take a closer look at **intro.geometry.mdl**::

    Cube POLYGON_LIST
    {
      VERTEX_LIST
      {
        [ 1, 0.999999940395355, -1 ]
        [ 1, -1, -1 ]
        [ -1.00000011920929, -0.999999821186066, -1 ]
        [ -0.999999642372131, 1.00000035762787, -1 ]
        [ 1.00000047683716, 0.999999463558197, 1 ]
        [ 0.999999344348907, -1.00000059604645, 1 ]
        [ -1.00000035762787, -0.999999642372131, 1 ]
        [ -0.999999940395355, 1, 1 ]
      }
      ELEMENT_CONNECTIONS
      {
        [ 4, 0, 3 ]
        [ 4, 3, 7 ]
        [ 2, 6, 7 ]
        [ 2, 7, 3 ]
        [ 1, 5, 2 ]
        [ 5, 6, 2 ]
        [ 0, 4, 1 ]
        [ 4, 5, 1 ]
        [ 4, 7, 5 ]
        [ 7, 6, 5 ]
        [ 0, 1, 2 ]
        [ 0, 2, 3 ]
      }
      DEFINE_SURFACE_REGIONS
      {
        top
        {
          ELEMENT_LIST = [1, 8, 9]
        }
      }
    }

Mesh objects made in Blender become a **POLYGON_LIST** object in MCell. A **POLYGON_LIST** object consists of two to three sections in MCell: a **VERTEX_LIST**, an **ELEMENT_CONNECTIONS** list, and a **DEFINE_SURFACE_REGIONS** section. A **VERTEX_LIST** is exactly what it sounds like, a list of vertices. The **ELEMENT_CONNECTIONS** list defines the faces of the triangles. Each number in the list is an index to a single vertex defined in the **VERTEX_LIST**. Each set of three numbers (e.g. **[ 0, 1, 2 ]**) tells which vertices are connected together to form a single face. **DEFINE_SURFACE_REGIONS** is optional, unless you want to specify specify surface regions. Each number in the **ELEMENT_LIST** is an index to a triangle in **ELEMENT_CONNECTIONS**.

Molecule Definitions
---------------------------------------------

Molecules need to be defined before they are used (as a release site or a reaction) in the MDL.

:index:`\ <single:DEFINE_MOLECULES>`

Open the **intro.molecules.mdl** file, and you'll see the following::

    DEFINE_MOLECULES
    {
      vol1
      {
        DIFFUSION_CONSTANT_3D = 1e-06
      }
      vol2
      {
        DIFFUSION_CONSTANT_3D = 1e-06
      }
      surf1
      {
        DIFFUSION_CONSTANT_2D = 1e-07
      }
    }

:index:`\ <single:DIFFUSION_CONSTANT_3D>`
:index:`\ <single:DIFFUSION_CONSTANT_2D>`
Molecules that use **DIFFUSION_CONSTANT_3D** command, like **vol1** and **vol2**, will be volume molecules, meaning that they will exist in solution. Molecules that use **DIFFUSION_CONSTANT_2D**, like **surf1**, will be surface molecules, meaning that they exist on a surface. The units of the values assigned to this command (**1E-6** and **1E-7** in this instance) are in cm\ :sup:`2`\ /s. 

.. _reactions:

Reactions
---------------------------------------------
Molecules that were defined in the previous section can be created and destroyed in a number of different ways using reactions. A reaction is defined in the following manner:

**reactant(s) -> product(s) [rate]**

This means that **reactant(s)** are converted into **product(s)** at a given **rate**.

There must be one or more molecules on the left hand  **reactants** side. On the right hand **products** side, you must have zero (`\ <single:NULL>` **NULL**) or more molecules. The units of the **rate** depend on the type of reaction. [s\ :sup:`-1`\ ] for unimolecular reactions and [M\ :sup:`-1`\ s\ :sup:`-1`\ ] for bimolecular reactions between two volume molecules or a volume molecule and a surface molecule.

.. _rxn_dir:

Reaction Directionality
---------------------------------------------

:index:`\ <single:DEFINE_REACTIONS>`
Surface molecules have a `\ <single:TOP>` **TOP** and a `\ <single:BOTTOM>` **BOTTOM**, so we need a way to differentiate between reactions that happen on one side versus the other. Commas (**,**), ticks (**'**), and semi-colons (**;**) serve this purpose. For detailed information on this reaction syntax, please refer to this pdf_. Let's look at the relatively simple example we have created in **intro.reactions.mdl**::

    DEFINE_REACTIONS
    {
      vol1' + surf1, -> surf1, + vol2, [1e+08]
    }

.. _pdf: http://mcell.psc.edu/download/files/MCell3_rxns_06_18_2007.pdf

Read this next section carefully, as some people find this syntax confusing at first. If a volume molecule and a surface molecule have their orientations *opposed* (i.e. a tick and a comma), then the volume molecule interacts with the **BOTTOM** of the surface molecule. If a volume molecule and a surface molecule have their orientations *aligned* (i.e. two ticks *or* two commas), then the volume molecule interacts with the **TOP** of the surface molecule. 

For this reaction, **vol1** and **surf1** are opposed (a comma and a tick), and **vol2** and **surf1** are aligned (two ticks). This means that **vol1** will react with the **BOTTOM** of **surf1**, creating **vol2** at the **TOP** of **surf1**. Since **vol1** is not on the products side, it is destroyed when it reacts with **surf1**. Conversely, **surf1** is on both the **reactant** and **product** side, so it will not be destroyed from the reaction.

The directionality of these ticks and commas are relative, which means that we could flip the signs and get the same result, like this::
    
    DEFINE_REACTIONS
    {
      vol1, + surf1' -> surf1' + vol2' [1e+08]
    }

.. index::
   single: RELEASE_SITES

.. _rel_sites:

Release Sites
---------------------------------------------

Let's examine the **INSTANTIATE** section of **intro.main.mdl** more closely::

    INSTANTIATE Scene OBJECT
    {
      Cube OBJECT Cube {}
      vol1_rel RELEASE_SITE
      {
       SHAPE = Scene.Cube
       MOLECULE = vol1
       NUMBER_TO_RELEASE = 2000
       RELEASE_PROBABILITY = 1
      }
      surf1_rel RELEASE_SITE
      {
       SHAPE = Scene.Cube[top]
       MOLECULE = surf1'
       NUMBER_TO_RELEASE = 2000
       RELEASE_PROBABILITY = 1
      }
    }

This section creates two release sites, one called **vol1_rel** and the other **surf1_rel**. Each release site can take a number of different commands. 

The **SHAPE** of the release determines what object (or region of an object) that molecules are released onto or into. You can also use some predefined shapes, like **CUBIC** or **SPHERICAL**, but we won't cover that here.

**MOLECULE** determines what molecule is released. If it is a surface molecule, an orientation is also specified This is similar to what's described in :ref:`rxn_dir`, but it is not relative. A tick means that the **TOP** of the molecule is aligned with the **FRONT** of the surface, and a comma means that the **TOP** is aligned with the **BACK** of the surface.

**NUMBER_TO_RELEASE** gives an absolute number of molecules to be released. Alternatively, one could define a **CONCENTRATION** or **DENSITY**.

These two release sites together will release 1000 **vol1** molecules randomly throughout the inside of **World.Cube** and also 5000 **surf1** molecules randomly on the **top** surface region of **World.Cube**. Also, the **TOP** of **surf1** will be aligned with the **FRONT** of the surface.


.. index::
   single: REACTION_DATA_OUTPUT

.. _rxn_data:

Visualization Data
---------------------------------------------

For these last two sections, we'll actually be hand editing some mdls. First, create a file called **intro.viz_output.mdl** with the following text in it::

    VIZ_OUTPUT {
        MODE = ASCII
        FILENAME = "./viz_data/intro"
        MOLECULES 
        {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }   
    }

The :index:`\ <single:VIZ_OUTPUT>` **VIZ_OUTPUT** section specifies what visualization data to export and at what time values. Right now, it is set to export everything. 

Reaction Data
---------------------------------------------

Now, create a file called **intro.viz_output.mdl**::

    REACTION_DATA_OUTPUT
    {
        STEP=time_step
        {COUNT[vol1,WORLD]}=> "./react_data/vol1.dat"
        {COUNT[vol2,WORLD]}=> "./react_data/vol2.dat"
    }

The **STEP** command tells MCell how often it should write out reaction data.

The brackets after the **COUNT** command tell MCell what molecule to count and where to count it. For instance the first **COUNT** statement tells it to count all of the **vol1** molecules in the **WORLD** (the entire simulation). Alternatively, you could specify that it only count those found in/on an object/region (e.g. **[vol1,World.Cube]**) 

The file listed after the arrow symbol (**=>**) tells it where to save it. 

.. _run_sim:

Run the Simulation
---------------------------------------------

At the command line, navigate to the appropriate directory (``cd /home/user/mcell_tutorial/intro`` where **user** is your user name), and enter the command:: 

    mcell intro.mdl

MCell should output some information to the command line indicating that it ran successfully.

At the command line, type::

    ls

You should notice that we have created four new files: **intro.main.mdl**, **intro.geometry.mdl**, **intro.molecules.mdl**, and **intro.reactions.mdl**. We will take a look at all of these in turn.
