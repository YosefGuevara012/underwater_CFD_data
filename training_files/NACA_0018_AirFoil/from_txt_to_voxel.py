import numpy as np

# Definir dos matrices de ejemplo
middle_matrix = np.array([
				 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1]])

layer1_matrix = np.array([
				 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [0],
                 [0]])
				 
layer2_matrix = np.array([
				 [0],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [0],
                 [0],
                 [0],
                 [0],
                 [0],
                 [0]])

layer3_matrix = np.array([
				 [0],
                 [0],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [1],
                 [0],
                 [0],
                 [0],
                 [0],
                 [0],
                 [0],
                 [0],
                 [0],
                 [0],
                 [0],
                 [0]])

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
result_matrix = np.stack((
                          layer3_matrix,layer2_matrix,layer1_matrix,
                          middle_matrix, 
                          layer1_matrix, layer2_matrix,layer3_matrix), axis=0)

n = 30
result_matrix = np.tile(result_matrix, (1,1,n))


# Print Final Matrix shape
print("Matriz resultante:")
print(result_matrix.shape)

result_matrix = rotate_180_XY(rotate_90_YZ(rotate_90_XY(result_matrix))) # Proper orientation for surge motion 
# result_matrix = rotate_180_XY(result_matrix) # Proper orientation for heave motion 
print(result_matrix.shape)

obj_name = "Airfoil_L"

np.save(f"voxel_grid_{obj_name}.npy",result_matrix)




