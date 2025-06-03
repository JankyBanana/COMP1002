#
# Implementation of the stack data type for the COMP1002 Assignment
# Based on DSAstack.py from the Practical_6 submission
#

import numpy as np

class DSAStack:
    defaultSize = 100

    def __init__(self, size = defaultSize):
        self.size = size
        self.stackArray = np.full(self.size, None, dtype=object)
        self.count = 0

    def push(self, data):
        if self.is_full():
            raise MemoryError(f"Can't push to a full stack")
        else:
            self.stackArray[self.count] = data
            self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError(f"Can't pop from an empty stack")
        else:
            top = self.stackArray[self.count - 1]
            self.stackArray[self.count - 1] = None
            self.count -= 1
            return top

    def peek(self):
        if self.is_empty():
            raise IndexError(f"Can't peek the top of an empty stack")
        else:
            top = self.stackArray[self.count - 1]
            return top

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size