import os
from compas.datastructures import Mesh
from compas.utilities import i_to_rgb

from compas_view2.app import App

# ==============================================================================
# File
# ==============================================================================
HERE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILE_FOLDER = os.path.join(HERE, 'data', 'cube_6')
# FILE_I = os.path.join(HERE, 'data', 'cube_6/Cube_shard.obj')

# initialize viewer
viewer = App()

file_nums = len(os.listdir(FILE_FOLDER))
print(file_nums)
for i, filename in enumerate(os.listdir(FILE_FOLDER)):
    if filename.endswith(".obj"): 
        FILE_I = os.path.join(FILE_FOLDER, filename)
        mesh = Mesh.from_obj(FILE_I)
        viewer.add(mesh, facecolor=i_to_rgb(i/file_nums, True))



# ==============================================================================
# Viz
# ==============================================================================
viewer.run()
