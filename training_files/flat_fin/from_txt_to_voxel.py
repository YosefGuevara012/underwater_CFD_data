import numpy as np

result_matrix = np.ones((3,22,22)) #Ensures a flat fin of 1m x 1m

print(result_matrix.shape)

# Función para rotar una matriz multidimensional en 90 grados en el plano XY
def rotate_90_XY(matrix):
    return np.rot90(matrix, axes=(0, 1))

# Función para rotar una matriz multidimensional en 90 grados en el plano XZ
def rotate_90_XZ(matrix):
    return np.rot90(matrix, axes=(0, 2))

# Función para rotar una matriz multidimensional en 90 grados en el plano YZ
def rotate_90_YZ(matrix):
    return np.rot90(matrix, axes=(1, 2))

# Función para rotar una matriz multidimensional en 180 grados en el plano XY
def rotate_180_XY(matrix):
    return np.rot90(matrix, k=2, axes=(0, 1))

# Función para rotar una matriz multidimensional en 180 grados en el plano XZ
def rotate_180_XZ(matrix):
    return np.rot90(matrix, k=2, axes=(0, 2))

# Función para rotar una matriz multidimensional en 180 grados en el plano YZ
def rotate_180_YZ(matrix):
    return np.rot90(matrix, k=2, axes=(1, 2))



# Print Final Matrix shape
print("Matriz resultante:")
print(result_matrix.shape)

# result_matrix = rotate_180_XY(rotate_90_YZ(rotate_90_XY(result_matrix))) # Proper orientation for surge motion 
result_matrix = rotate_180_XY(result_matrix) # Proper orientation for heave motion 
print(result_matrix.shape)

obj_name = "flat_fin_h"

np.save(f"voxel_grid_{obj_name}.npy",result_matrix)




