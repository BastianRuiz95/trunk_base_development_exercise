import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

# Solicitar al usuario que ingrese el radio
radio = float(input("Por favor, ingresa el radio del círculo: "))

# Calcular el área del círculo
area_del_circulo = calcular_area_circulo(radio)

# Imprimir el resultado
print("El área del círculo con radio", radio, "es:", area_del_circulo)
