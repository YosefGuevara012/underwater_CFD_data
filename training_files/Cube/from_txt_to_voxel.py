import numpy as np

n = 16
result_matrix = np.ones((n,n,n)) #Ensures a flat fin of 1m x 1m

obj_name = "Cube_" + str(n) + "D"

np.save(f"voxel_grid_{obj_name}.npy",result_matrix)




