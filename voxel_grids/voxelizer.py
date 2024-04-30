import bpy
import numpy as np

# Obtener el objeto activo (asegúrate de que tu objeto está seleccionado)
obj_name = "AUV"
obj = bpy.data.objects[obj_name]

# Lista para almacenar las coordenadas de los vértices
vertices = []

# Asegurarse de que estamos usando datos de malla
if obj.type == 'MESH':
    # Acceso a los vértices del objeto
    mesh = obj.data
    for vertex in mesh.vertices:
        # Agrega las coordenadas del vértice a la lista
        vertices.append(vertex.co[:])  # [:] para copiar la tupla

    # Convertir la lista a un array de NumPy
    vertex_array = np.array(vertices)

    # Guardar el array en un archivo .npy
    np.save(f"voxel_grids/voxel_grid_{obj_name}.npy", vertex_array)
    print("Datos de vértices guardados en 'vertex_data.npy'")
else:
    print("El objeto seleccionado no es una malla.")

