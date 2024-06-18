import numpy as np

# Definir dos matrices de ejemplo


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


# final matrix to voxel
result_matrix = np.ones((8,10,6))


# Print Final Matrix shape
print("Matriz resultante:")
print(result_matrix.shape)

result_matrix = rotate_90_XZ(result_matrix)
print(result_matrix.shape)

obj_name = "AUV_5D"

np.save(f"voxel_grid_{obj_name}.npy",result_matrix)




