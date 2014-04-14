.. _CellOrganelle12:

**************************************************
CellBlender Tutorial - Simple Cell with Organelles
**************************************************

Introduction to Simple Cell Model:
---------------------------------------------

This tutorial will introduce CellBlender, a cellular microphysiology modeling tool
that aims to simplify the construction of realistic biological models of biochemistry in cells,
including the construction of cellular anatomy, definition of both freely diffusing and
membranebound biomolecules, and definition of reaction pathways.

In this tutorial we will build a simple model that uses many of CellBlender’s features. As shown below,
the model is a simple cell with two organelles, Organelle 1 and 2, each adorned respectively with
transporter molecules T1 and T2. A freely diffusing molecule ‘A’ is released uniformly throughout
the cytoplasm, which reacts with t1 to cross the membrane of Organelle 1. Another freely
diffusing molecule ‘B’ is uniformly released within Organelle 1, and reacts with molecule ‘A’ to
produce molecule ‘C’. Note that because ‘A’, ‘B’, and ‘C’ can’t penetrate the organelle
membranes, they will only cross over through a transporter molecule reaction. After ‘C’ is
produced, it can react with transporter t1 to be moved into the cytoplasm. Here ‘C’ will diffuse
freely until it meets transporter t2, at which point it can be transported across the membrane and
become isolated in Organelle 2. Because all the reactions are irreversible, this reaction will
eventually lead to the extinction of molecule ‘A’ and accumulation of molecule ‘C’ in organelle 2.
Although this isn’t a model of a known biochemical process, the transport of molecules across a
membrane is ubiquitous, and similar reaction pathways occur in the nucleus, mitochondria, and
endoplasmic reticulum.

.. image:: ./organelle_images/cellmodel_s.gif

CellBlender Setup
---------------------------------------------

Before we begin the actual tutorial that we just outlined, we need to start and set up Blender so the
CellBlender plugin is enabled. It can sometimes be helpful to use the **File/Load-Factory-Settings** command
to ensure that your version of Blender is in its default condition before starting.



We install CellBlender by choosing **User-Preferences** under the **File** menu, selecting
the **Addons** option, choosing the **Cell Modeling** option, and clicking on the CellBlender check box
to enable it. Then close the **Addon** dialog box and choose **File/Save-Startup-File** so that CellBlender
will be enabled every time you restart Blender.

To verify that CellBlender is enabled, lets click on the scene tab of the properties
panel:


.. image:: ./organelle_images/properties_panel_scene.png

Then collapse all subpanels in the properties panel by clicking the little triangles to the left
of each subpanel. The resulting scene panel should look like this:

.. image:: ./organelle_images/scene_panel_all_closed.png

You'll notice the standard Blender subpanels listed from the top (Scene, Units, Keying Sets, ...)
down to the "Custom Properties" subpanel. The remainder of the subpanels should all begin with
the word "CellBlender", and these are the subpanels we'll be using the most. When using subpanels,
it can be easy to get lost. So it's a good practice to close each subpanel when you're done with it.
If you like, this might be a good time to open each subpanel, take a look at it, and then close it
again.

The next thing we need to do is customize the screen so it's more convenient for cell modeling.
The first thing we'll do is eliminate the outline panel, because its too small, and create a larger
one by duplicating the 3dview window, dragging it over until we have a narrow panel, which we can convert into an
Outliner panel. Then to make this the default, we save this as the startup file. With this saved as
the startup file, we can now quit Blender, and restart Blender and reveal that this is now the
default layout.

Attempt to clean up, need your input!:
---------------------------------------------

Before we begin building the model we outlined, we need to set up Blender so the CellBlender
addon is enabled. Under the file menu, choose user preferences and select the Addons panel.
From the list on the left hand side select Cell Modeling, and then check the box next to
CellBlender to enable it. Click Save User Settings. To verify the installation, lets click on the
scene tab of the properties panel. We can collapse any unneeded panels, and note that a series
of CellBlender panels are now listed. The next thing we need to do is customize the screen so its
more convenient for cell modeling. The outline panel is too small, so we’ll eliminate this one, and
create a larger one by duplicating the 3dview window, dragging across to make a pair of windows
with a larger one in the center for viewing, and convert the narrower left hand window into a
Outline panel. In order to make this setup the default every time you start Blender, under the file
menu click Save this as the startup file. With this saved, we can now quit Blender, and restart
Blender into the new default layout.

Restart Blender (02:10:00)
---------------------------------------------

We are now ready to begin our modeling project. The first thing we need to do is delete the cube.
Select the cube, and hit the ‘x’ key to delete it. The next thing we will do is create an Icosphere.
Zoom in to see it better. Change its radius to 0.625 microns and increase the number of
subdivisions to make it a better approximation of a sphere. We're going to crank up the number
of subdivisions to 5, which makes a fairly smooth looking sphere. We zoom in to see it better.
But we are also going to be creating organelles inside this object. First we rename the object
Cell by clicking on the name in the outliner and renaming. And then we are going to make this
view a wireframe view so we can see inside the icosphere better. Another way to add new
meshes to the scene is to use the spacebar, and then type in the name of a command, such as
"Add Icosphere", and then hit enter and we get an icosphere the same size as the previous one
so it looks like its on top, but if we change its radius to 0.3 microns we can see that its small and
inside the cell icosphere. When moving and manipulating objects for design of a scene, its most
convenient to use orthographic mode, which is done by selecting orthographic from the view.
Then, you can click on the small arrows associated with the object and drag to move in the
desired direction. We are adding another Icosphere, by default it comes up with the same radius
as the most recently created one, we are going to change its radius to 0.2 now, and drag this
slightly off center to the other side. We've now created 2 new Icospheres, and you can see in the
outliner that they've been named Icosphere and Icosphere.001, now change Icosphere to
Organelle_1 and the other icosphere to Organelle_2. Lets now rotate the scene so we can see
the relationship between the cell and its two organelles.

We are now ready to begin our modeling project. Blender will startup with a cube in the center,
but we won’t be using this for our model, so we delete the cube by selecting the cube with the
right mouse button and hit the ‘x’ key to delete it. The next thing we need to do is create an
Icosphere from the add mesh submenu. This will represent our cell. Using the middle mouse
wheel, we can zoom in to get a better look. On the left hand tool panel, change the radius to
0.625 microns and the increase the number of subdivisions to make it a better approximation of
a sphere. We’re going to crank up the number of subdivisions to 5, which makes a fairly smooth
looking sphere. We could make a more realistic cell using imaging data of real cells, but we’ll
stick with our smooth sphere, and label it Cell by clicking on the name in the Outliner. In order to
see the organelles we are going to put inside the cell, we select the wireframe view mode by
selecting it from the menu at the bottom of the 3dview window. Hitting the ‘z’ button on the
keyboard will also toggle the view mode between wireframe and solid mode. When adding our
organelle, instead of using the menus, we hit the spacebar and type in the name of a command,
such as “Add Icosphere”, and then hit enter to place another Icosphere with the same
dimensions as the previous. We can see that this is a new object by changing the radius to 0.3
microns. We’re going to move this organelle, but first go to the view menu towards the bottom,
and click Use Orthographic Mode. This is a more convenient viewpoint when manipulating 3d
objects. With this view, we left click one of the arrows at the base of the object and drag to our
desired position. We add another Icosphere, change the radius to 0.2, and drag to the other side
of the cell. We now change the names of our new Icospheres to Organelle_1 and Organelle_2.
We can now rotate around the cell to see the relationship between the organelles and the cell.
Before moving on, make sure both organelles are inside the cell, but not overlapping.

Geometry Complete (06:07:18)
---------------------------------------------

Save Model (06:46:14)
---------------------------------------------

After you've made several changes to a scene its useful to save. Select save from the file menu,
you now get a file system navigator. Navigate to the directory you'd like to store the project, name
the project, in this case demo.blend, and click save blender file. You only need to name the
project and blender file the first time you save, after that typing ‘cntrl s’ on the keyboard will cause
an automatic save. The next thing we need to do is configure the project as a cell blender
project. Under the CellBlender Project Setup choose set the project directory, navigate to the
directory you would like the project to live, select that directory, and then change the name of the
project basename to the desired name, in this case demo, and then save. This step turns the
project into a CellBlender project.
At this point its a good idea to save. Select save from the file menu to bring up a file system
navigator. Navigate to the working directory where you’d like to store the projects, and give it a
name, in this case demo.blend, and click Save Blender File. The familiar ‘Cntrl s’ keyboard
shortcut will save our project under this name, which is a good idea to do frequently. The next
thing we need to do is configure the project as a CellBlender project. Under the CellBlender
Project Setup click on Set the Project Directory, and navigate to the working directory where you
would like the project to live, and select the directory. Change the Project Basename to the
desired name, in this case demo, and then save. This step turns the project into a CellBlender
project.

Prepare to add regions (08:27:05)
---------------------------------------------

The next thing we are going to do is create regions on the two organelles, this is best done by
making the objects appear solid, but when we do the cell now obscures the scene, so we need
to make it invisible. Next we choose organelle number 1, and to make it the center of rotation you
choose the object and then say view selected, to make the other organelle be the center of
rotation, choose that object and select view selected under the view menu. This is a very
convenient way to switch back and forth between editing of different objects. Next we switch into
edit mode so that we can create a surface region on this organelle. The tab key also switches
between object mode and edit mode. Object mode is used for manipulating sepeparate object
within the scene, and edit mode is used for manipulating polygons and vertices and faces of a
given object. In edit mode, by default a newly created object has all of its vertices selected. The
a key on the keyboard toggles between select and unselect of all the vertices in the object. The
hotkey for select all and deslect all can be seen in the menu, but to create regions on the object
which are collections of faces, we need to switch into face select mode, which is done by using
one of the three tabs at the bottom of the 3dview window. In face select mode the polygons have
little square handles that can be seen. We next switch to the objects property panel, and at the
bottom you can see the define surface regions CellBlender panel. We create a new region by
clicking on the plus button and then changingt the name of that region, in this case calling it
t1_region. To create our region, we can use the circular paintbrush by typing the c key on the
keyboard. Or we can choose it from the menu. In which case we get a circular shaped
paintbrush, adn the scroll weheel on the mouse lets you select the size of the paintbrush. And
then left click and drag lets you sweep out like a spraycan. And select faces. Then to make these
faces a member of this region, click on the assign button under the surface regions panel. To
verify that they have been assigned, you can use the select and deselct buttons in the control
panel. This completes the region on organelle number 1, we are now ready to switch to organelle
number 2 and create a region on it. We're going to create this region on the top of the sphere, so
we rotate to look down on it, hit the tab key to go into edit mode, edit mode rembembers that we
had left it in face slect mode, we use the c key to select the cirucular paintbrush and then sweep
out and select the faces that we like. Notice in this create we didn't create the region yet, the
order doesn't really matter, we've now created the t2_region and assigned the selected polygons
to that region and verfified it using the select and deslect buttons. Next we turn the cell back on,
switch back to wireframe mode, and save.

The next thing we are going to do is create special membrane regions on the two organelles
where the transporters will be placed. Selecting regions is difficult in the wireframe view mode, so
we will switch back to solid view mode, and hide the Cell so that we work on the organelles. This
is done by clicking the Eye on the Outline panel next to the object. With the Cell hidden, we
select organelle 1 with right click, and select View Selected from the View menu, making the
center of the object the center of rotation of the view. We can do the same to organelle 2,
centering the camera on this object. This is a very convenient way to switch back and forth
between editing of different objects. Next we switch into Edit mode using the menu at the bottom,
which can also be done by pressing the Tab key. Object mode is used for manipulating separate
objects within the scene, and edit mode is used for manipulating vertices, edges and faces of a
given object. We see that all vertices are selected by default, we can toggle Select All and Select
None by pressing the ‘A’ key on the keyboard, or by using the option in the menu. Note that
almost every operation has a keyboard shortcut shown in the menu, it is helpful to learn some of
the frequently used shortcuts to speed up your model building. At the bottom of the 3dview
window there are buttons for vertex, edge and face select modes, we click on face select mode,
changing the scene to show square handles on the faces, and allowing us to choose the faces
that will make up the region we are creating. We now switch to the Objects Property Panel, and
at the bottom we expand the Define Surface Regions CellBlender panel. We create a new region
by clicking on the plus button and changing the name of the region, in this case to t1_region. To
create our region, we select the Circle Select tool from the Select menu, or by pressing the ‘C’
key on the keyboard, as shown in the menu. This gives us a circular selection tool that can be
resized using the mouse wheel. We left click and hold to select the desired region, like a
spraycan. To make these regions part of the region we created, click on the Assign button on
the Define Surface Regions panel. To verify that they have been assigned, you can use the
Select and Deselect buttons in the control panel. This completes the region on organelle 1, we
are now ready to switch to organelle 2 and create a region on it. We're going to create this region
on the top of the sphere, so we rotate to look down on it, and hit the tab key to go into edit mode.
Edit mode remembers that we had left it in face select mode, so we again use the ‘C’ key to
select the Circle Select paintbrush and then sweep out a region that we like. We create the
region in the same way and name it t2_region. We assign the selected faces to the region, and
verify the operation using the Select and Deselect buttons. Our regions are now created, so we
make the Cell visible, go back into wireframe view mode, and save.

We're now ready to begin creating the rest of the MCellCellBlender project. First we need to
select the 3 objects that we've just created, the cell, org1 and org2, and add them as model
objects under the model objects panel just hitting the plus key adds all selected objects as model
objects. This maeks those objects part of the mcell model that we will export later. Our next step
is to enable and change the simulation iterations to 20000 in this case, with a time step of 1
microsecond. The next thing we need to do is enable partitions which subdivide the space into
small cubes, which accelerates the simulation process. The default spacing of the partitions is a
little bit too fine for our purposes so we change it to be 0.05. Next we are going to define the
molecuels that we spelled out in the outline in the beginning of this tutorial. The first molecule is
molecule t1 which is the transporter which will be on org1, its a surface molecule, and its
diffusion constant will be 1x106 cm^2/s. You can see the bubble help that pops up when you
hover over any button in the user interface which gives you a hint about the purpose of the
button. Next we're going to add molecule t2, another surface molecule. T2 is immobile, so we
give it a diffusion constant of 0.

Now that our geometry is fully defined, we are ready to describe the rest of our CellBlender
model. First we need to select the 3 objects that we've just created, the Cell, Organelle 1 and
Organelle 2, and add them to the CellBlender model so the simulation recognizes the geometry
and properly exports it later when we run our simulation. With the objects selected, we go to the
Model Objects CellBlender panel and press the plus button to add them to model. Our next step
is to set simulation parameters, first changing the number of Iterations to perform, in this case
20000, with a Timestep of 1 microsecond. The next thing we need to do is edit the partitions
which subdivide the simulation space into small cubes, which accelerates the simulation
process. The default spacing of the partitions is a little bit too fine for our purposes so we change
it to be 0.05 microns. Figuring out efficient partitioning in your own projects can be a tricky
process, but only affects simulation speed, not simulation accuracy. Next we are going to define
the molecules that we spelled out in the outline in the beginning of this tutorial. The first molecule
is molecule t1 which is the transporter which will be on organelle 1, its a surface molecule, and its
diffusion constant will be 1x10^6 cm^2/s. Notice when you hover over any button in the user
interface you can see a help bubble that pops up and gives a hint about the purpose of the
button. Next we're going to add molecule t2, another surface molecule. T2 is immobile, so we
give it a diffusion constant of 0.

Finish molecule t2 (17:31:10)
---------------------------------------------

Begin Mol A (17:59:23)
---------------------------------------------

Next we add molecule a, molecule a is a volume molecule, it diffuses freely in the ctyoplasm in
the cell, its diffusion constant will be 1 times 10 to the minus 6 centimeters squared per second.
You can change the name of molecules by selecting them in the define molecules panel and
changing its name. NExt we add molecule b, another volume molecule, diffusion constant again
1e6 cm2/s. Molecule c, 1x106,
but notice we've accidentally noticed molecule c as a surface
molecule, we notice this and change it to a volume molecule as we scan over each moleucle
and double check and verify its settings. With molecules defined we're now ready to define
reactions.

Next we add molecule ‘A’, which is a volume molecule, and diffuses freely in the cytoplasm in
the cell. We set the diffusion constant to be 1x10^6 cm^2/s. Next we add molecule ‘B’, another
volume molecule, with diffusion constant again 1x10^6 cm^2/s. We repeat for molecule ‘C’, with
the same diffusion constant, but notice we've accidentally declared molecule ‘C’ as a surface
molecule, but its simple to fix and change to a volume molecule as we scan over each molecule
and verify the definitions. With all the molecules defined we're now ready to define reactions.
Hit the plus key to add a reaction, adnd in the reactants textbox type in the reaction, in this case a
on the outside plus t1 facing outward undergoes an irrevirsbile reaction to craete products a
comma means a on the inside plus t1 appostrophe means t1 still facing outwards. Forward rate
constant 3x10 to the 8th per molar per second, its a bimolecular reaction. Second reaction will
be a plus b irreversibily producing molecule c, becasue both reactants are volume reactants no
orientation marks are required when writing the reaction, rate constant 3 times 10 to the 9 per
molar per second. NExt reaction is c comma, which means c on the inside, plus t1 facing
outward irrev creates c apostoprhe meaning c on the outside plus t1 apostrophe still facing
outward, forward rate constant 3 times 10 to the 8th. Next reaction is c on the outside plus t2
facing outward irrev creates products c comma meaning c on the inside plus t2 still facing
outwards forward rate constant 3 times 10 to the 8th. Those are our reactions. Next we need to
place our molecules within their initial position within the model. This is done by creating release
sites. The first molecule we are going to release is molecule a, so lets name the release site
rel_A, releasing molecule a, moleucle a is going to be released inside an object or region, we're
going to release it inside the cell, the whole cell, but not including the two organelles, so we have
to say cell all minus the union of org 1 all and org 2 all. This creates a boolean operation that will
release the molecule a inside the cell but outside the two organelles. We're going to release a
constant number of a molecules, 1000 of them. The next release site is to place molecule b, so
lets call it rel_b, inside an object, the object we're going to release inside is org 1 all. If you make
a typo, you can just type it again. Again a constant number, 1000, so we have equal numbers of
A and B being released, but in 2 sepearate compartments. The transporter t1 is what will casue
molecule a to be transported inside of organelle number 1, so we're going to create a release
site called rel_t1, and its going to be an object release again, orientation since t1 is a surface
molecule is top/front, and we're going to release these in organelle 1 in the t1_region. This
restricts the release of t1 to be only within that region that we created on organelle 1, and again a
constant number will be released, 1000. And finally, t2, lets create rel_t2 as the t2 release site,
releasing molecule t2, orientation top/front, its an obejct/region release, but now its going to be
released on organelle 2 in a region that we named there called t2_region. Releasing a constant
number, 1000. We've now finished creating the relase sites, we're almost ready to run our
model, but first we need to enable reaction output so we have numerical output being created by
mcell and viz output so we can visualize the dynamics that the simulation will create. This
completes creation of the model.

Open the Define Reactions panel and hit the plus key to add a reaction. In the reactants textbox
we type in the first half of the reaction, in this case ‘A’ with an apostrophe denoting ‘A’ on the
outside plus t1 with apostrophe facing outward. These reactants undergo an irreversible reaction
to create products ‘A’ comma means ‘A’ on the inside plus t1 apostrophe means t1 remains
facing outwards. The forward rate constant is 3x10^8 per molar per second. The second reaction
will be ‘A’ plus ‘B’ irreversibly producing molecule ‘C’, because both reactants are volume
molecules no orientation marks are required when writing the reaction. The rate constant is
1x10^9 per molar per second. The next reaction is ‘C’ comma, which means ‘C’ on the inside,
plus t1 facing outward irreversibly creates ‘C’ apostrophe meaning ‘C’ on the outside plus t1
apostrophe still facing outward, with a forward rate constant 3x10^8 per molar per second. The
final reaction is ‘C’ on the outside plus t2 facing outward irreversibly creates products ‘C’ comma
meaning ‘C’ on the inside plus t2 still facing outwards with forward rate constant 3x10^8 per molar
per second. We have now defined all desired reactions. Next we need to place our molecules at
their initial positions within the model. This is done by creating Release Sites. The first molecule
we are going to release is molecule ‘A’, so lets name the release site rel_A. It will release
molecule ‘A’, and will be released inside an object or region. We want to release throughout the
Cell, but not inside the two organelles. To do this we say Cell All minus the union of Organelle 1
All and Organelle 2 All. This is a boolean operation that will release the molecule ‘A’ inside the
cell but outside the two organelles. We're going to release a constant number of A molecules,
1000 of them. The next release site is to place molecule ‘B’, so lets call it rel_B, and releasing
inside an object, but this time we are releasing inside Organelle 1 All. Again a constant number,
1000, so we have equal numbers of A and B being released, but in 2 separate compartments.
The transporter t1 is what will casue molecule ‘A’ to be transported inside of Organelle 1, as we
described in our reactions, so we're going to create a release site called rel_t1. Its going to be an
object release again, we need to declare an orientation since t1 is a surface molecule, in this
case we select top/front, and we're going to release these on Organelle 1 in the t1_region. This
restricts the release of t1 to be only within the region that we created on Organelle 1, and again a
constant number will be released, 1000. Finally we need to release t2. Lets create rel_t2 as the t2
release site, which releases molecule t2, the orientation is also top/front, we are releasing in a
region, but its going to be released on Organelle 2 in the region we created t2_region. We
release a constant number, 1000 again. We've now finished creating the release sites, and are
almost ready to run our model. A final step is to enable Reaction Output so MCell will create
numerical output for plotting and enable Visualization Output so we can visualize the dynamics
that the simulation will create. This completes creation of the model.

Completion of the model (26:09:12)
---------------------------------------------

Export MDL (26:25:09)
---------------------------------------------

In order to run the model we need to export it. This is done under the CellBlender project setup
panel. Clicking on export blender project clicking on export CellBlender projects brings up a file
navigation menu that defaults to the project directory that we specify, and clicking on save
exports the entire model and its now ready to run in mcell. We switch to another virtual console
on our desktop, cd to our directory where our project lives, and run the mcell main file which is
called demo.main.mdl mcell starts up, gives some useful prelim information about the model
settings, and begins to run. This takes several minutes.

In order to run the model we need to export it. This is done under the CellBlender Project Setup
panel. Clicking on Export Blender Project brings up a file navigation menu that defaults to the
project directory that we specified, which is where we will save all of our MDL files. MDL stands
for Model Description Language, and is the language MCell parses to create the model and
perform the simulation. We could directly edit our MDL files using a text editor if necessary, but
in this case the model is fully defined and ready to go. We switch to another virtual console on
our desktop, go to our directory where our project lives, and run the MCell main file which is
called demo.main.mdl. MCell starts up, gives some useful preliminary information about the
model settings, and begins to run. This takes several minutes.

Run for a bit and speed up (27:28:03)
---------------------------------------------

Audio/visual becomes desynced here
---------------------------------------------

Normal Speed (30:16:28)
---------------------------------------------

Thanks to the miracle of modern electronics and movie magic, we can fast forward to the end of
our simulation, and see the completion of our run. We're now ready to switch back to cellblender
and blender and visuatlize the results we just generated. In our other virtual console, we see our
model as we left it, and to visualize the results we just generated we hit visualize simulation
results, navigate tot he directory, choose the viz directory, and say read molecule files. Blender
reads the 20000 files we just generated. And jumps to the very first iteration, by default, with
playback turned off. And in order to better visualize what we've done we're swtiching back to
solid mode, which makes the interior of the objects invisible. To maek the visible, we go to the
objects property panel, enable transparency, for each of the 3 objects, and we can use the
outliner to select one object at a time an enable its transparency. And next we need to create a
material, which is transparent, we choose the clel, choose a new material, turn on transparency
for taht material, set an opacity lower than 1, and voila, the clel is now transparent and we can
see inside. The two oraganelles however are still not transparent. Since we've created a material
which is transparent, instead of creating a new material, we can choose to associate our object
with the transparent material we've just created, and we can do the same thing for org 1 and 2.
Choose the material we've just crated, and associate org2 with that material. And now we can
see thei nitail conditions taht we specified in our blender setup, the molecules of a, red, are
outside of the two organelles. The b molecules, which are green, are inside org 1. The t1
molecules are on the t1_region, they are blue. And we see under the moelcules object that
appears in the outliner, we have moleucle a, b, t1 and t2. And by clicking on the visibility icon we
can turn those on and off, make them visible nad invisible. Notice that molecule c is missing
from that list, its because initially we didn't release any molecule c, we're looking at only the first
frame of the simulation, before any molecules of c have been created by the reactions. To be
able to visualize the entire simulation, which is 20000 iterations long, we set the start and end to
be 20000, select view all under the timeline, and hit the play vcr controls. And the animation
begins. While the animation is playing, we can rotate the scene and view it from any angle. You
can also grab on to the yellow cursor in the timeline which indicates the current position in time
and drag with the left mouse button to any point in time and notice as we go further in time, a
molecules have disappeared, and we've accumulated c molecules in the cytoplasm of the cell,
which then are trasnported into org 2 and accumulate there. When time runs past the end of the
animation, at iteration 20000, frame number 20000, blender will automatically reset the timeline
back to t0. And it loops from the beginning. The vcr contrls let you pause, start and stop, rewind,
fastforward. While its palying, you can actuallly turn on and off different moleucles to visualize
the state of the system. Here we've turned off everything except the c moleucles, we can watch
them begin created, transported into the cytoplasm of the cell, then accumulate in org 2. That
concludes our demo of cellblender, but we've generated visual output but we've also generated
numerical output, reaction data ouput from the simulation, which we'll visualize using a plotting
pacakge. We'll do that in the next segment.

For the sake of time, we fast forward to the end of our simulation, and see the completion of our
run. Feel free to pause at this point and wait for your own simulation to finish so you can follow
along with the visualization. We're now ready to switch back to CellBlender and visualize the
results we just generated. In our original virtual console, we see our model as we left it. To
visualize the results open the Visualize Simulation Results CellBlender panel, navigate to our
working directory, choose the viz directory, and click Read Molecule Files. Blender tabulates the
names of the 20000 files we generated, which may take a few seconds. It starts by displaying
the position of all existing molecules at the first iteration step. We see that in wireframe view
mode the scene is confusing, so in order to better visualize what we've done we switch back to
solid view mode, but now the cell is opaque. To make the interior visible we will make the objects
transparent. First go to the Objects Property Panel and enable transparency for each object, by
using the Outliner to select one object at a time and enable transparency. Next we need to
create a transparent material that we will apply to the object. We select the Cell object, make a
new material, check the transparency option and set an opacity lower than 1. Voila, the Cell is
now transparent and we can see the ‘A’ molecules in the cytoplasm of the cell. The two
organelles however are still not transparent. Since we've created a material which is transparent,
instead of creating a new material, we can choose to associate an object with the transparent
material we've just created. Select Organelle 1 and choose the material we've just created. We
do the same for Organelle 2. With these settings its apparent that visualizing the dynamics of
our model is much easier. We can now see the initial conditions that we specified in our
CellBlender setup, the molecules of ‘A’, red, are in the Cell cytoplasm, but outside of the two
organelles. The ‘B’ molecules, which are green, are inside Organelle 1. The t1 molecules are
shown in dark blue on Organelle 1 and t2 molecules, shown in teal, are fixed on Organelle 2. We
see under the molecules object in the Outliner that we are displaying molecules ‘A’, ‘B’, ‘t1’ and
‘t2’. By clicking on the visibility icon we can hide or show each molecule as desired. Notice that
molecule ‘C’ is missing from the list, which makes sense as we didn’t release any ‘C’ initially, but
expect C to accumulate as time passes. To be able to visualize the entire simulation, which is
20000 iterations long, set the end time to 20000 and select View All under the timeline, and then
hit the play button on the VCR controls. While the animation is playing, we can rotate the scene
and view it from any angle. The playback controls are similar to any standard playback device,
with start, stop, pause, rewind, and fastforward. We can also grab the yellow bar in the Timeline
and move it through time as desired. After some time has elapsed, ‘A’ molecules have
disappeared, and we've begun accumulating ‘C’ molecules in the cytoplasm of the cell, which are
then transported into Organelle 2 and accumulate there. When time runs past the end of the
animation, at iteration 20000, Blender will automatically reset the timeline back to time zero and
continue looping. While its playing, we can hide and show molecules to help simplify the scene
and get a better understanding of the dynamics of each molecule. Here we've turned off
everything except the ‘C’ molecules, and we can watch them being created, transported into the
cytoplasm of the cell, and accumulating in Organelle 2. This concludes our demo of Cellblender.
But wfor the camerae've also generated numerical reaction output, which we can visualize using
a plotting package. (TODO Add plot still to the movie, the following is just a guess) Here we can
see the count of ‘A’ in the cytoplasm, count of ‘B’ in Organelle 1, and count of ‘C’ in Organelle 2.
It is apparent that these numbers are coupled by the reaction pathways and show correlations in
their evolution. A major benefit of MCell is that the stochastic noise of finite particles is apparent
in a given simulation. If we were to rerun the simulation with a series of different random number
generator seeds, we could obtain the average and variance of the evolution of each molecule
over time.

The End (37:36:24)
---------------------------------------------


