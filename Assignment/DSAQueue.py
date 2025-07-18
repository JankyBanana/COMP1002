#
# Implementation of the shuffling circular DSAQueue abstract
# data type for COMP1002 practical 3
#

import numpy as np


class DSAQueue:
    default_size = 100

    def __init__(self, size=default_size):
        self.size = size
        self.queueArray = np.full(self.size, None, dtype=object)
        self.numElements = 0

    def enqueue(self, value):
        raise NotImplementedError("enqueue must be implemented in subclass")

    def dequeue(self):
        raise NotImplementedError("dequeue must be implemented in subclass")

    def peek(self):
        raise NotImplementedError("peek must be implemented in subclass")

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


class ShufflingQueue(DSAQueue):
    def enqueue(self, value):
        if self.is_full():  # Same as saying if self.is_full == True
            raise MemoryError(f"Can't add new item as the queue is full")
        else:
            self.queueArray[self.numElements] = value
            self.numElements += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"Can't dequeue next item as the queue is empty")
        else:
            queue_next = self.queueArray[0]
            for i in range(1, self.numElements):
                self.queueArray[i - 1] = self.queueArray[i]
            self.queueArray[self.numElements - 1] = None
            self.numElements -= 1
            return queue_next

    def peek(self):
        if self.is_empty():
            raise IndexError(f"Can't access next item as the queue is empty")
        else:
            return self.queueArray[0]


class CircularQueue(DSAQueue):
    def __init__(self, name):
        super().__init__(name)
        self.queueEnd = 0
        self.queueStart = 0

    def enqueue(self, value):
        if self.is_full():
            raise MemoryError(f"Can't add new item as the queue is full")
        else:
            self.queueArray[self.queueEnd] = value
            self.queueEnd = (self.queueEnd + 1) % self.size
            self.numElements += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"Can't dequeue next item as the queue is empty")
        else:
            queue_next = self.queueArray[self.queueStart]
            self.queueArray[self.queueStart] = None
            self.queueStart = (self.queueStart + 1) % self.size
            self.numElements -= 1
            return queue_next

    def peek(self):
        if self.is_empty():
            raise IndexError(f"Can't access next item as the queue is empty")
        else:
            return self.queueArray[self.queueStart]
