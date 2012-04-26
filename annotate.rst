.. _annotate:

*********************************************
Annotate the MDL
*********************************************

Open **intro.mdl** with your favorite text editor (try gedit or kedit if you aren't sure what to use).

- `Examining the MDL`_
- `Initialization Commands`_
- `Molecule Definitions`_
- Reactions_
- `Reaction Directionality`_
- `Release Sites`_
- `Reaction Data`_

.. _examine_mdl:

Examining the MDL
---------------------------------------------

Before we start making changes, let's *briefly* look at what we have to start with::

    iterations = 1
    time_step = 1e-6
    ITERATIONS = iterations
    TIME_STEP = time_step

    INCLUDE_FILE = "./intro_Cube.mdl"

    INSTANTIATE World OBJECT {
        Cube OBJECT Cube{}
    }

    VIZ_OUTPUT {
        FILENAME = "tutorial"
        MOLECULES {
            NAME_LIST {ALL_MOLECULES}
            ITERATION_NUMBERS {ALL_DATA @ ALL_ITERATIONS}
        }
        MESHES {
            NAME_LIST {ALL_MESHES}
            ITERATION_NUMBERS {ALL_DATA @ [1]}
        }
    }

The first four lines are some `Initialization Commands`_ that we'll cover in the next section.

:index:`\ <single:INCLUDE_FILE>` **INCLUDE_FILE** commands let you break up MDLs into multiple sections. In this particular instance, the vertices and faces that make up our **Cube** are being imported or *included*.

In addition to simply *including* meshes, you also have to :index:`\ <single:INSTANTIATE>` **INSTANTIATE** meshes to make them exist and interact in the simulation. We'll see later that we can also instantiate other types of objects, like molecule `Release Sites`_.

Lastly, the :index:`\ <single:VIZ_OUTPUT>` **VIZ_OUTPUT** section specifies what visualization data to export and at what time values. Right now, it is set to export everything. 

.. _init_commands:

Initialization Commands
---------------------------------------------
:index:`\ <single:TIME_STEP>`
:index:`\ <single:ITERATIONS>`
At the beginning of the mdl, there are two variables **time_step** and **iterations**. These variables are applied to the initialization commands  **TIME_STEP** and **ITERATIONS** respectively. As the names imply, these commands control how many **ITERATIONS** the simulation runs for, with each iteration lasting one **TIME_STEP** (units are seconds). 

At the beginning of the mdl, change **iterations** from **1** to **1000** and **time_step** from **1e-6** to **5e-6**. This means that the simulation will run for 1000 iterations at a time step of **5e-6** seconds (total time: 1000*5e-6=5e-3 seconds).

::

    iterations = 1000
    time_step = 5e-6
    ITERATIONS = iterations
    TIME_STEP = time_step

.. _molec_def:

Molecule Definitions
---------------------------------------------
Molecules need to be defined before they are used (as a release site or a reaction) in the MDL.

:index:`\ <single:DEFINE_MOLECULES>`
After the **INCLUDE_FILE** command, add a **DEFINE_MOLECULES** section as shown here::

    DEFINE_MOLECULES {
        vol1 {DIFFUSION_CONSTANT_3D = 1E-6}
        vol2 {DIFFUSION_CONSTANT_3D = 1E-6}
        surf1 {DIFFUSION_CONSTANT_2D = 1E-7}
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
Surface molecules have a `\ <single:TOP>` **TOP** and a `\ <single:BOTTOM>` **BOTTOM**, so we need a way to differentiate between reactions that happen on one side versus the other. Commas (**,**), ticks (**'**), and semi-colons (**;**) serve this purpose. For detailed information on this reaction syntax, please refer to this pdf_. Let's look at a relatively simple example. First, add this code after the **DEFINE_MOLECULES** section::

    DEFINE_REACTIONS {
        vol1, + surf1' -> surf1' + vol2' [1E8]
    }

.. _pdf: http://mcell.psc.edu/download/files/MCell3_rxns_06_18_2007.pdf

Read this next section carefully, as some people find this syntax confusing at first. If a volume molecule and a surface molecule have their orientations *opposed* (i.e. a tick and a comma), then the volume molecule interacts with the **BOTTOM** of the surface molecule. If a volume molecule and a surface molecule have their orientations *aligned* (i.e. two ticks *or* two commas), then the volume molecule interacts with the **TOP** of the surface molecule. 

For this reaction, **vol1** and **surf1** are opposed (a comma and a tick), and **vol2** and **surf1** are aligned (two ticks). This means that **vol1** will react with the **BOTTOM** of **surf1**, creating **vol2** at the **TOP** of **surf1**. Since **vol1** is not on the products side, it is destroyed when it reacts with **surf1**. Conversely, **surf1** is on both the **reactant** and **product** side, so it will not be destroyed from the reaction.

The directionality of these ticks and commas are relative, which means that we could flip the signs and get the same result, like this::

    DEFINE_REACTIONS {
        vol1' + surf1, -> surf1, + vol2, [1E8]
    }

.. _rel_sites:

.. index::
   single: RELEASE_SITES

Release Sites
---------------------------------------------

*Modify* the **INSTANTIATE** section of the MDL so it looks like this::

    INSTANTIATE World OBJECT {
        Cube OBJECT Cube{}
        vol1_rel RELEASE_SITE {
            SHAPE = World.Cube
            MOLECULE = vol1
            NUMBER_TO_RELEASE = 2000
        }
        surf1_rel RELEASE_SITE {
            SHAPE = World.Cube[top]
            MOLECULE = surf1'
            NUMBER_TO_RELEASE = 2000
        }
    }

*Note*: Don't just add this section in or you will have two **INSTANTIATE** sections.

This section creates two release sites, one called **vol1_rel** and the other **surf1_rel**. Each release site can take a number of different commands. 

The **SHAPE** of the release determines what object (or region of an object) that molecules are released onto or into. You can also use some predefined shapes, like **CUBIC** or **SPHERICAL**, but we won't cover that here.

**MOLECULE** determines what molecule is released. If it is a surface molecule, an orientation is also specified This is similar to what's described in `Reaction Directionality`_, but it is not relative. A tick means that the **TOP** of the molecule is aligned with the **FRONT** of the surface, and a comma means that the **TOP** is aligned with the **BACK** of the surface.

**NUMBER_TO_RELEASE** gives an absolute number of molecules to be released. Alternatively, one could define a **CONCENTRATION** or **DENSITY**.

These two release sites together will release 1000 **vol1** molecules randomly throughout the inside of **World.Cube** and also 5000 **surf1** molecules randomly on the **top** surface region of **World.Cube**. Also, the **TOP** of **surf1** will be aligned with the **FRONT** of the surface.

.. _rxn_data:

.. index::
   single: REACTION_DATA_OUTPUT

Reaction Data
---------------------------------------------

At the end of the MDL, add the following::

    REACTION_DATA_OUTPUT {
        STEP=time_step
        {COUNT[vol1,WORLD]}=> "./react_data/vol1.dat"
        {COUNT[vol2,WORLD]}=> "./react_data/vol2.dat"
    }

The **STEP** command tells MCell how often it should write out reaction data.

The brackets after the **COUNT** command tell MCell what molecule to count and where to count it. For instance the first **COUNT** statement tells it to count all of the **vol1** molecules in the **WORLD** (the entire simulation). Alternatively, you could specify that it only count those found in/on an object/region (e.g. **[vol1,World.Cube]**) 

The file listed after the arrow symbol (**=>**) tells it where to save it. 

