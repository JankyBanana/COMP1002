#
# Implementation of the shuffling circular DSAQueue abstract
# data type using a linked list for practical 4
#
# Derived from DSAQueue.py submitted COMP1002 Practical 3
#

import LinkedList as ll

class DSAQueue():

    def __init__(self, name):
        self.linkedList = ll.DSALinkedList(name)
        self.numElements = 0
        self.name = name

    def enqueue(self, value):
        raise NotImplementedError("enqueue must be implemented in subclass")

    def dequeue(self):
        raise NotImplementedError("dequeue must be implemented in subclass")

    def peek(self):
        raise NotImplementedError("peek must be implemented in subclass")

    def isEmpty(self):
        return self.linkedList.isEmpty()

    def queueContents(self):
        return self.linkedList.printNodeValues()

    def queueInfo(self):
        return self.linkedList.listStats()

class ShufflingQueue(DSAQueue):
    def enqueue(self, value):
        self.linkedList.insertLast(value)
        self.numElements += 1

    def dequeue(self):
        return self.linkedList.removeFirst()

    def peek(self):
        return self.linkedList.peekFirst()

class CircularQueue(DSAQueue):
    def enqueue(self, value):
        self.linkedList.insertLast(value)
        if self.isEmpty():
            self.linkedList.tail.next = self.linkedList.tail
            self.linkedList.tail.prev = self.linkedList.head
        else:
            self.linkedList.head.prev = self.linkedList.tail
            self.linkedList.tail.next = self.linkedList.head
        self.numElements += 1

    def dequeue(self):
        queueNext = self.linkedList.removeFirst()
        self.linkedList.head.prev = self.linkedList.tail
        self.linkedList.tail.next = self.linkedList.head
        self.numElements -= 1
        return queueNext

    def peek(self):
        return self.linkedList.peekFirst()