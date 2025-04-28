#
# Implementation of the linked list for the Graph class, imported from practical 5
# DSALinkedList object point to head/tail listNodes
# --> ListNodes contain data in _data and point to adjacent listNodes


class DSALinkedList:

    #----------  Inner ListNode Class  ----------#
    class _DSAListNode():
        def __init__(self, _data, _next=None, _previous=None):
            self._data = _data
            self._next = _next
            self._prev = _previous
    #---------- LinkedList Class ----------#
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = 0

    def isEmpty(self):
        return self.nodes == 0

    def peekFirst(self):
        if self.isEmpty():
            raise Exception(f"Cannot peek first node as the list is empty")
        return self.head._data

    def peekLast(self):
        if self.isEmpty():
            raise Exception(f"Cannot peek last node as the list is empty")
        return self.tail._data

    def removeFirst(self):
        if self.isEmpty():
            raise Exception(f"Cannot remove first node as the list is empty.")
        elif self.head == self.tail:
            nodeValue = self.head._data
            self.head = None
            self.tail = None
            return nodeValue
        else:
            nodeValue = self.head._data
            self.head = self.head._next
            self.head._prev = None
            self.nodes -= 1
            return nodeValue 

    def removeLast(self):
        if self.isEmpty():
            raise Exception(f"Cannot remove last node as the list '{self.name}' is empty.")
        elif self.head == self.tail:
            nodeValue = self.head._data
            self.head = None
            self.tail = None
            return nodeValue
        else:
            nodeValue = self.tail._data
            self.tail = self.tail._data
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

    def display(self):
        nextNode = self.head
        valueString = ""

        for i in range(self.nodes):
            valueString += f"{str(nextNode._data)} "
            nextNode = nextNode._next
        return valueString

    def find(self, data):
        nextNode = self.head

        while nextNode is not None:
            if nextNode._data == data:
                return nextNode
            nextNode = nextNode._next
        raise Exception("Node with given data not found")