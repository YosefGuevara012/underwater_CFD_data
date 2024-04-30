import numpy as np

voxel_grid = np.load("voxel_grid_AUV.npy")

print(f"voxel_grid.shape: {voxel_grid.shape}")


for dimention in voxel_grid:

    print("------------------------------------------------------------")
    print(dimention)
