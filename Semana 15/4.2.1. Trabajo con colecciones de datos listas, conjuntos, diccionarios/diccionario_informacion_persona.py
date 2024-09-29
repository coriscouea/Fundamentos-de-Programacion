# Tarea: Trabajando con Diccionarios en Python
# Crea un diccionario llamado 'informacion_personal'
# que contenga información ficticia sobre una persona,
# incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".

diccionario_informacion_personal = {
    "Nombre":        "Manuel Lopez",
    "Edad":          35,
    "Estatura":      1.65,
    "Ciudad":        "Manabi",
    "Direccion":     "C.18D Calle principal",
    "Estado_Civil":  "Casado",
    "Nacionalidad":  "Mexicano",
    "Genero":        "Masculino"
}

# Acceder al valor asociado con la clave 'Ciudad' y modificarlo
diccionario_informacion_personal["Ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor al diccionario que represente la "Profesion" de la persona
diccionario_informacion_personal["Profesion"] ="Ing. de Software"

# Verificar si la clave "teléfono" existe en el diccionario. Si no existe, agregarla con un número ficticio.
if "telefono" not in diccionario_informacion_personal:
    diccionario_informacion_personal["telefono"] = "0995236567"

# Eliminar la clave "Edad" del diccionario, ya que esa información no es necesaria
del diccionario_informacion_personal["Edad"]

# Imprimir el diccionario final
print("\n".join(f"{clave}:{valor}" for clave, valor in  diccionario_informacion_personal.items()))
