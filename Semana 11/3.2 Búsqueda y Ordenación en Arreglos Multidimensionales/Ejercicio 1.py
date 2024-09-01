# matriz bidimensional (3x3)
matriz = [
    [20, 25, 35],
    [4, 5, 6],
    [10, 38, 69]
]

# Definir la función de búsqueda
def buscar_en_matriz(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return f"Valor {valor_buscado} encontrado en la posición ({i}, {j})"
    return f"Valor {valor_buscado} no encontrado en la matriz"

# el valor a buscar
valor_buscado = 38

# Llamar la Matriz y mostrar el resultado
resultado = buscar_en_matriz(matriz, valor_buscado)
print(matriz)
print(resultado)
