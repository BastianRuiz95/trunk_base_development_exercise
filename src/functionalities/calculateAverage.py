def calculate_average(values):
    try:
        if len(values) == 0:
            raise ValueError("List is empty")
        total = sum(values)
        if all(isinstance(x, (int, float)) for x in values):
            return total / len(values)
        else:
            raise ValueError("List must contain only numbers")
    except ValueError as e:
        print("Error:", e)
        return 0