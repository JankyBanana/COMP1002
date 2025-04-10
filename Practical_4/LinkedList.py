#
# Implementation of the linked list ADS for practical 4
#
# ---- Note ----
# The remove methods check if the linked list only has 1 node using `if self.head == self.tail' as these references are
# explicitly assigned and controlled each time the linked list's structure changes and so represent the real structure
# of the linked list.
#
# Using `self.elements == 0` is valid this relies on self-managing the `elements` variable, leaving this method
# vulnerable to any unexpected changes to the `elements` variable which would break this logic check

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
    def __init__(self, head = None, tail = None, name = None):
        self.head = head
        self.tail = tail
        self.name = name
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
            self.tail = newNode
            self.elements += 1
        else:
            newNode = DSAListNode(value, self.head)
            self.head.prev = newNode
            self.head = newNode
            self.elements += 1

    def insertLast(self, value: object):
        if self.isEmpty():
            newNode = DSAListNode(value, self.head)
            self.head = newNode
            self.tail = newNode
            self.elements += 1

        else:
            newNode = DSAListNode(value, None, self.tail)
            self.tail.next = newNode
            self.tail = newNode
            self.elements += 1

    def removeFirst(self):
        if self.elements == 0:
            return False

        elif self.head == self.tail:
            nodeValue = self.head.getValue()
            self.head = None
            self.tail = None
            return nodeValue

        else:
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
            self.head.prev = None
            self.elements -= 1
            return nodeValue

    def removeLast(self):
        if self.elements == 0:
            return False

        elif self.head == self.tail:
            nodeValue = self.head.getValue()
            self.head = None
            self.tail = None
            return nodeValue

        else:
            nodeValue = self.tail.getValue()
            self.tail = self.tail.getPrev()
            self.tail.next = None
            self.elements -= 1
            return nodeValue

    def printNodeValues(self):
        nextNode = self.head
        print("The values of the nodes in {self.name} are:")
        for i in range(self.elements):
            print(nextNode.getValue())
            nextNode = nextNode.getNext()