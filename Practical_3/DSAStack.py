#
# Implementation of the DSAStack abstract
# data type for COMP1002 practical 3
#

import numpy as np

class Stack():
    defaultSize = 100

    def __init__(self, name):
        self.stackArray = np.full(Stack.defaultSize, None)
        self.numElements = 0
        self.size = len(self.stackArray)
        self.name = name

    def push(self, value):
        if self.isFull == True:
            raise MemoryError(f"New item can't be added to the stack, {self.name} as it is full")
        else:
            self.stackArray[self.numElements] = value
            self.numElements += 1

    def pop(self):
        if self.isEmpty == True:
            raise IndexError(f"Can't access top item as the stack, {self.name} is empty")
        else:
            stackTop = self.stackArray[self.numElements-1]
            self.stackArray[self.numElements-1] = None
            self.numElements -= 1
            return stackTop

    def peek(self):
        if self.isEmpty == True:
            raise IndexError(f"Can't access top item as the stack, {self.name} is empty")
        else:
            stackTop = self.stackArray[self.numElements-1]
            return stackTop

    def isEmpty(self):
        if self.numElements == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.numElements == self.size:
            return True
        else:
            return False

    def demo():
        demoStack = Stack("demoStack")
        print(f"\nThe stack, {demoStack.name}, has size {demoStack.size}, "
              f"has {demoStack.numElements} elements "
              f"and contains the array:\n\n{demoStack.stackArray}\n")

        print(f"{demoStack.name} is empty? {demoStack.isEmpty()}")
        print(f"{demoStack.name} is full? {demoStack.isFull()}\n")

        for i in range(100):
            demoStack.push(i)

        print(f"\nThe stack, {demoStack.name}, has size {demoStack.size}, "
              f"has {demoStack.numElements} elements "
              f"and contains the array:\n\n{demoStack.stackArray}\n")

        print(f"{demoStack.name} is empty? {demoStack.isEmpty()}")
        print(f"{demoStack.name} is full? {demoStack.isFull()}\n")

        print(f"Taking a peek of the top element of {demoStack.name}: Top element = {demoStack.peek()}")
        print(f"Taking the top element of {demoStack.name}, which is: {demoStack.pop()}\n")

        print(f"\nThe stack, {demoStack.name}, has size {demoStack.size}, "
              f"has {demoStack.numElements} elements "
              f"and contains the array:\n\n{demoStack.stackArray}\n")