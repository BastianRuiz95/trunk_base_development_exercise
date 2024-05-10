def calculateAverage(values):
    try:
        if len(values) == 0:
            raise ValueError("List is empty")
        if not all(isinstance(x, (int, float)) for x in values):
            raise ValueError("List must contain only numbers")
        total = sum(values)
        return total / len(values)
    except ValueError as e:
        print("Error:", e)
        return 0