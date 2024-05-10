def calculate_average(values):
    try:
        if len(values) == 0:
            return 0
        total = sum(values)
        if all(isinstance(x, (int, float)) for x in values):
            return total / len(values)
        else:
            raise ValueError("List must contain only numbers")
    except TypeError:
        print("Error: empty list")
        return 0
    except ValueError as e:
        print("Error:", e)
        return 0