# Definir una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)

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

# Calcular el promedio de temperaturas por ciudad y semana
promedios_por_ciudad = []

# Iterar a través de las ciudades, semanas y días para calcular el promedio de temperaturas
for ciudad in temperaturas:  # Iterar sobre cada ciudad en temperaturas
    promedio_semanal = []
    suma_total = 0
    cantidad_total = 0
    for semana in ciudad:  # Iterar sobre cada semana en la ciudad
        suma_semanal = 0
        cantidad_semanal = 0
        for dia in semana:  # Iterar sobre cada día en la semana
            suma_semanal += dia['Temp']
            cantidad_semanal += 1
            suma_total += dia['Temp']
            cantidad_total += 1
        promedio = suma_semanal / cantidad_semanal  # Calcular el promedio de la semana
        promedio_semanal.append(promedio)
    promedio_ciudad = suma_total / cantidad_total  # Calcular el promedio de la ciudad
    promedios_por_ciudad.append((promedio_semanal, promedio_ciudad))

# Mostrar el promedio de temperaturas para cada ciudad y semana
for i, (promedio_semanal, promedio_ciudad) in enumerate(promedios_por_ciudad):
    print(f"\nCiudad {i + 1}:")
    print(f"Promedio general de la ciudad: {promedio_ciudad:.2f}" "°C")
    for j, promedio in enumerate(promedio_semanal):
        print(f"Promedio de la Semana {j + 1}: {promedio:.2f}" "°C")

# Menú para seleccionar ciudad y mostrar solo el promedio general
while True:
    print("\nSeleccione una ciudad:")
    print("1. Ciudad Guayaquil ")
    print("2. Ciudad Quito")
    print("3. Ciudad Puyo")
    print("4. Salir")

    option = input("Ingrese la Ciudad: ")
    if option == "1":
        print(f"\nPromedio general de la Temperatura de Guayaquil : {promedios_por_ciudad[0][1]:.2f}" "°C")
    elif option == "2":
        print(f"\nPromedio general de la Temperatura de Quito: {promedios_por_ciudad[1][1]:.2f}""°C")
    elif option == "3":
        print(f"\nPromedio general de la Temperatura de Puyo: {promedios_por_ciudad[2][1]:.2f}""°C")
    elif option == "4":
        print("SALIR...")
        break
    else:
        print("Opción no válida, intenta de nuevo")