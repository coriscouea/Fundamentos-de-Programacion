# Definir una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "Temp": 30},
            {"day": "Martes", "Temp": 32},
            {"day": "Miércoles", "Temp": 28},
            {"day": "Jueves", "Temp": 30},
            {"day": "Viernes", "Temp": 31},
            {"day": "Sábado", "Temp": 32},
            {"day": "Domingo", "Temp": 29}
        ],
        [  # Semana 2
            {"day": "Lunes", "Temp": 27},
            {"day": "Martes", "Temp": 29},
            {"day": "Miércoles", "Temp": 30},
            {"day": "Jueves", "Temp": 28},
            {"day": "Viernes", "Temp": 28},
            {"day": "Sábado", "Temp": 29},
            {"day": "Domingo", "Temp": 30}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 33},
            {"day": "Martes", "Temp": 31},
            {"day": "Miércoles", "Temp": 30},
            {"day": "Jueves", "Temp": 31},
            {"day": "Viernes", "Temp": 32},
            {"day": "Sábado", "Temp": 30},
            {"day": "Domingo", "Temp": 31}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 26},
            {"day": "Martes", "Temp": 29},
            {"day": "Miércoles", "Temp": 28},
            {"day": "Jueves", "Temp": 30},
            {"day": "Viernes", "Temp": 31},
            {"day": "Sábado", "Temp": 28},
            {"day": "Domingo", "Temp": 30}
        ]
    ],
    [  # Ciudad 2 Quito
        [  # Semana 1
            {"day": "Lunes", "Temp": 14},
            {"day": "Martes", "Temp": 10},
            {"day": "Miércoles", "Temp": 11},
            {"day": "Jueves", "Temp": 12},
            {"day": "Viernes", "Temp": 13},
            {"day": "Sábado", "Temp": 14},
            {"day": "Domingo", "Temp": 9}
        ],
        [  # Semana 2
            {"day": "Lunes", "Temp": 8},
            {"day": "Martes", "Temp": 9},
            {"day": "Miércoles", "Temp": 11},
            {"day": "Jueves", "Temp": 10},
            {"day": "Viernes", "Temp": 11},
            {"day": "Sábado", "Temp": 10},
            {"day": "Domingo", "Temp": 12}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 12},
            {"day": "Martes", "Temp": 13},
            {"day": "Miércoles", "Temp": 14},
            {"day": "Jueves", "Temp": 16},
            {"day": "Viernes", "Temp": 15},
            {"day": "Sábado", "Temp": 14},
            {"day": "Domingo", "Temp": 13}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 15},
            {"day": "Martes", "Temp": 10},
            {"day": "Miércoles", "Temp": 16},
            {"day": "Jueves", "Temp": 12},
            {"day": "Viernes", "Temp": 13},
            {"day": "Sábado", "Temp": 14},
            {"day": "Domingo", "Temp": 14}
        ]
    ],
    [  # Ciudad 3 Puyo
        [  # Semana 1
            {"day": "Lunes", "Temp": 22},
            {"day": "Martes", "Temp": 24},
            {"day": "Miércoles", "Temp": 26},
            {"day": "Jueves", "Temp": 25},
            {"day": "Viernes", "Temp": 27},
            {"day": "Sábado", "Temp": 28},
            {"day": "Domingo", "Temp": 25}
        ],
        [  # Semana 2
            {"day": "Lunes", "Temp": 24},
            {"day": "Martes", "Temp": 26},
            {"day": "Miércoles", "Temp": 25},
            {"day": "Jueves", "Temp": 24},
            {"day": "Viernes", "Temp": 23},
            {"day": "Sábado", "Temp": 26},
            {"day": "Domingo", "Temp": 27}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 25},
            {"day": "Martes", "Temp": 27},
            {"day": "Miércoles", "Temp": 28},
            {"day": "Jueves", "Temp": 29},
            {"day": "Viernes", "Temp": 28},
            {"day": "Sábado", "Temp": 27},
            {"day": "Domingo", "Temp": 26}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 25},
            {"day": "Martes", "Temp": 26},
            {"day": "Miércoles", "Temp": 27},
            {"day": "Jueves", "Temp": 28},
            {"day": "Viernes", "Temp": 29},
            {"day": "Sábado", "Temp": 28},
            {"day": "Domingo", "Temp": 25}
        ]
    ]
]

# Función para calcular los promedios de temperatura
def calcular_promedios(temperaturas):
    """
    Calcula el promedio de temperatura semanal y general para cada ciudad.

    Args:
        temperaturas (list): Lista 3D que contiene las temperaturas diarias de cada ciudad, organizada por semanas.

    Returns:
        list: Lista de tuplas que contiene los promedios semanales y el promedio general para cada ciudad.
    """
    promedios_por_ciudad = []

    # Recorre cada ciudad en la lista de temperaturas
    for ciudad in temperaturas:
        # Calcula el promedio semanal para cada semana
        promedio_semanal = [sum(dia['Temp'] for dia in semana) / len(semana) for semana in ciudad]
        # Calcula el promedio general de la ciudad a partir de los promedios semanales
        promedio_ciudad = sum(promedio_semanal) / len(promedio_semanal)
        # Añade los promedios calculados a la lista
        promedios_por_ciudad.append((promedio_semanal, promedio_ciudad))

    return promedios_por_ciudad

# Función para imprimir los promedios de temperatura para cada ciudad
def imprimir_promedios(promedios_por_ciudad, ciudades):
    """
    Imprime los promedios de temperatura semanal y general para cada ciudad.

    Args:
        promedios_por_ciudad (list): Lista de tuplas con los promedios semanales y el promedio general de cada ciudad.
        ciudades (list): Lista de nombres de las ciudades.
    """
    for index, ciudad in enumerate(ciudades):
        promedio_semanal, promedio_ciudad = promedios_por_ciudad[index]
        print(f"\nCiudad {ciudad}:")
        print(f"Promedio general de la ciudad: {promedio_ciudad:.2f}°C")
        for j, promedio in enumerate(promedio_semanal):
            print(f"Promedio de la Semana {j + 1}: {promedio:.2f}°C")

# Función para mostrar un menú interactivo que permite seleccionar una ciudad
def mostrar_menu(promedios_por_ciudad, ciudades):
    """
    Muestra un menú para seleccionar una ciudad y ver el promedio general de temperatura de la misma.

    Args:
        promedios_por_ciudad (list): Lista de tuplas con los promedios semanales y el promedio general de cada ciudad.
        ciudades (list): Lista de nombres de las ciudades.
    """
    while True:
        print("\nSeleccione una ciudad:")
        # Muestra las opciones de las ciudades en el menú
        for i, ciudad in enumerate(ciudades, 1):
            print(f"{i}. Ciudad {ciudad}")
        print(f"{len(ciudades) + 1}. Salir")

        # Lee la opción seleccionada por el usuario
        option = input("Ingrese el número de la ciudad: ")
        if option.isdigit() and 1 <= int(option) <= len(ciudades):
            index = int(option) - 1
            promedio_ciudad = promedios_por_ciudad[index][1]
            print(f"\nPromedio general de la Ciudad {ciudades[index]}: {promedio_ciudad:.2f}°C")
        elif option == str(len(ciudades) + 1):
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Definir los nombres de las ciudades
ciudades = ['Guayaquil', 'Quito', 'Puyo']

# Calcular los promedios de temperatura para cada ciudad
promedios_por_ciudad = calcular_promedios(temperaturas)

# Imprimir los promedios de temperatura
imprimir_promedios(promedios_por_ciudad, ciudades)

# Mostrar el menú interactivo
mostrar_menu(promedios_por_ciudad, ciudades)
