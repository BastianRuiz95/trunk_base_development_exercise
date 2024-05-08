# Print the main menu
def printMenu():
	print("MAIN MENU")
	print("---------------------------------")
	print("1. Calculate Average from List")
	print("2. Find a Max Value from List")
	print("3. Get Factorial Number")
	print("4. Calculate Circle Area")
	print("5. Check Prime Number")
	print("6. Word is Palindrome")
	print("7. Sort Number List")
	print("8. Get Number Frequency from List")
	print("9. Get Word List from a text")
	print("0. Exit Application")

# Check if the option selected by user is valid
def isValidOption(option):
	if option < 0 or option > 9:
		return False
	return True