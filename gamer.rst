.. _gamer:

*********************************************
Using GAMer to Refine a Mesh
*********************************************

.. _gamer_intro:

Introduction
---------------------------------------------

In this tutorial you will go through the step-by-step procedure to generate a
Constrained Delaunay Tetrahedral Mesh suitable for Finite Element computation.
You will learn how to:

- Import segmented geometries into Blender  
- Use GAMer to improve the quality of the surface mesh
- Generate a bounding mesh
- Further improve the mesh and define boundary markers
- Generate a tetrahedral mesh with marked domains and boundaries

Our model of interest today is the murine cardiac myocyte calcium release unit.
You can get the segmentation from the Cell Centered Database (CCDB), a
collection of 2D, 3D, and 4D cellular and subcellular data derived from light
and electron microscopy. The data we will be using today is from entry 3603 .
For the purposes of this tutorial, we have selected a nicely segmented section
for model building. The segmentation can be found in file tt­sr­mit.mod . The
segmentation has been created and visualized in IMOD and shown in Fig. 1. The
hand-segmented contours can be used to generate a preliminary surface mesh of
the extracted features in IMOD.

.. _gamer_tutorial:

Tutorial
---------------------------------------------

Preliminary surface meshes from segmentations are typically of poor quality for
computation. A poor quality mesh is defined as one which will lead to large
errors in computation or inefficiency. For triangle surface meshes, the quality
of the mesh can be qualitatively judged by evenness of the edge and node
distribution. Quantitatively, mesh quality is measured by mesh topology and
proportion of high aspect triangles (triangles with extremely large and small
angles).

- In order to load the mesh from IMOD into Blender, we first need to convert
  from IMOD’s .mod contour format to Wavefront .obj surface mesh format. Note
  that the “$” denotes the command-line prompt in the terminal.  $ imod2obj
  tt­sr­mit.mod tt­sr­mit.obj

- Now we can open up the new .obj file in blender.

  - Start Blender by typing ``blender`` at the command line.

  - The Cube, Camera and Lamp are placed in the viewport by default. We won’t
    need them so go ahead and delete them. Note, Blender has lots of useful
    keyboard shortcuts. Where applicable in the tutorial, relevant shortcuts
    are shown as follows: Select All [A] , Delete [X].

  - Change the Rotation Mode by going to User Preferences → Input tab →
    track-ball
  - Import the data file with File → Import → Wavefront (.obj): tt­sr­mit.obj.

- You may notice that parts of the model are getting truncated by the clipping
   plane. To remove the visual artifacts, we perform the following:

  - Increase the distance of the far clipping plane by opening the Numerics
    Panel [N] → View subpanel → Clip → End: 2000 <Enter>.

  - For geometric models, it’s often useful to change to the orthographic view.

- We need the model to be in one volumetric domain so let’s join it. In the
  Outliner shift lmb (i.e.  left-mouse-button) click each object, clicking on
  obj1_T-Tub_1 last, then do Object → Join [ctrl+J]

- The mesh is currently rendered as a solid material. While this is great for
  the purposes of animation and visualization, we care about the distribution
  of nodes and edges. To show the edges in the Viewport, go to the Object
  Properties tab and select Wire and Draw all Edges in the Display subpanel.
  Refer back to Fig. 4 for help finding these options.

- To simplify future manipulation let’s center the model about the origin.

  - Object → Transform → Geometry to Origin.

  - Rearrange the view using the following options: View → Selected 
    [numpad .], View → Front [numpad 1] , View → Selected [numpad .]

- Let’s now align the model so that the long axis is horizontal.

  - Rotate about the y-axis by 45 degrees to line up the model horizontally
    [R Y 45]

  - Save this state as the object’s default rotation and scale. Object →
    Apply → Rotation and Scale [ctrl + A, Rotation and Scale]

- CHECKPOINT: Let’s save our work now as: tt­sr­mit.imp_obj.blend. Note that if
  you get behind or if something goes awry, you can always close Blender and
  reopen at this checkpoint!

- We can use the mesh analyzer function of CellBlender to inspect the mesh for
  suitability for computational analysis. I.e., that there are no unexpected
  holes or bizarre topologies.

  - CellBlender → Mesh Analysis → Analyze Mesh! You should see that it is not
    watertight and non-manifold. Now we know that there is a hole in the mesh
    somewhere, rendering it non-watertight.  Similarly there are some
    topological issues indicated by non-manifold topology. Manifold geometry is
    essentially geometry which can exist in the real world. For some pragmatic
    examples of non-manifold geometry please consult the following
    stackexchange.

- Let’s start by cleaning up regions of non-manifold topology.

  - First engage Edit Mode [tab] and Unselect All [A] .
  - Using your mouse pick the Vertex-Select Mode option.
  - Highlight regions of non-manifold topology Select → Select All By Trait →
    Non Manifold [shift + ctrl + alt + M] . This highlights all the regions of
    non-manifold topologies.

- Conveniently non-manifoldness is a problem in the animation industry (it
  tends to cause problems with raytracing among other things). Thus, Blender
  has some built-in tools to help resolve non-manifoldness.

  - First, Select All [A] then go to Mesh → Clean up → Degenerate Dissolve.
    This function will take care of several cases of bad geometry: edges with
    no length, faces with no area, or face corners with no area. It does so by
    deleting vertices and edges it thinks don’t make sense.
  - This will leave some holes in the mesh. We can automatically fill the holes
    using: Mesh → Clean up → Fill Holes.
  - Let’s now check how many issues we have resolved. Unselect All [A] then
    Select → Select All By Trait → Non Manifold [shift + ctrl + alt + M] . We
    see that the mesh has been substantially improved but is not perfect yet.

- We can zoom in on the selected region by performing View → Selected [num .] .

  - Let’s delete the dangling vertex. First Unselect All [A] then select the
    culprit vertex [rmb click] (Note, be sure to align the view such that the
    vertex has nothing behind it. You don’t want to accidentally delete
    something behind) and delete [X] and choose Vertices.

- Once again let’s take a look to see if there are any residual problems. In
  Edit Mode, Select → Select All By Trait → Non Manifold [shift + ctrl + alt +
  M] . At this point your mesh should have no more issues.
- Recall that the degenerate dissolve function deleted some vertices and edges.
  In some of these cases, when the holes are filled, the polygons may no longer
  be triangular. In Edit Mode, to re-triangulate, Select All [A] then choose
  Mesh → Faces → Triangulate [ctrl + T]
- Our mesh is starting to look pretty good! Let’s re-run mesh analyzer

  - Return to Object Mode [tab]
  - Rerun mesh analysis: CellBlender → Mesh Analysis → Analyze Mesh. We now
    have a watertight and manifold mesh but we have inward facing normals. This
    means that everything is good except the mesh is inside out!
- To reset the orientation of the faces, we need to recalculate the normals.

  - Return to Edit Mode [tab]
  - Mesh → Normals → Recalculate Outside [ctrl + N]
  - Return to to Object Mode [tab], run mesh analyzer again. We now we have
    good geometry to start with. Be sure to note the surface area and volume.
    See fig 10.

- CHECKPOINT: Save your progress to: tt­sr­mit.clean.blend 

- We are now ready to begin surface mesh refinement with GAMer .

  - Go to the GAMer tab on the left side of Blender .
  - Click on the Surface Mesh Improvement button to show this subpanel. The
    subpanel provides several functions as follows:

    - Coarse Dense Tris: reduces the number of triangles in densely
      triangulated portions of the mesh.
    - Coarse Flat Tris: reduces the number of triangles in flat regions of the
      mesh.
    - Smooth Tris: improves the aspect ratio of triangles by maximizing angles.
      It does so by flipping edges moving vertices based on angle and the local
      structure tensor.
    - Normal Smooth Surf: smooths surface roughness using a feature-preserving
      normal averaging algorithm.

  - In Object Mode [tab] with the model selected, perform the following
    operations in order. After each step the approximate number of vertices
    remaining is given.

    - Smooth Tris: Max_Min = 15, S_Iter = 10 (~73K vertices)
    - Coarse Dense Tris: CD_R, 1; CD_Iter, 5 (~37K vertices)
    - Smooth Tris: Max_Min, 15; S_Iter, 10
    - Coarse Dense Tris: CD_R, 0.5; CD_Iter, 5 (~28K vertices)
    - Smooth Tris: Max_Min, 20; S_Iter, 20
    - 2x Normal Smooth Surf

  - In Object Mode [tab] , run Mesh Analyzer. Note the slightly smaller surface area but similar volume.

- CHECKPOINT: Save your progress to: tt­sr­mit.gamer_proc_1.blend
- Now that we have a reasonable surface mesh of our features, we want to place
  a boundary box around the features to represent the cytosol.

  - First we center the 3D cursor to the center. We will next add a cube at the
    position of the 3D cursor. In Object Mode [tab] , Object → Snap → Cursor to
    Center [shift + S, Cursor to Center]
  - We will next add a cube at the position of the 3D cursor. Add a cube mesh
    object, Add → Mesh → Cube [shift + A, Mesh → Cube]
  - Let’s scale and translate the bounding box to where we want it. Recall that
    the Numerics Panel can be summoned with [N] .

    - Location (-40, 15, 30)
    - Scale (275, 130, 220)

- The cube is currently a quadrilateral mesh. We need to convert to a
  triangular mesh for later tetrahedralization.

  - Return to Edit Mode [tab] and Select All [A] . Then triangulate by going to
    Mesh → Faces → Triangulate [ctrl + T]
  - To capture detailed features we will need additional triangles. With the
    cube selected, Mesh → Edges → Subdivide a total of six times [W,
    subdivide].
  - Return to Object Mode [tab] .

- CHECKPOINT: Save your progress to: tt­sr­mit.with_cube.blend
- To get the surface representation of the cytosolic volume, we must subtract
  our features from our cube mesh.

  - In Object Mode [tab] , in the Modifier tab of the Properties Panel Add
    Modifier, Generate: Boolean, Operation: Difference, Object: obj1_T-Tub_1
    and apply the modifier.
  - In the Outliner click on the eye to hide obj1_T-tub_1.
  - With the cube selected, apply the current rotation and scale transform.
    Object → Apply → Rotation and Scale [ctrl + A, Rotation and Scale]
  - Apply the current location transform. Object → Apply → Location [ctrl + A,
    Location]
  - If you would like to show the edges, go to the Object Properties and select
    Wire and Draw all Edges.

- CHECKPOINT: Save your progress to: tt­sr­mit.boolean.blend
- Once again, we have a surface mesh to refine.

  - First in Edit Mode [tab] we can Select → Select All By Trait → Non Manifold
    [shift + ctrl + alt + M] .  Nothing should be selected. If there are some
    issues, try performing Degenerate Dissolve followed by Fill Holes.
  - Return to Object Mode [tab] , run Mesh Analyzer. We find that the Mesh is
    not triangulated.

- We can triangulate as before:

  - In Edit Mode [tab] , Select All [A] , Mesh → Faces → Triangulate [ctrl + T]
  - Return to Object Mode [tab] , and run Mesh Analyzer. We have a good
    geometry to start refining.

- CHECKPOINT: Save your progress to: tt­sr­mit.boolean_clean.blend
- Let’s begin surface refinement using GAMer

  - In Object Mode [tab] with the cube selected, perform the following
    operations in order. After each step the approximate number of vertices
    remaining is given.

    - Smooth Tris: Max_Min = 15, S_Iter = 10 (~70K vertices)
    - Coarse Dense Tris: CD_R = 0.75, CD_Iter = 10 (~57K vertices)
    - Coarse Flat Tris: CF_Rate = 0.016 (~44K vertices)
    - Smooth Tris: Max_Min = 15; S_Iter = 10
    - Coarse Dense Tris: CD_R = 0.1, CD_Iter = 10 (~42K vertices)
    - Smooth Tris: Max_Min = 20; S_Iter = 20
    - 2x Normal Smooth Surf

  - In Object Mode [tab] , run Mesh Analyzer. Note the slightly smaller surface area but similar volume.

- CHECKPOINT: Save your progress to: tt­sr­mit.gamer_proc_2.blend Now we're
  ready to add boundaries and associated boundary markers to the mesh!
- Return to the GAMer tab and choose the Boundary Marker tool

  - Add a new boundary (+ button). By clicking on the color swatch, you can
    select the color you wish to represent the Cytosol. The color only serves
    as a visual aid to help you mark. Set the color to green.
  - Change the name of the boundary to 'Cytosol'
  - Enter Edit Mode [tab] and choose Face Select Mode and begin selecting all
    faces of the cytosol. Clicking each face is very arduous! For larger
    surfaces, you may elect to select using the “Circle Select” tool [C] or the
    “Border Select” tool [B] . Use "Assign" to assign selected faces to
    boundary. You can assign as you go or all together at the end. Note, it can
    sometimes be very helpful to hide all selected faces using [H], or hide all
    unselected faces using [shift + H] . You can unhide everything using [alt +
    H] . In the next steps we’ll be using the the “Border Select”  tool [B].
  - Turn off option: “Limit selection to visible”.
  - View → Front [numpad 1] .
  - Select faces of Cytosol. Use “Border Select” tool [B] to select the profile
    of each side (see Fig. 19).
  - View → Top [numpad 7] .
  - Select additional faces of Cytosol. Use “Border Select” tool [B] to select
    the profile of remaining sides.
  - Hide All Unselected [shift + H] . You may notice that some triangles from
    internal features may have been selected. We will fix this next by
    selecting linked triangles.
  - Unselect All [A]
  - Select one triangle, click [rmb] .
  - Select Linked [ctrl + L]
  - Hide All Unselected [shift + H]
  - Use "Assign" to assign selected faces to boundary.
  - Turn on option: “Limit selection to visible”.
  - Unhide All [alt + H]
  - Unselect All [A]

- CHECKPOINT: Save your progress to: tt­sr­mit.cytosol.blend
- When you are finished marking the cytosol,

  - Select and hide the Cytosol [H]
  - Add a new boundary named “Mitochondria”, set color to magenta.
  - Select one face on each mitochondria [shift + rmb] and Select Linked [ctrl
    + L]
  - Use “Assign” to assign the selected faces to be in the mitochondria.
  - When finished, hide the mitochondria [H] and proceed with marking the
    t-tubule (“TT”, set color to blue) and sarcoplasmic reticulum (“SR”, set
    color to yellow). We chose the two letter abbreviations because boundary
    names cannot contain special characters or spaces (underscores are OK).

- CHECKPOINT: Save your progress to: tt­sr­mit.all_marked.blend 
- Now we finally have a Surface Mesh ready for tetrahedralization! Choose
  Tetrahedralization Tool and select the model in the Outliner. Make sure all
  faces of the model are selected.

  - Enter Edit Mode [tab]
  - Select All [A]
  - Return to Object Mode [tab]
  - Add domain to model (+ button)
  - Use Volume Constraint and set to 5000

- Choose tetrahedralization options:

  - Set mesh file base name to “tt-sr-mit.tet_mesh”
  - Set Min dihedral angle of 20
  - Choose DOLFIN mesh format
  - Hit Tetrahedralize button!
