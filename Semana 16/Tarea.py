
"""""(Semana 16) Tarea: 
Trabajo con Archivos de Texto en Python"""""

# Definimos el nombre del archivo que vamos a crear y manejar
file_name = "my_notes.txt"

# Crea un nuevo archivo llamado my_notes.txt en modo de escritura ("w")
my_notes = open(file_name, "w")

# Escribimos tres líneas de texto en el archivo utilizando el método write()
my_notes.write("Linea 1: Universidad.\n")
my_notes.write("Linea 2: UEA.\n")
my_notes.write("Linea 3: Excelencia.\n")

# También se puede escribir múltiples líneas a la vez con writelines()
# Aquí creamos una lista con dos líneas adicionales y las escribimos en el archivo
lineas = ["Linea 4: Siguiente Ejemplo.\n", "Linea 5: Finalizada de la Tarea.\n"]
my_notes.writelines(lineas)

# Después de escribir en el archivo, siempre es importante cerrarlo
# Esto asegura que los datos se guarden correctamente y libera recursos
my_notes.close()

# Ahora abrimos el archivo en modo lectura ("r") para leer su contenido
my_notes = open("my_notes.txt", "r")

# Primer método de lectura: read()
# read() lee todo el contenido del archivo de una sola vez
print('Primer Metodo : read()')
print('---------------------------->')
print(my_notes.read()) # Imprimimos todo el contenido del archivo

# Cerramos el archivo después de la lectura
my_notes.close()

# Volvemos a abrir el archivo en modo de lectura ("r") para usar otro método de lectura
my_notes = open("my_notes.txt", "r")

# Segundo método de lectura: readlines()
# readlines() devuelve una lista con todas las líneas del archivo
# Luego recorremos cada línea e imprimimos su contenido
print('Segundo Metodo : Readlines()')
print('---------------------------->')
for linea in my_notes.readlines():
    print(linea.strip('\n')) # Usamos strip() para eliminar el salto de línea adicional al imprimir

# Cerramos el archivo después de terminar la lectura
my_notes.close()




































