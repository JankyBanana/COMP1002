#
# Implementation of the DSAStack abstract
# data type for COMP1002 practical 3
#

import numpy as np

class DSAStack():
    defaultSize = 100

    def __init__(self, name = str, size = defaultSize):
        self.size = size
        self.stackArray = np.full(self.size, None, dtype=object)
        self.numElements = 0
        self.name = name

    def push(self, value):
        if self.isFull() == True:
            raise MemoryError(f"Can't add new item as the stack, {self.name} is full")
        else:
            self.stackArray[self.numElements] = value
            self.numElements += 1

    def pop(self):
        if self.isEmpty() == True:
            raise IndexError(f"Can't access top item as the stack, {self.name} is empty")
        else:
            stackTop = self.stackArray[self.numElements-1]
            self.stackArray[self.numElements-1] = None
            self.numElements -= 1
            return stackTop

    def peek(self):
        if self.isEmpty() == True:
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