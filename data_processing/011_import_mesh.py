import os
from compas.datastructures import Mesh
from compas.utilities import i_to_rgb

from compas_view2.app import App

# ==============================================================================
# File
# ==============================================================================
HERE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILE_FOLDER = os.path.join(HERE, 'data', 'cube_6')
FILE_I = os.path.join(HERE, 'data', 'cube_6/Cube_shard.obj')


# ==============================================================================
# Mesh
# ==============================================================================
mesh = Mesh.from_obj(FILE_I)


# ==============================================================================
# Viz
# ==============================================================================
viewer = App()
viewer.add(mesh)
viewer.run()