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

class DSALinkedList():
    class _DSAListNode():  # Defining the class DSAListNode as a private inner class of DSALinkedList
        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.prev = previous

        def getValue(self):
            return self.data

        def getNext(self):
            return self.next

        def getPrev(self):
            return self.prev

    def __init__(self, name = None):
        self.head = None
        self.tail = None
        self.name = name
        self.nodes = 0

    def isEmpty(self):
        return self.nodes == 0

    def peekFirst(self):
        if self.isEmpty():
            raise Exception(f"Cannot peek first node as the list {self.name} is empty")
        return self.head.getValue()

    def peekLast(self):
        if self.isEmpty():
            raise Exception(f"Cannot peek last node as the list {self.name} is empty")
        return self.tail.getValue()

    def removeFirst(self):
        if self.isEmpty():
            raise Exception(f"Cannot remove first node as the list {self.name} is empty.")
        elif self.head == self.tail:
            nodeValue = self.head.getValue()
            self.head = None
            self.tail = None
            return nodeValue
        else:
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
            self.head.prev = None
            self.nodes -= 1
            return nodeValue

    def removeLast(self):
        if self.isEmpty():
            raise Exception(f"Cannot remove last node as the list {self.name} is empty.")
        elif self.head == self.tail:
            nodeValue = self.head.getValue()
            self.head = None
            self.tail = None
            return nodeValue
        else:
            nodeValue = self.tail.getValue()
            self.tail = self.tail.getPrev()
            self.tail.next = None
            self.nodes -= 1
            return nodeValue

    def insertFirst(self, value: object):
        if self.isEmpty():
            newNode = self._DSAListNode(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = self._DSAListNode(value, self.head)
            self.head.prev = newNode
            self.head = newNode
        self.nodes += 1

    def insertLast(self, value: object):
        if self.isEmpty():
            newNode = self._DSAListNode(value, self.head)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = self._DSAListNode(value, None, self.tail)
            self.tail.next = newNode
            self.tail = newNode
        self.nodes += 1

    def printNodeValues(self):
        if self.isEmpty():
            print(f"The list {self.name} is empty.")
        else:
            nextNode = self.head
            print(f"The values of the nodes in the list {self.name} are:")
            valueString = "( "
            while nextNode is not None:
                valueString += f"{str(nextNode.getValue())} "
                nextNode = nextNode.getNext()
            print(valueString + ")")

    def listStats(self):
        print(f"Head: {self.head}    Tail: {self.tail}    Nodes: {self.nodes}")
        self.printNodeValues()