import bpy
import bmesh
from bpy.types import Operator
from bpy.props import FloatVectorProperty, IntVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add

from mathutils import Matrix
bpy.app.debug = True
bpyscene = bpy.context.scene

# delete all the meshes
# bpy.ops.mesh.select_all(action='DESELECT')
for o in bpyscene.objects:
    if o.type == 'MESH':
        o.select = True
    else:
        o.select = False
bpy.ops.object.delete()

# Create an empty mesh and the object.
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))

# loop through all the objects in the scene
for ob in bpyscene.objects:
    if ob.type == 'MESH':
        # make the current object active and select it
        bpyscene.objects.active = ob
        ob.select = True

ob = bpy.context.active_object

# change to edit mode
if bpy.ops.object.mode_set.poll():
    bpy.ops.object.mode_set(mode='EDIT')
print("Active object = ",ob.name)

me = ob.data
bm = bmesh.new()
bm.from_mesh(me)

# subdivide
bmesh.ops.subdivide_edges(bm,
                          edges=bm.edges,
                          cuts=10,
                          use_grid_fill=True,
                          )

# Write back to the mesh
bpy.ops.mesh.select_all(action='DESELECT')
bm.select_flush(True)

bpy.ops.object.mode_set(mode='OBJECT') # if bmesh.from_edit_mesh() --> mode == EDIT - ValueError: to_mesh(): Mesh 'Cube' is in editmode 
bm.to_mesh(me) #If mode ==Object  -> ReferenceError: BMesh data of type BMesh has been removed
bm.free() 
ob.update_from_editmode()

# modifier = object.modifiers.new(name="Fracture", frac_algorithm='BOOLEAN_FRACTAL')
bpy.ops.object.modifier_add(type='FRACTURE')
md = ob.modifiers["Fracture"]
md.fracture_mode = 'PREFRACTURED'
md.frac_algorithm = 'BOOLEAN_FRACTAL'
md.fractal_cuts = 2
md.fractal_iterations = 4
md.shard_count = 20
md.point_seed = 1  # random seed

bpy.ops.object.fracture_refresh(reset=True)
bpy.ops.object.rigidbody_convert_to_objects()

# deselect all objects
bpy.ops.object.select_all(action='DESELECT')    

# loop through all the objects in the scene
scene = bpy.context.scene
for ob in scene.objects:
    # make the current object active and select it
    scene.objects.active = ob
    ob.select = True

    # make sure that we only export meshes
    if ob.type == 'MESH':
        # export the currently selected object to its own file based on its name
        bpy.ops.export_scene.obj(
                filepath=os.path.join(PATH, ob.name + '.obj'),
                use_selection=True,
                )
    # deselect the object and move on to another if any more are left
    ob.select = False