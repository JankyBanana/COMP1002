#
# Implementation of the DSAStack abstract
# data type using a linked list for practical 4
#
# Derived from DSAStack.py submitted for COMP1002 Practical 3
#

import LinkedList as ll

class DSAStack():
    def __init__(self, name = None):
        self.linkedList = ll.DSALinkedList(name)
        self.numElements = 0
        self.name = name

    def isEmpty(self):
        if self.numElements == 0:
            return True
        else:
            return False

    def push(self, value):
        self.linkedList.insertLast(value)
        self.numElements += 1

    def pop(self):
        stackTop = self.linkedList.removeLast()
        self.numElements -= 1
        return stackTop

    def peek(self):
        if self.isEmpty():
            raise Exception(f"Cannot peek top item as the stack, {self.name} is empty")
        else:
            stackTop = self.linkedList.peekLast()
            return stackTop
    def stackContents(self):
        self.linkedList.printNodeValues()
