#
# Implementation of the shuffling circular DSAQueue abstract
# data type for COMP1002 practical 3
#

import numpy as np

class ShufflingQueue():
    defaultSize = 100

    def __init__(self, name):
        self.queueArray = np.full(ShufflingQueue.defaultSize, None)
        self.numElements = 0
        self.size = len(self.queueArray)
        self.name = name

    def enqueue(self, value):
        if self.isFull == True:
            raise MemoryError(f"Can't add new item as the queue, {self.name} is full")
        else:
            self.queueArray[self.numElements] = value
            self.numElements += 1

    def dequeue(self):
        if self.isEmpty == True:
            raise IndexError(f"Can't dequeue next item as the queue, {self.name} is empty")
        else:
            queueNext = self.queueArray[0]
            for i in range(1, self.numElements):
                self.queueArray[i-1] = self.queueArray[i]
            self.queueArray[self.numElements-1] = None
            self.numElements -= 1
            return queueNext

    def peek(self):
        if self.isEmpty == True:
            raise IndexError(f"Can't access next item as the queue, {self.name} is empty")
        else:
            queueTop = self.queueArray[0]
            return queueTop

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
        demoQueue = ShufflingQueue("demoQueue")
        print(f"\nThe queue, {demoQueue.name}, has size {demoQueue.size}, "
              f"has {demoQueue.numElements} elements "
              f"and contains the array:\n\n{demoQueue.queueArray}\n")

        print(f"{demoQueue.name} is empty? {demoQueue.isEmpty()}")
        print(f"{demoQueue.name} is full? {demoQueue.isFull()}\n")

        for i in range(100):
            demoQueue.enqueue(i)

        print(f"The queue, {demoQueue.name}, has size {demoQueue.size}, "
              f"has {demoQueue.numElements} elements "
              f"and contains the array:\n\n{demoQueue.queueArray}\n")

        print(f"{demoQueue.name} is empty? {demoQueue.isEmpty()}")
        print(f"{demoQueue.name} is full? {demoQueue.isFull()}\n")

        print(f"Taking a peek of queue, {demoQueue.name}, the next element in the queue is: {demoQueue.peek()}")
        print(f"Dequeuing the next element of {demoQueue.name} removes {demoQueue.dequeue()} from the queue\n")

        print(f"The queue, {demoQueue.name}, has size {demoQueue.size}, "
              f"has {demoQueue.numElements} elements "
              f"and contains the array:\n\n{demoQueue.queueArray}\n")