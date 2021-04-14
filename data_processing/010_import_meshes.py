import os
from compas.datastructures import Mesh
from compas.utilities import i_to_rgb

from compas_view2.app import App

# ==============================================================================
# File
# ==============================================================================
HERE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILE_FOLDER = os.path.join(HERE, 'data', 'cat_seed_1')
# FILE_I = os.path.join(HERE, 'data', 'cube_6/Cube_shard.obj')

# initialize viewer
viewer = App()

file_nums = len(os.listdir(FILE_FOLDER))
print(file_nums)

# calculate the total vertices
total_vertices = 0
for i, filename in enumerate(os.listdir(FILE_FOLDER)):
    if filename.endswith(".obj"): 
        FILE_I = os.path.join(FILE_FOLDER, filename)
        mesh = Mesh.from_obj(FILE_I)
        if "shard" in filename:
            len_vertices = len(list(mesh.vertices()))
            print(len_vertices)
            total_vertices += len_vertices
            viewer.add(mesh, facecolor=i_to_rgb(i/file_nums, True))
        else:
            print("Input mesh vertices:", len(list(mesh.vertices())))

print("Total fracture vertices:", total_vertices)

# ==============================================================================
# Viz
# ==============================================================================
viewer.run()