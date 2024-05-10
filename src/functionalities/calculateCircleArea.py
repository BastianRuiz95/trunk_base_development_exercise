import math

def calculateArea(radio):
    if radio == "":
        raise Exception("The input must not be empty")
    elif radio.isalpha():
        raise Exception("The input is invalid, please enter a number")
    elif float(radio) <= 0:
        raise Exception("The input must be greater than 0")
    return round(math.pi * pow(float(radio),2),2)


def printResult(result: float):
    print("\nCircle area:")
    print(result)
    print()


def execute():
    circleRadius = input("\nDefine the radius of the circle: ")

    try:
        area = calculateArea(circleRadius)
    except Exception as e:
        print("\n" + e.__str__())
        print()
        return
    
    printResult(area)