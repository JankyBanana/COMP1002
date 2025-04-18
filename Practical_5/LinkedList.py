#
# Implementation of the linked list ADS for practical 5
#


class DSALinkedList():

    # Defining the listNode class as a private inner class of the linkedList class
    class _DSAListNode():
        def __init__(self, data, next=None, previous=None):
            self._data = data
            self._next = next
            self._prev = previous

        def _getValue(self):
            return self._data

        def _getNext(self):
            return self._next

        def _getPrev(self):
            return self._prev

    def __init__(self, name = None):
        self.head = None
        self.tail = None
        self.name = name
        self.nodes = 0

    def isEmpty(self):
        return self.nodes == 0

    def peekFirst(self):
        if self.isEmpty():
            raise Exception(f"Cannot peek first node as the list '{self.name}' is empty")
        return self.head._getValue()

    def peekLast(self):
        if self.isEmpty():
            raise Exception(f"Cannot peek last node as the list '{self.name}' is empty")
        return self.tail._getValue()

    def removeFirst(self):
        if self.isEmpty():
            raise Exception(f"Cannot remove first node as the list '{self.name}' is empty.")
        elif self.head == self.tail:
            nodeValue = self.head._getValue()
            self.head = None
            self.tail = None
            return nodeValue
        else:
            nodeValue = self.head._getValue()
            self.head = self.head._getNext()
            self.head._prev = None
            self.nodes -= 1
            return nodeValue

    def removeLast(self):
        if self.isEmpty():
            raise Exception(f"Cannot remove last node as the list '{self.name}' is empty.")
        elif self.head == self.tail:
            nodeValue = self.head._getValue()
            self.head = None
            self.tail = None
            return nodeValue
        else:
            nodeValue = self.tail._getValue()
            self.tail = self.tail._getPrev()
            self.tail._next = None
            self.nodes -= 1
            return nodeValue

    def insertFirst(self, value: object):
        if self.isEmpty():
            newNode = self._DSAListNode(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = self._DSAListNode(value, self.head)
            self.head._prev = newNode
            self.head = newNode
        self.nodes += 1

    def insertLast(self, value: object):
        if self.isEmpty():
            newNode = self._DSAListNode(value, self.head)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = self._DSAListNode(value, None, self.tail)
            self.tail._next = newNode
            self.tail = newNode
        self.nodes += 1

    def values(self):
        nextNode = self.head
        valueString = ""

        for i in range(self.nodes):
            valueString += f"{str(nextNode._getValue())} "
            nextNode = nextNode._getNext()
        return valueString

    def listStats(self):
        print(f"Head: {self.head._getValue()}\n"
              f"Tail: {self.tail._getValue()}\n"
              f"Nodes: {self.nodes}")
        self.display()