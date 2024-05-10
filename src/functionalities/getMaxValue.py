def getMaxValue(list):
    return max(list)

def execute():
    valores = input("Enter values separated by '-' (example:1-2-3...):")
    partes = valores.split("-")
    list = []
    for parte in partes:
        list.append(int(parte))
    print("The max value is:",getMaxValue(list))