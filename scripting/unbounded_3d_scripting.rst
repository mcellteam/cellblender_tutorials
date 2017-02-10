.. _unbounded_3d_scripting:


***************************************************
Unbounded 3D Diffusion Data Model Scripting Example
***************************************************

.. Git Repo SHA1 ID: 3520f8694d61c81424ff15ff9e7a432e42f0623f


MCell and CellBlender can be easily used to demonstrate unbounded 3D diffusion. Simply release
a large number of molecules at the origin and watch them diffuse. However, to make measurements,
a little more work is required.

This example uses a script that builds a series of concentric counting shells centered at the origin.
The shells are assigned a transparent surface class so the molecules can pass through them. Counting
statements are added to count the number of molecules in each shell (the total within each sphere
minus the total in the next inner sphere). This allows easy plotting of the final result.

The following animation gives a visual outline of this process:

.. image:: ./images/unbounded_diffusion_800.gif


Unbounded Diffusion Construction Script
---------------------------------------------

The following script builds the CellBlender model for this example from scratch. It will be discussed in more detail below.
If you just want to run this demonstration, copy this entire script and paste it into a Blender text editing window. Then
press the **"Run Script"** button at the bottom of the text editing window. That should build the model ready for CellBlender
to run it. Each section will be discussed further below this script.

::


    # Import cellblender to get the data model and project directory functions

    import math
    import cellblender as cb

    # Get a copy of the data model and change directories to the project directory for any file I/O

    dm = cb.get_data_model(geometry=True)
    old_location = cb.cd_to_project()

    # Print some information about the data model

    print ( "###############################################################" )

    print ( "Data Model Top Level Keys = " + str(dm.keys()) )
    print ( "MCell Keys = " + str(dm['mcell'].keys()) )

    print ( "###############################################################" )


    # Define parameters and set default values (these will also be available as local variables in this script)
    #  The format for each parameter is:   Name, Value, Units, Description
    #    All values are given as strings!!!

    pars = [
      # These control the geometry of the model
      ['n',    "3",       '#',   'Number of shells to sample'],
      ['dr',   "0.1",    'um',   'Delta Radius of each successive shell'],
      ['ss',   "2",       '#',   'Surface Smoothness of each shell'],
      # These describe the behavior of the model
      ['dc',    "1e-6",   'cm^2/sec',    'Diffusion Constant of Molecules'],
      ['nrel',  "1000",   'Count',       'Number of molecules to release'],
      # These control the simulation itself
      ['iters', "600",   '',      'Number of iterations to run'],
      ['seeds', "1",     '',      'Number of seeds to run'],
      ['dt',    "1e-6",  'sec',   'Time step for each iteration of the simulation'],
     ]

    # Update local parameter list values from the existing data model with user-modified settings BEFORE regenerating it
    dm_par_list = dm['mcell']['parameter_system']['model_parameters']
    for dm_par in dm_par_list:
        print ( "Data Model Parameter " + dm_par['par_name'] + " = " + dm_par['par_expression'] )
        for p in pars:
            if dm_par['par_name'] == p[0]:
                # Update the local expression based on the parameter found in the incoming data model
                p[1] = dm_par['par_expression']
                p[2] = dm_par['par_units']
                p[3] = dm_par['par_description']

    # Create the local variables from the updated values to use in this script
    for p in pars:
        locals()[p[0]] = eval(p[1])

    # Create the new mcell data model inside the existing data model (this deletes the previous mcell data model)
    dm['mcell'] = { 'data_model_version' : "DM_2014_10_24_1638" }


    # Restore the parameters that were either initialized from scratch or preserved from the previous data model
    dm['mcell']['parameter_system'] = { 'model_parameters':[] }   # Parameters are currently unversioned
    for p in pars:
        dm['mcell']['parameter_system']['model_parameters'].append ( { 'par_name':p[0], 'par_expression':p[1], 'par_units':p[2], 'par_description':p[3] } )



    ##################################
    #   Geometry  Support  Classes   #
    ##################################

    class point:

      def __init__ ( self, x, y, z ):
        self.x = x;
        self.y = y;
        self.z = z;


    class face:
      
      def __init__ ( self, v1, v2, v3 ):
        self.verts = [];
        self.verts.append ( v1 );
        self.verts.append ( v2 );
        self.verts.append ( v3 );
      

    class IcoSphere:

      # Builds an icosphere with recursion
      
      def __init__ ( self ):
        self.points = []
        self.faces = []
      
      def make_dm_object ( self, center_x=0, center_y=0, center_z=0 ):
        obj = {}
        obj['vertex_list'] = []
        obj['element_connections'] = []

        for p in self.points:
          obj['vertex_list'].append ( [ center_x+p.x, center_y+p.y, center_z+p.z ] )
        for f in self.faces:
          obj['element_connections'].append ( f.verts )

        return obj

      def add_normalized_vertex ( self, p ):
        # Normalize the point
        # Add to the list of points if it's not already in the list
        # Return an index to the new or existing point in the list

        l = math.sqrt ( (p.x * p.x) + (p.y * p.y) + (p.z * p.z) );
        pnorm = point ( p.x/l, p.y/l, p.z/l );

        # Check if it's already there
        index = -1;
        for pt in self.points:
          if (pt.x == pnorm.x) and (pt.y == pnorm.y) and (pt.z == pnorm.z):
            index = self.points.index(pt)
            break;

        if (index < 0):
          self.points.append ( pnorm );
          index = self.points.index ( pnorm );
          #print ( "Added vertex at " + str(index) );
        #else:
        #  print ( "Found vertex at " + str(index) );
        return (index);


      def __init__ ( self, recursion_level, scale_x=1.0, scale_y=1.0, scale_z=1.0 ):

        self.points = [];

        t = (1.0 + math.sqrt(5.0)) / 2.0;  # Approx 1.618033988749895
        
        # Create 12 verticies from the 3 perpendicular planes whose corners define an icosahedron

        self.add_normalized_vertex ( point (-1,  t,  0) );
        self.add_normalized_vertex ( point ( 1,  t,  0) );
        self.add_normalized_vertex ( point (-1, -t,  0) );
        self.add_normalized_vertex ( point ( 1, -t,  0) );

        self.add_normalized_vertex ( point ( 0, -1,  t) );
        self.add_normalized_vertex ( point ( 0,  1,  t) );
        self.add_normalized_vertex ( point ( 0, -1, -t) );
        self.add_normalized_vertex ( point ( 0,  1, -t) );

        self.add_normalized_vertex ( point ( t,  0, -1) );
        self.add_normalized_vertex ( point ( t,  0,  1) );
        self.add_normalized_vertex ( point (-t,  0, -1) );
        self.add_normalized_vertex ( point (-t,  0,  1) );
        
        
        # Rotate all points such that the resulting icosphere will be separable at the equator
        
        if (True):
          # A PI/6 rotation about z (transform x and y) gives an approximate equator in x-y plane
          angle = (math.pi / 2) - math.atan(1/t);
          # print ( "Rotating with angle = " + str(180 * angle / math.pi) );
          for p in self.points:
            newx = (math.cos(angle) * p.x) - (math.sin(angle) * p.z);
            newz = (math.sin(angle) * p.x) + (math.cos(angle) * p.z);
            p.x = newx;
            p.z = newz;

        # Build the original 20 faces for the Icosphere

        self.faces = []

        # Add 5 faces around point 0 (top)
        self.faces.append ( face (  0, 11,  5 ) );    
        self.faces.append ( face (  0,  5,  1 ) );    
        self.faces.append ( face (  0,  1,  7 ) );    
        self.faces.append ( face (  0,  7, 10 ) );    
        self.faces.append ( face (  0, 10, 11 ) );    

        # Add 5 faces adjacent faces
        self.faces.append ( face (  1,  5,  9 ) );    
        self.faces.append ( face (  5, 11,  4 ) );    
        self.faces.append ( face ( 11, 10,  2 ) );    
        self.faces.append ( face ( 10,  7,  6 ) );    
        self.faces.append ( face (  7,  1,  8 ) );    

        # Add 5 faces around point 3 (bottom)
        self.faces.append ( face (  3,  9,  4 ) );    
        self.faces.append ( face (  3,  4,  2 ) );    
        self.faces.append ( face (  3,  2,  6 ) );    
        self.faces.append ( face (  3,  6,  8 ) );    
        self.faces.append ( face (  3,  8,  9 ) );    

        # Add 5 faces adjacent faces
        self.faces.append ( face (  4,  9,  5 ) );    
        self.faces.append ( face (  2,  4, 11 ) );    
        self.faces.append ( face (  6,  2, 10 ) );    
        self.faces.append ( face (  8,  6,  7 ) );    
        self.faces.append ( face (  9,  8,  1 ) );
        

        # Subdivide the faces as requested by the recursion_level argument
        old_points = None;
        old_faces = None;
        
        for rlevel in range(recursion_level):
          # System.out.println ( "\nRecursion Level = " + rlevel );
          # Save the old points and faces and build a new set for this recursion level
          old_points = self.points;
          old_faces = self.faces;
          self.points = []
          self.faces = []
          for f in old_faces:
            # Split this face into 4 more faces
            midpoint = point(0,0,0)
            potential_new_points = []
            for i in range(6):
              potential_new_points.append ( point(0,0,0) )
            for side in range(3):
              p1 = old_points[f.verts[side]];
              p2 = old_points[f.verts[(side+1)%3]];
              midpoint = point ( ((p1.x+p2.x)/2), ((p1.y+p2.y)/2), ((p1.z+p2.z)/2) );
              potential_new_points[2*side] = p1;
              potential_new_points[(2*side)+1] = midpoint;
            # Add the 4 new faces
            # Start with the verticies ... add them all since add_normalized_vertex() will remove duplicates
            vertex_indicies = []
            for i in range(6):
              vertex_indicies.append ( 0 )
            for i in range(6):
              vertex_indicies[i] = self.add_normalized_vertex ( potential_new_points[i] );
            # Now add the 4 new faces
            self.faces.append ( face ( vertex_indicies[0], vertex_indicies[1], vertex_indicies[5] ) );
            self.faces.append ( face ( vertex_indicies[1], vertex_indicies[2], vertex_indicies[3] ) );
            self.faces.append ( face ( vertex_indicies[3], vertex_indicies[4], vertex_indicies[5] ) );
            self.faces.append ( face ( vertex_indicies[1], vertex_indicies[3], vertex_indicies[5] ) );

        for pt in self.points:
          pt.x *= scale_x
          pt.y *= scale_y
          pt.z *= scale_z



    # Add materials for the objects
    dm['mcell']['materials'] = { 'material_dict' : {} }   # Materials are currently unversioned
    dm['mcell']['materials']['material_dict']['shell_color']   = { 'diffuse_color' : {'a':0.3, 'r':0.2, 'g':0.4, 'b':1.0} }


    # Create container objects for geometrical objects and model objects
    dm['mcell']['geometrical_objects'] = {}   # Geometrical objects are currently unversioned
    dm['mcell']['model_objects'] = { 'data_model_version':"DM_2014_10_24_1638" }

    # Each container also includes a list
    dm['mcell']['geometrical_objects']['object_list'] = []
    dm['mcell']['model_objects']['model_object_list'] = []

    # Create a transparent surface class
    dm['mcell']['define_surface_classes'] = {
      'data_model_version' : "DM_2014_10_24_1638",
      'surface_class_list' : [
        {
          'data_model_version' : "DM_2014_10_24_1638",
          'name' : "transp",
          'surface_class_prop_list' : [
            {
              'affected_mols' : "ALL_MOLECULES",
              'clamp_value' : "0",
              'data_model_version' : "DM_2015_11_08_1756",
              'molecule' : "",
              'name' : "Molec.: ALL_MOLECULES   Orient.: Ignore   Type: Transparent",
              'surf_class_orient' : ";",
              'surf_class_type' : "TRANSPARENT"
            }
          ]
        }
      ]
    }

    # Define the Modify Surface Regions structure
    dm['mcell']['modify_surface_regions'] = {
      'data_model_version' : "DM_2014_10_24_1638",
      'modify_surface_regions_list' : []
    }

    # Define the count/plot structure
    dm['mcell']['reaction_data_output'] = {
      'always_generate' : True,
      'combine_seeds' : True,
      'data_model_version' : "DM_2016_03_15_1800",
      'mol_colors' : False,
      'plot_layout' : " ",
      'plot_legend' : "0",
      'reaction_output_list' : [],
      'rxn_step' : ""
    }
      
    # Make a series of transparent icospheres and define a count statement for each one
    for i in range(n):
        r = (i+1) * dr
        ico = IcoSphere(ss,r,r,r).make_dm_object ( 0, 0, 0 )
        ico['name'] = 'ico_' + str(i+1)
        ico['material_names'] = [ 'shell_color' ]
        dm['mcell']['geometrical_objects']['object_list'].append ( ico )
        dm['mcell']['model_objects']['model_object_list'].append ( { 'name':ico['name'] } )
        dm['mcell']['modify_surface_regions']['modify_surface_regions_list'].append ( {
                  'data_model_version' : "DM_2015_11_06_1732",
                  'name' : "Surface Class: transp   Object: ico_%d   ALL" % (i+1),
                  'object_name' : "ico_%d" % (i+1),
                  'region_name' : "",
                  'region_selection' : "ALL",
                  'surf_class_name' : "transp"
                } )
        mdl_string = "COUNT[vm,Scene.ico_%d]" % (i+1)
        if i > 0:
            mdl_string += " - COUNT[vm,Scene.ico_%d]" % (i)
        dm['mcell']['reaction_data_output']['reaction_output_list'].append ( {
                  'count_location' : "Object",
                  'data_file_name' : "",
                  'data_model_version' : "DM_2016_03_15_1800",
                  'mdl_file_prefix' : "ico_%d" % (i+1),
                  'mdl_string' : mdl_string,
                  'molecule_name' : "vm",
                  'name' : "MDL: Count ico_%d]" % (i+1),
                  'object_name' : "ico_%d" % (i+1),
                  'plotting_enabled' : True,
                  'reaction_name' : "",
                  'region_name' : "",
                  'rxn_or_mol' : "MDLString"
                } )


    # Create a molecule list and create a "vm" molecule along with its display properties in that list
    dm['mcell']['define_molecules'] = { 'data_model_version' : "DM_2014_10_24_1638" }
    mol = { 'mol_name':"vm", 'mol_type':"3D", 'diffusion_constant':"dc", 'data_model_version':"DM_2016_01_13_1930" }
    mol['display'] = {'color':[0.0,1.0,0.0], 'emit':1.0, 'glyph':"Cube", 'scale':0.5 }
    dm['mcell']['define_molecules']['molecule_list'] = [ mol ]


    # Create a release site
    dm['mcell']['release_sites'] = {
      'data_model_version' : "DM_2014_10_24_1638",
      'release_site_list' : [
        {
          'molecule' : "vm",
          'quantity' : "nrel",
          'location_x' : "0",
          'location_y' : "0",
          'location_z' : "0",
          'shape' : "SPHERICAL",
          'site_diameter' : "0",
          'stddev' : "0",
          'name' : "release",
          'object_expr' : "",
          'orient' : ";",
          'pattern' : "",
          'points_list' : [],
          'quantity_type' : "NUMBER_TO_RELEASE",
          'release_probability' : "1",
          'data_model_version' : "DM_2015_11_11_1717"
        }
      ]
    }


    # Set up the simulation running parameters

    dm['mcell']['initialization'] = { 'data_model_version':"DM_2014_10_24_1638" }
    dm['mcell']['initialization']['iterations'] = "iters"
    dm['mcell']['initialization']['time_step'] = "dt"

    dm['mcell']['simulation_control'] = { 'data_model_version': 'DM_2016_04_15_1430' }
    dm['mcell']['simulation_control']['start_seed'] = '1'
    dm['mcell']['simulation_control']['end_seed'] = 'seeds'


    # Return to the previous directory and replace the existing data model with this modified version

    cb.cd_to_location ( old_location )
    cb.replace_data_model ( dm, geometry=True )



Initialization
---------------------------------------------

The first part of the script imports the needed modules, gets a copy of the data model, and prints some keys from the data model.
This section is pretty self-explanatory. The directory change isn't needed in this example, because the script doesn't read or
create any files. But it's included here as good practice.

::

    # Import cellblender to get the data model and project directory functions

    import math
    import cellblender as cb

    # Get a copy of the data model and change directories to the project directory for any file I/O

    dm = cb.get_data_model(geometry=True)
    old_location = cb.cd_to_project()

    # Print some information about the data model

    print ( "###############################################################" )

    print ( "Data Model Top Level Keys = " + str(dm.keys()) )
    print ( "MCell Keys = " + str(dm['mcell'].keys()) )

    print ( "###############################################################" )



Collecting Parameters
---------------------------------------------

The next section of the script uses a common CellBlender scripting idiom for setting and/or obtaining various
parameters. The parameters are defined in a Python list of lists. The fields in each list are implied to be
the parameter **name**, **value**, **units**, and **description**. The code then reads through the data model
(which may or may not contain these same values in the parameters section) and replaces the defaults with any
current values set by the user. If this is the first run of this script in an empty CellBlender model, then
none will be found, and the defaults will remain unchanged. Then the script uses these possibly updated values
to create local variables that can be used later by the script. It then creates a new data model containing an
"mcell" key, and fills its parameter_system dictionary with the possibly updated parameters in the list of lists.

::

    # Define parameters and set default values (these will also be available as local variables in this script)
    #  The format for each parameter is:   Name, Value, Units, Description
    #    All values are given as strings!!!

    pars = [
      # These control the geometry of the model
      ['n',    "3",       '#',   'Number of shells to sample'],
      ['dr',   "0.1",    'um',   'Delta Radius of each successive shell'],
      ['ss',   "2",       '#',   'Surface Smoothness of each shell'],
      # These describe the behavior of the model
      ['dc',    "1e-6",   'cm^2/sec',    'Diffusion Constant of Molecules'],
      ['nrel',  "1000",   'Count',       'Number of molecules to release'],
      # These control the simulation itself
      ['iters', "600",   '',      'Number of iterations to run'],
      ['seeds', "1",     '',      'Number of seeds to run'],
      ['dt',    "1e-6",  'sec',   'Time step for each iteration of the simulation'],
     ]

    # Update local parameter list values from the existing data model with user-modified settings BEFORE regenerating it
    dm_par_list = dm['mcell']['parameter_system']['model_parameters']
    for dm_par in dm_par_list:
        print ( "Data Model Parameter " + dm_par['par_name'] + " = " + dm_par['par_expression'] )
        for p in pars:
            if dm_par['par_name'] == p[0]:
                # Update the local expression based on the parameter found in the incoming data model
                p[1] = dm_par['par_expression']
                p[2] = dm_par['par_units']
                p[3] = dm_par['par_description']

    # Create the local variables from the updated values to use in this script
    for p in pars:
        locals()[p[0]] = eval(p[1])

    # Create the new mcell data model inside the existing data model (this deletes the previous mcell data model)
    dm['mcell'] = { 'data_model_version' : "DM_2014_10_24_1638" }


    # Restore the parameters that were either initialized from scratch or preserved from the previous data model
    dm['mcell']['parameter_system'] = { 'model_parameters':[] }   # Parameters are currently unversioned
    for p in pars:
        dm['mcell']['parameter_system']['model_parameters'].append ( { 'par_name':p[0], 'par_expression':p[1], 'par_units':p[2], 'par_description':p[3] } )



Defining Geometry Support Classes
---------------------------------------------

This next section is probably the most model-specific portion of the script. It generates the
geometrical objects needed for the model. In some cases, this geometrical data can simply be
read from a file. In other cases, it can use some of Blender's internal mesh functions. In still
other cases, it might just assume that the proper geometrical objects have already been created.

Creating mesh objects from scratch can be somewhat tedious. For this model, we'll need a series
of concentric spheres for counting. It turns out the Blender has a built-in function that could
create these spheres (or more properly, icospheres) for us. But that's certainly not the case for
all geometrical objects. So this code shows how it can be done from scratch. This entire section
is written to support a simple call to make an icosphere:

::

    ico = IcoSphere(ss,r,r,r).make_dm_object ( 0, 0, 0 )

The result should be a dictionary of points and faces representing the icosphere in data model format.
This particular example starts by building an icosahedron with 12 points and 20 faces. The algorithm
then recursively subdivides each face into 4 smaller faces. The new points are then renormalized to be
on the sphere and the process is repeated until the desired number of subdivisions has been reached.

The algorithm uses its own internal representation of points and faces (the point and face classes).
Eventually it calls the "make_dm_object" to convert that internal representation into a CellBlender
data model compatible dictionary named "obj" that it returns.

::

    ##################################
    #   Geometry  Support  Classes   #
    ##################################

    class point:

      def __init__ ( self, x, y, z ):
        self.x = x;
        self.y = y;
        self.z = z;


    class face:
      
      def __init__ ( self, v1, v2, v3 ):
        self.verts = [];
        self.verts.append ( v1 );
        self.verts.append ( v2 );
        self.verts.append ( v3 );
      

    class IcoSphere:

      # Builds an icosphere with recursion
      
      def __init__ ( self ):
        self.points = []
        self.faces = []
      
      def make_dm_object ( self, center_x=0, center_y=0, center_z=0 ):
        obj = {}
        obj['vertex_list'] = []
        obj['element_connections'] = []

        for p in self.points:
          obj['vertex_list'].append ( [ center_x+p.x, center_y+p.y, center_z+p.z ] )
        for f in self.faces:
          obj['element_connections'].append ( f.verts )

        return obj

      def add_normalized_vertex ( self, p ):
        # Normalize the point
        # Add to the list of points if it's not already in the list
        # Return an index to the new or existing point in the list

        l = math.sqrt ( (p.x * p.x) + (p.y * p.y) + (p.z * p.z) );
        pnorm = point ( p.x/l, p.y/l, p.z/l );

        # Check if it's already there
        index = -1;
        for pt in self.points:
          if (pt.x == pnorm.x) and (pt.y == pnorm.y) and (pt.z == pnorm.z):
            index = self.points.index(pt)
            break;

        if (index < 0):
          self.points.append ( pnorm );
          index = self.points.index ( pnorm );
          #print ( "Added vertex at " + str(index) );
        #else:
        #  print ( "Found vertex at " + str(index) );
        return (index);


      def __init__ ( self, recursion_level, scale_x=1.0, scale_y=1.0, scale_z=1.0 ):

        self.points = [];

        t = (1.0 + math.sqrt(5.0)) / 2.0;  # Approx 1.618033988749895
        
        # Create 12 verticies from the 3 perpendicular planes whose corners define an icosahedron

        self.add_normalized_vertex ( point (-1,  t,  0) );
        self.add_normalized_vertex ( point ( 1,  t,  0) );
        self.add_normalized_vertex ( point (-1, -t,  0) );
        self.add_normalized_vertex ( point ( 1, -t,  0) );

        self.add_normalized_vertex ( point ( 0, -1,  t) );
        self.add_normalized_vertex ( point ( 0,  1,  t) );
        self.add_normalized_vertex ( point ( 0, -1, -t) );
        self.add_normalized_vertex ( point ( 0,  1, -t) );

        self.add_normalized_vertex ( point ( t,  0, -1) );
        self.add_normalized_vertex ( point ( t,  0,  1) );
        self.add_normalized_vertex ( point (-t,  0, -1) );
        self.add_normalized_vertex ( point (-t,  0,  1) );
        
        
        # Rotate all points such that the resulting icosphere will be separable at the equator
        
        if (True):
          # A PI/6 rotation about z (transform x and y) gives an approximate equator in x-y plane
          angle = (math.pi / 2) - math.atan(1/t);
          # print ( "Rotating with angle = " + str(180 * angle / math.pi) );
          for p in self.points:
            newx = (math.cos(angle) * p.x) - (math.sin(angle) * p.z);
            newz = (math.sin(angle) * p.x) + (math.cos(angle) * p.z);
            p.x = newx;
            p.z = newz;

        # Build the original 20 faces for the Icosphere

        self.faces = []

        # Add 5 faces around point 0 (top)
        self.faces.append ( face (  0, 11,  5 ) );    
        self.faces.append ( face (  0,  5,  1 ) );    
        self.faces.append ( face (  0,  1,  7 ) );    
        self.faces.append ( face (  0,  7, 10 ) );    
        self.faces.append ( face (  0, 10, 11 ) );    

        # Add 5 faces adjacent faces
        self.faces.append ( face (  1,  5,  9 ) );    
        self.faces.append ( face (  5, 11,  4 ) );    
        self.faces.append ( face ( 11, 10,  2 ) );    
        self.faces.append ( face ( 10,  7,  6 ) );    
        self.faces.append ( face (  7,  1,  8 ) );    

        # Add 5 faces around point 3 (bottom)
        self.faces.append ( face (  3,  9,  4 ) );    
        self.faces.append ( face (  3,  4,  2 ) );    
        self.faces.append ( face (  3,  2,  6 ) );    
        self.faces.append ( face (  3,  6,  8 ) );    
        self.faces.append ( face (  3,  8,  9 ) );    

        # Add 5 faces adjacent faces
        self.faces.append ( face (  4,  9,  5 ) );    
        self.faces.append ( face (  2,  4, 11 ) );    
        self.faces.append ( face (  6,  2, 10 ) );    
        self.faces.append ( face (  8,  6,  7 ) );    
        self.faces.append ( face (  9,  8,  1 ) );
        

        # Subdivide the faces as requested by the recursion_level argument
        old_points = None;
        old_faces = None;
        
        for rlevel in range(recursion_level):
          # System.out.println ( "\nRecursion Level = " + rlevel );
          # Save the old points and faces and build a new set for this recursion level
          old_points = self.points;
          old_faces = self.faces;
          self.points = []
          self.faces = []
          for f in old_faces:
            # Split this face into 4 more faces
            midpoint = point(0,0,0)
            potential_new_points = []
            for i in range(6):
              potential_new_points.append ( point(0,0,0) )
            for side in range(3):
              p1 = old_points[f.verts[side]];
              p2 = old_points[f.verts[(side+1)%3]];
              midpoint = point ( ((p1.x+p2.x)/2), ((p1.y+p2.y)/2), ((p1.z+p2.z)/2) );
              potential_new_points[2*side] = p1;
              potential_new_points[(2*side)+1] = midpoint;
            # Add the 4 new faces
            # Start with the verticies ... add them all since add_normalized_vertex() will remove duplicates
            vertex_indicies = []
            for i in range(6):
              vertex_indicies.append ( 0 )
            for i in range(6):
              vertex_indicies[i] = self.add_normalized_vertex ( potential_new_points[i] );
            # Now add the 4 new faces
            self.faces.append ( face ( vertex_indicies[0], vertex_indicies[1], vertex_indicies[5] ) );
            self.faces.append ( face ( vertex_indicies[1], vertex_indicies[2], vertex_indicies[3] ) );
            self.faces.append ( face ( vertex_indicies[3], vertex_indicies[4], vertex_indicies[5] ) );
            self.faces.append ( face ( vertex_indicies[1], vertex_indicies[3], vertex_indicies[5] ) );

        for pt in self.points:
          pt.x *= scale_x
          pt.y *= scale_y
          pt.z *= scale_z




Creating Materials, Containers, and a Transparent Surface Class
-------------------------------------------------------------------------------

Building a data model is mostly making dictionaries and lists with CellBlender's expected keys.
In this next section of code, new dictionaries are made for materials, geometrical objects, and
model objects. These will all be filled by looping in subsequent sections of this script. Since
a transparent surface class will be needed, it's created here as well. Note the pattern of setting
up empty lists that will be filled in later.

::

    # Add materials for the objects
    dm['mcell']['materials'] = { 'material_dict' : {} }   # Materials are currently unversioned
    dm['mcell']['materials']['material_dict']['shell_color']   = { 'diffuse_color' : {'a':0.3, 'r':0.2, 'g':0.4, 'b':1.0} }


    # Create container objects for geometrical objects and model objects
    dm['mcell']['geometrical_objects'] = {}   # Geometrical objects are currently unversioned
    dm['mcell']['model_objects'] = { 'data_model_version':"DM_2014_10_24_1638" }

    # Each container also includes a list
    dm['mcell']['geometrical_objects']['object_list'] = []
    dm['mcell']['model_objects']['model_object_list'] = []

    # Create a transparent surface class
    dm['mcell']['define_surface_classes'] = {
      'data_model_version' : "DM_2014_10_24_1638",
      'surface_class_list' : [
        {
          'data_model_version' : "DM_2014_10_24_1638",
          'name' : "transp",
          'surface_class_prop_list' : [
            {
              'affected_mols' : "ALL_MOLECULES",
              'clamp_value' : "0",
              'data_model_version' : "DM_2015_11_08_1756",
              'molecule' : "",
              'name' : "Molec.: ALL_MOLECULES   Orient.: Ignore   Type: Transparent",
              'surf_class_orient' : ";",
              'surf_class_type' : "TRANSPARENT"
            }
          ]
        }
      ]
    }



Building Containers for Surface Regions and Counting
-------------------------------------------------------------------------------

The model will also need to modify surface regions to make them transparent and it will
need to generate count statements. Again, the empty list structures are created to be
filled in later.

::

    # Define the Modify Surface Regions structure
    dm['mcell']['modify_surface_regions'] = {
      'data_model_version' : "DM_2014_10_24_1638",
      'modify_surface_regions_list' : []
    }

    # Define the count/plot structure
    dm['mcell']['reaction_data_output'] = {
      'always_generate' : True,
      'combine_seeds' : True,
      'data_model_version' : "DM_2016_03_15_1800",
      'mol_colors' : False,
      'plot_layout' : " ",
      'plot_legend' : "0",
      'reaction_output_list' : [],
      'rxn_step' : ""
    }
      


Looping to build Geometrical Objects, assign Surface Classes, and make Count Statements
---------------------------------------------------------------------------------------

Now that all of the empty "containers" have been set up, this section of code
can loop through the requested number of measuring shells and do the following
things:

  * Create the geometry (icosphere) for each shell
  * Name each icosphere
  * Assign a material to each icosphere
  * Append each icosphere to the geometrical objects list and the model objects list
  * Apply a surface region modification to make each icosphere transparent to all molecules
  * Create a Count statement for each icosphere that subtracts the count of the previous (inner) icosphere

That's a lot of tasks, but they're easily accomplished because everything has already been
set up.


::

    # Make a series of transparent icospheres and define a count statement for each one
    for i in range(n):
        r = (i+1) * dr
        ico = IcoSphere(ss,r,r,r).make_dm_object ( 0, 0, 0 )
        ico['name'] = 'ico_' + str(i+1)
        ico['material_names'] = [ 'shell_color' ]
        dm['mcell']['geometrical_objects']['object_list'].append ( ico )
        dm['mcell']['model_objects']['model_object_list'].append ( { 'name':ico['name'] } )
        dm['mcell']['modify_surface_regions']['modify_surface_regions_list'].append ( {
                  'data_model_version' : "DM_2015_11_06_1732",
                  'name' : "Surface Class: transp   Object: ico_%d   ALL" % (i+1),
                  'object_name' : "ico_%d" % (i+1),
                  'region_name' : "",
                  'region_selection' : "ALL",
                  'surf_class_name' : "transp"
                } )
        mdl_string = "COUNT[vm,Scene.ico_%d]" % (i+1)
        if i > 0:
            mdl_string += " - COUNT[vm,Scene.ico_%d]" % (i)
        dm['mcell']['reaction_data_output']['reaction_output_list'].append ( {
                  'count_location' : "Object",
                  'data_file_name' : "",
                  'data_model_version' : "DM_2016_03_15_1800",
                  'mdl_file_prefix' : "ico_%d" % (i+1),
                  'mdl_string' : mdl_string,
                  'molecule_name' : "vm",
                  'name' : "MDL: Count ico_%d]" % (i+1),
                  'object_name' : "ico_%d" % (i+1),
                  'plotting_enabled' : True,
                  'reaction_name' : "",
                  'region_name' : "",
                  'rxn_or_mol' : "MDLString"
                } )



Defining Molecules and a Release Site
---------------------------------------------

Since this model only has one molecule and one release site, these can be created directly.

::

    # Create a molecule list and create a "vm" molecule along with its display properties in that list
    dm['mcell']['define_molecules'] = { 'data_model_version' : "DM_2014_10_24_1638" }
    mol = { 'mol_name':"vm", 'mol_type':"3D", 'diffusion_constant':"dc", 'data_model_version':"DM_2016_01_13_1930" }
    mol['display'] = {'color':[0.0,1.0,0.0], 'emit':1.0, 'glyph':"Cube", 'scale':0.5 }
    dm['mcell']['define_molecules']['molecule_list'] = [ mol ]


    # Create a release site
    dm['mcell']['release_sites'] = {
      'data_model_version' : "DM_2014_10_24_1638",
      'release_site_list' : [
        {
          'molecule' : "vm",
          'quantity' : "nrel",
          'location_x' : "0",
          'location_y' : "0",
          'location_z' : "0",
          'shape' : "SPHERICAL",
          'site_diameter' : "0",
          'stddev' : "0",
          'name' : "release",
          'object_expr' : "",
          'orient' : ";",
          'pattern' : "",
          'points_list' : [],
          'quantity_type' : "NUMBER_TO_RELEASE",
          'release_probability' : "1",
          'data_model_version' : "DM_2015_11_11_1717"
        }
      ]
    }



Defining Simulation Run Parameters and Replacing the Data Model
-------------------------------------------------------------------------------

The final step is setting up the initialization and run control sections. Note that the
parameters "iters" and "dt" and "seeds" are given as string expressions. These refer to
the parameters that have already been added to the data model. This will allow these to
be changed easily from the parameter panel each time the simulation is re-run.

The last two calls restore the default directory location to the location saved at the
top of this script and replace the CellBlender data model with the data model that we
built in this script. Once that last call has returned, all of CellBlender's properties
will have been replaced with values from the data model that we built in this script.

::

    # Set up the simulation running parameters

    dm['mcell']['initialization'] = { 'data_model_version':"DM_2014_10_24_1638" }
    dm['mcell']['initialization']['iterations'] = "iters"
    dm['mcell']['initialization']['time_step'] = "dt"

    dm['mcell']['simulation_control'] = { 'data_model_version': 'DM_2016_04_15_1430' }
    dm['mcell']['simulation_control']['start_seed'] = '1'
    dm['mcell']['simulation_control']['end_seed'] = 'seeds'


    # Return to the previous directory and replace the existing data model with this modified version

    cb.cd_to_location ( old_location )
    cb.replace_data_model ( dm, geometry=True )



