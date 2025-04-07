#
# Implementation of the linked list ADS for practical 4
#

class DSAListNode():
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.prev = previous
    def getValue(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev

class DSALinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        self.elements = 0
    def isEmpty(self):
        if self.elements == 0:
            return True
        else:
            return False
    def peekFirst(self):
        return self.head.getValue()
    def peekLast(self):
        return self.tail.getValue()
    def insertFirst(self, value: object):
        if self.isEmpty():
            newNode = DSAListNode(value)
            self.head = newNode
            self.elements += 1
        else:
            newNode = DSAListNode(value, self.head)
            self.head = newNode
            self.elements += 1
    def insertLast(self, value: object):
        if self.isEmpty():
            newNode = DSAListNode(value, self.head)
            self.head = newNode
            self.elements += 1
        else:
            newNode = DSAListNode(value, None, self.tail)
            self.tail = newNode
            self.elements += 1
    def removeFirst(self):
        if self.isEmpty():
            return False
        else:
            nodeValue = self.head.getValue
            self.head = self.head.getNext
            self.head.prev = None
            self.elements -= 1
            return nodeValue
    def removeLast(self):
        if self.isEmpty():
            return False
        else:
            nodeValue = self.tail.getValue
            self.tail = self.tail.getPrev
            self.tail.next = None
            self.elements -= 1
            return nodeValue