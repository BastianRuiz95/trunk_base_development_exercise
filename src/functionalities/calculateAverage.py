def calcular_promedio(valores):
    try:
        if len(valores) == 0:
            return 0
    except TypeError:
        print("Error: Lista vacía")
        return 0
    total = sum(valores)
    return total / len(valores)
