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
        self.count = 0

    def enqueue(self, data):
        raise NotImplementedError("Enqueue must be implemented in subclass")

    def dequeue(self):
        raise NotImplementedError("Dequeue must be implemented in subclass")

    def peek(self):
        raise NotImplementedError("Peek must be implemented in subclass")

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size


class ShufflingQueue(DSAQueue):
    def enqueue(self, data):
        if self.is_full():  # Same as saying if self.is_full == True
            raise MemoryError(f"Can't enqueue to a full queue")
        else:
            self.queueArray[self.count] = data
            self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"Can't dequeue from an empty queue")
        else:
            front = self.queueArray[0]

            for i in range(1, self.count):
                self.queueArray[i - 1] = self.queueArray[i]

            self.queueArray[self.count - 1] = None
            self.count -= 1
            return front

    def peek(self):
        if self.is_empty():
            raise IndexError(f"Can't peek the front of an empty queue")
        else:
            return self.queueArray[0]


class CircularQueue(DSAQueue):
    def __init__(self):
        super().__init__()
        self.start = 0
        self.end = 0

    def enqueue(self, value):
        if self.is_full():
            raise MemoryError(f"Can't enqueue to a full queue")
        else:
            self.queueArray[self.end] = value
            self.end = (self.end + 1) % self.size
            self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"Can't dequeue from an empty queue")
        else:
            front = self.queueArray[self.start]
            self.queueArray[self.start] = None
            self.start = (self.start + 1) % self.size
            self.count -= 1
            return front

    def peek(self):
        if self.is_empty():
            raise IndexError(f"Can't peek the front of an empty queue")
        else:
            return self.queueArray[self.start]
