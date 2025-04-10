#
# Implementation of the shuffling circular DSAQueue abstract
# data type using a linked list for practical 4
#

import numpy as np

class DSAQueue():
    defaultSize = 100

    def __init__(self, name, size = defaultSize):
        self.size = size
        self.queueArray = np.full(self.size, None, dtype=object)
        self.numElements = 0
        self.name = name

    def enqueue(self, value):
        raise NotImplementedError("enqueue must be implemented in subclass")

    def dequeue(self):
        raise NotImplementedError("dequeue must be implemented in subclass")

    def peek(self):
        raise NotImplementedError("peek must be implemented in subclass")

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

class ShufflingQueue(DSAQueue):
    def enqueue(self, value):
        if self.isFull():  # Same as saying if self.isFull == True
            raise MemoryError(f"Can't add new item as the queue, {self.name} is full")
        else:
            self.queueArray[self.numElements] = value
            self.numElements += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError(f"Can't dequeue next item as the queue, {self.name} is empty")
        else:
            queueNext = self.queueArray[0]
            for i in range(1, self.numElements):
                self.queueArray[i-1] = self.queueArray[i]
            self.queueArray[self.numElements-1] = None
            self.numElements -= 1
            return queueNext

    def peek(self):
        if self.isEmpty() == True:
            raise IndexError(f"Can't access next item as the queue, {self.name} is empty")
        else:
            return self.queueArray[0]

class CircularQueue(DSAQueue):
    def __init__(self, name, size):
        super().__init__(name, size)
        self.queueEnd = 0
        self.queueStart = 0

    def enqueue(self, value):
        if self.isFull():
            raise MemoryError(f"Can't add new item as the queue, {self.name} is full")
        else:
            self.queueArray[self.queueEnd] = value
            self.queueEnd = (self.queueEnd+1) % self.size
            self.numElements += 1

    def dequeue(self):
        if self.isEmpty() == True:
            raise IndexError(f"Can't dequeue next item as the queue, {self.name} is empty")
        else:
            queueNext = self.queueArray[self.queueStart]
            self.queueArray[self.queueStart] = None
            self.queueStart = (self.queueStart + 1) % self.size
            self.numElements -= 1
            return queueNext

    def peek(self):
        if self.isEmpty() == True:
            raise IndexError(f"Can't access next item as the queue, {self.name} is empty")
        else:
            return self.queueArray[self.queueStart]