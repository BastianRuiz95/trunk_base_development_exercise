from functionalities import *

# Execute a functionality. Return True if the user select option 0
def executeFunction(option):
    if option == 1:
        print("TO BE IMPLEMENTED...")
    elif option == 2:
        print("TO BE IMPLEMENTED...")
    elif option == 3:
        print("TO BE IMPLEMENTED...")
    elif option == 4:
        print("TO BE IMPLEMENTED...")
    elif option == 5:
        print("TO BE IMPLEMENTED...")
    elif option == 6:
        print("TO BE IMPLEMENTED...")
    elif option == 7:
        # Ask the user for the sort address
        direction = input("Do you want to sort in ascending or descending order? (ascending/descending):").lower()
        while direction not in ['ascending', 'descending']:
            print("Invalid option. Try again.")
            direction = input("Do you want to sort in ascending or descending order? (ascending/descending): ").lower()
        sortNumberList.execute(direction)
    elif option == 8:
        print("TO BE IMPLEMENTED...")
    elif option == 9:
        print("TO BE IMPLEMENTED...")
    elif option == 0:
        return True
    return False


# MAIN CODE
def main():
	while True:

		menu.printMenu()
		userInput = int(input("Select an Option: "))

		if not menu.isValidOption(userInput):
			print("Invalid Option. Try Again!")
		else:
			terminated = executeFunction(userInput)

			if terminated:
				break

	print("Application Ended!")


main()