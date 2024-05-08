def _processText(text: str):
    return text.split(' ')


def printResult(result: list):
    print("Word List:")
    print(result)
    print()


def execute():
    userText = input("Write a text: ")

    result = _processText(userText)

    printResult(result)