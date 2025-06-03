#
# Implementation of the DSAStack abstract
# data type for COMP1002 practical 3
#

import numpy as np

class DSAStack:
    defaultSize = 100

    def __init__(self, size = defaultSize):
        self.size = size
        self.stackArray = np.full(self.size, None, dtype=object)
        self.numElements = 0

    def push(self, value):
        if self.is_full():
            raise MemoryError(f"Can't add new item as the stack is full")
        else:
            self.stackArray[self.numElements] = value
            self.numElements += 1

    def pop(self):
        if self.is_empty():
            raise IndexError(f"Can't access top item as the stack is empty")
        else:
            stack_top = self.stackArray[self.numElements-1]
            self.stackArray[self.numElements-1] = None
            self.numElements -= 1
            return stack_top

    def peek(self):
        if self.is_empty():
            raise IndexError(f"Can't access top item as the stack is empty")
        else:
            stack_top = self.stackArray[self.numElements-1]
            return stack_top

    def is_empty(self):
        if self.numElements == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.numElements == self.size:
            return True
        else:
            return False