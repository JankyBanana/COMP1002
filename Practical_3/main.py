#
# Main program file for COMP1002 practical 3
#

import DSAStack as DSAS
import DSAQueue as DSAQ

def stackTest():
    # Demonstration of the DSAStack class in DSAStack.py
    stack = DSAS.DSAStack("stack", 10)
    print(f"Stack is:\n{stack.stackArray}\n")

    # Full or empty stack check
    print(f"The stack is empty? {stack.isEmpty()}")
    print(f"The stack is full? {stack.isFull()}\n")

    # Pushing one-less than max items to the stack
    print("Adding none-less than max items in ascending order to the stack")
    for i in range(stack.size - 1):
        stack.push(i + 1)
    print(f"Stack is:\n{stack.stackArray}\n")

    # Full or empty stack check
    print(f"The stack is empty? {stack.isEmpty()}")
    print(f"The stack is full? {stack.isFull()}\n")

    # Pushing one more item to the stack
    print("Pushing 10 to the stack")
    stack.push(10)
    print(f"Stack is:\n{stack.stackArray}\n")

    # Full or empty stack check
    print(f"The stack is empty? {stack.isEmpty()}")
    print(f"The stack is full? {stack.isFull()}\n")

    # Peeking the top item of the stack
    print(f"Taking a peek at the top item of the stack\n"
          f"Top item = {stack.peek()}")
    print(f"Stack is: {stack.stackArray}\n")

    # Popping the top item off the stack
    print(f"Taking the top item from the stack\n"
          f"Taken item = {stack.pop()}")
    print(f"Stack is:\n{stack.stackArray}\n")


def main():
    stackTest()
    #shufflingQueueTest()
main()

