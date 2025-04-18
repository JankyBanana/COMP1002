#
# Main section for testing practical 5
#


import BinaryTree as BT
import numpy as np


def stringSeperator(inputStr):
    tempString = ""
    wordCount = 1

    for idx in range(1, len(inputStr)):
        if inputStr[idx-1] != " " and inputStr[idx] == " ":
            wordCount += 1

    results = np.full(wordCount, None)
    resultIndx = 0

    for idx in range(len(inputStr)):
        if inputStr[idx] != " ":
            tempString += inputStr[idx]
        elif idx > 0 and inputStr[idx-1] != " ":
            results[resultIndx] = tempString
            tempString = ""
            resultIndx += 1

    if tempString:
        results[resultIndx] = tempString

    return results

def main():
    demoTree = BT.DSABinarySearchTree()
    userInput = input(f"\nBinary Search Tree operations listed below. Select using the square brackets [...]\n"
                      f"------------------------\n"
                      f" Add Node        [ADD <KEY> <DATA>]\n"
                      f" Delete Node     [DEL <KEY>]\n"
                      f" Show Tree       [SHOW METHOD: IO|PRE|POST]\n"
                      f" Tree Minimum    [MIN]\n"
                      f" Tree Maximum    [MAX]\n"
                      f" Tree Height     [HEIGHT]\n"
                      f" Tree Balance    [BAL]\n"
                      f" Find Key        [FIND <KEY>]\n"
                      f" Exit            [EXIT]\n"
                      f"------------------------\n"
                      f"Input: ")

    inputs = stringSeperator(userInput)

    while 1:
        try:
            inputs[0] = inputs[0].upper()

            if inputs[0] == "ADD":
                try:
                    demoTree.insert(int(inputs[1]), inputs[2])
                except IndexError:
                    demoTree.insert(int(inputs[1]), None)
            elif inputs[0] == "DEL":
                demoTree.delete(int(inputs[1]))
            elif inputs[0] == "SHOW":
                inputs[1] = inputs[1].upper()

                if inputs[1] == "IO":
                    print(f"\nTree contents: {demoTree.traverse("inorder").values()}")
                elif inputs[1] == "PRE":
                    print(f"\nTree contents: {demoTree.traverse("preorder").values()}")
                elif inputs[1] == "POST":
                    print(f"\nTree contents: {demoTree.traverse("postorder").values()}")
                else:
                    print("Invalid input. Valid inputs are:\n"
                          "IO\n"
                          "PRE\n"
                          "POST")
            elif inputs[0] == "MIN":
                print(f"Minimum key value: {demoTree.min()}")
            elif inputs[0] == "MAX":
                print(f"Maximum key value: {demoTree.max()}")
            elif inputs[0] == "HEIGHT":
                print(f"Tree height: {demoTree.height()}")
            elif inputs[0] == "BAL":
                print(f"Tree balance: {demoTree.balance()}")
            elif inputs[0] == "FIND":
                print(f"Data of key '{inputs[1]}' is: {demoTree.find(int(inputs[1]))}")
            elif inputs[0] == "EXIT":
                break
            else:
                print("Invalid input. Ensure that all commands are capitalised.")
        except Exception:
            print("\nCommand provided was either invalid or missing an argument.")
        userInput = input("Input: ")
        inputs = stringSeperator(userInput)
main()