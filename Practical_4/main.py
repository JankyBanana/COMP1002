#
# Main section for practical 4
#

import LinkedList as ll

demoList = ll.DSALinkedList("demoList")
stay = True

while stay:
    userInput = input("List operations shown below, select using the in square brackets [...]\n"
                      "InsertFirst  [IF]\n"
                      "InsertLast   [IL]\n"
                      "RemoveFirst  [RF]\n"
                      "RemoveLast   [RL]\n"
                      "Display list [D]\n"
                      "Exit         [E]\n\n"
                      "Input: ")
    print("\n")

    if userInput == "IF":
        userValue = input("Enter a value to insert: ")
        demoList.insertFirst(userValue)
        stay = True

    elif userInput == "IL":
        userValue = input("Enter a value to insert: ")
        demoList.insertLast(userValue)
        stay = True

    elif userInput == "RF":
        demoList.removeFirst()
        stay = True

    elif userInput == "RL":
        demoList.removeLast()
        stay = True

    elif userInput == "D":
        demoList.listStats()
        stay = True

    elif userInput == "E":
        print("Exiting.")
        stay = False
    else:
        print("Invalid input. Input must be in capitals with no spaces.")
        stay = True