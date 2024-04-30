import numpy as np
import pandas as pd

# Cargar el archivo .npy
data = np.load('voxel_grid_Cube.npy')

np.savetxt('voxel_data', data)
