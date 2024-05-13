def execute(order=''):
    values = []

    # Prompt the user to enter values until they input 'fin'
    while True:
        value = input("Enter a value (or type 'end' to finish): ")
        if value.lower() == 'finish':
            break
        try:
            value_num = float(value)
            values.append(value_num)
        except ValueError:
            print("Please enter a valid numerical value.")

     # Sort the list of values according to the specified direction
    if order == 'ascending':
        values.sort()
    elif order == 'descending':
        values.sort(reverse=True)

    # Print the sorted list
    print("Values sorted", order, ":", values)