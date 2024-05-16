import re

def wordInput():
    pattern = "^[a-zA-Z]+$"
    userText = input("Write a single word to check if it is palindrome: ").lower()

    while not re.match(pattern, userText):
        print('The word is invalid. It must have only letters and no spaces.')
        userText = input("Write a single word to check if it is palindrome: ").lower()
    
    return userText

def checkWord(text: str):
    return text == text[::-1]


def printResult(isPalindrome: bool, userText: str):
    if isPalindrome:
        print(f'The word {userText} is a palindrome')
        print()
    else:
        print(f'The word {userText} is not a palindrome')
        print()

def execute():
    userText = wordInput()

    isPalindrome = checkWord(userText)

    printResult(isPalindrome, userText)