# Definición de la función calcular_descuento
# La función toma dos parámetros: monto_total (obligatorio) y porcentaje (con un valor predeterminado de 10)
# Calcula el descuento aplicando el porcentaje al monto total y devuelve el valor del descuento redondeado a dos decimales
def calcular_descuento(monto_total, porcentaje=10):
    # Calcula el monto del descuento
    descuento = monto_total * porcentaje / 100
    # Devuelve el descuento redondeado a dos decimales
    return round(descuento, 2)

# Ejemplo 1: Usando el porcentaje predeterminado del 10%
monto_total = 10850
# Se llama a la función calcular_descuento con el monto_total y el porcentaje por defecto
descuento = calcular_descuento(monto_total)
# Se calcula el monto final restando el descuento del monto total
monto_final = monto_total - descuento
# Muestra los resultados: monto total, descuento aplicado y monto final a pagar
print(f"Monto total: $ {monto_total:.2f}, Descuento: $ {descuento:.2f}, Monto a pagar: $ {monto_final:.2f}")

# Ejemplo 2: Usando un porcentaje de descuento personalizado del 40%
monto_total2 = 35499
descuento2 = 40
# Se llama a la función calcular_descuento con el monto_total2 y el porcentaje del 40%
descuento2 = calcular_descuento(monto_total2, descuento2)
# Se calcula el monto final restando el descuento del monto total
monto_final2 = monto_total2 - descuento2
# Muestra los resultados: monto total, descuento aplicado y monto final a pagar
print(f"Monto total: $ {monto_total2:.2f}, Descuento: $ {descuento2:.2f}, Monto a pagar: $ {monto_final2:.2f}")

# Solicita al usuario que ingrese el monto total de la compra
monto_total = float(input("Ingrese el monto total de la compra: "))
# Se llama a la función calcular_descuento con el monto ingresado por el usuario y el porcentaje predeterminado (10%)
descuento = calcular_descuento(monto_total)
# Se calcula el monto final restando el descuento del monto total
monto_final = monto_total - descuento
# Muestra los resultados para el monto ingresado por el usuario
print(f"Descuento para un monto total de $ {monto_total}, Descuento: $ {descuento:.2f}, Monto a pagar: $ {monto_final:.2f}")