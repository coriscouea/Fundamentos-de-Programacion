# Definir una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)

temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "Temp": 76},
            {"day": "Martes", "Temp": 80},
            {"day": "Miércoles", "Temp": 90},
            {"day": "Jueves", "Temp": 100},
            {"day": "Viernes", "Temp": 110},
            {"day": "Sábado", "Temp": 120},
            {"day": "Domingo", "Temp": 131}
        ],
        [  # Semana 2
            {"day": "Lunes", "Temp": 50},
            {"day": "Martes", "Temp": 82},
            {"day": "Miércoles", "Temp": 93},
            {"day": "Jueves", "Temp": 106},
            {"day": "Viernes", "Temp": 113},
            {"day": "Sábado", "Temp": 126},
            {"day": "Domingo", "Temp": 151}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 79},
            {"day": "Martes", "Temp": 86},
            {"day": "Miércoles", "Temp": 99},
            {"day": "Jueves", "Temp": 108},
            {"day": "Viernes", "Temp": 115},
            {"day": "Sábado", "Temp": 129},
            {"day": "Domingo", "Temp": 140}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 80},
            {"day": "Martes", "Temp": 92},
            {"day": "Miércoles", "Temp": 100},
            {"day": "Jueves", "Temp": 112},
            {"day": "Viernes", "Temp": 120},
            {"day": "Sábado", "Temp": 130},
            {"day": "Domingo", "Temp": 143}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "Temp": 77},
            {"day": "Martes", "Temp": 81},
            {"day": "Miércoles", "Temp": 91},
            {"day": "Jueves", "Temp": 101},
            {"day": "Viernes", "Temp": 111},
            {"day": "Sábado", "Temp": 121},
            {"day": "Domingo", "Temp": 132}
        ],
        [  # Semana 2
            {"day": "Lunes", "Temp": 80},
            {"day": "Martes", "Temp": 83},
            {"day": "Miércoles", "Temp": 94},
            {"day": "Jueves", "Temp": 107},
            {"day": "Viernes", "Temp": 114},
            {"day": "Sábado", "Temp": 127},
            {"day": "Domingo", "Temp": 137}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 80},
            {"day": "Martes", "Temp": 87},
            {"day": "Miércoles", "Temp": 100},
            {"day": "Jueves", "Temp": 109},
            {"day": "Viernes", "Temp": 117},
            {"day": "Sábado", "Temp": 130},
            {"day": "Domingo", "Temp": 140}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 81},
            {"day": "Martes", "Temp": 93},
            {"day": "Miércoles", "Temp": 101},
            {"day": "Jueves", "Temp": 113},
            {"day": "Viernes", "Temp": 121},
            {"day": "Sábado", "Temp": 134},
            {"day": "Domingo", "Temp": 141}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "Temp": 90},
            {"day": "Martes", "Temp": 91},
            {"day": "Miércoles", "Temp": 101},
            {"day": "Jueves", "Temp": 121},
            {"day": "Viernes", "Temp": 131},
            {"day": "Sábado", "Temp": 141},
            {"day": "Domingo", "Temp": 151}
        ],
        [  # Semana 2
            {"day": "Lunes", "Temp": 91},
            {"day": "Martes", "Temp": 93},
            {"day": "Miércoles", "Temp": 104},
            {"day": "Jueves", "Temp": 107},
            {"day": "Viernes", "Temp": 114},
            {"day": "Sábado", "Temp": 131},
            {"day": "Domingo", "Temp": 137}
        ],
        [  # Semana 3
            {"day": "Lunes", "Temp": 60},
            {"day": "Martes", "Temp": 77},
            {"day": "Miércoles", "Temp": 80},
            {"day": "Jueves", "Temp": 99},
            {"day": "Viernes", "Temp": 106},
            {"day": "Sábado", "Temp": 110},
            {"day": "Domingo", "Temp": 119}
        ],
        [  # Semana 4
            {"day": "Lunes", "Temp": 71},
            {"day": "Martes", "Temp": 86},
            {"day": "Miércoles", "Temp": 91},
            {"day": "Jueves", "Temp": 103},
            {"day": "Viernes", "Temp": 111},
            {"day": "Sábado", "Temp": 121},
            {"day": "Domingo", "Temp": 131}
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
    print(f"Promedio general de la ciudad: {promedio_ciudad:.2f}")
    for j, promedio in enumerate(promedio_semanal):
        print(f"Promedio de la Semana {j + 1}: {promedio:.2f}")

# Menú para seleccionar ciudad y mostrar solo el promedio general
while True:
    print("\nSeleccione una ciudad:")
    print("1. Ciudad 1")
    print("2. Ciudad 2")
    print("3. Ciudad 3")
    print("4. Salir")

    option = input("Ingrese la Ciudad: ")
    if option == "1":
        print(f"\nPromedio general de Ciudad 1: {promedios_por_ciudad[0][1]:.2f}")
    elif option == "2":
        print(f"\nPromedio general de Ciudad 2: {promedios_por_ciudad[1][1]:.2f}")
    elif option == "3":
        print(f"\nPromedio general de Ciudad 3: {promedios_por_ciudad[2][1]:.2f}")
    elif option == "4":
        print("SALIR...")
        break
    else:
        print("Opción no válida, intenta de nuevo")