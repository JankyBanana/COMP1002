#
# Implementation of the linked list for the Graph class, imported from practical 5
# DSALinkedList object point to head/tail listNodes
# --> ListNodes contain data in data and point to adjacent listNodes


class DSALinkedList:

    #----------  Inner ListNode Class  ----------#
    class DSAListNode():
        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.prev = previous
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
        return self.head.data

    def peekLast(self):
        if self.isEmpty():
            raise Exception(f"Cannot peek last node as the list is empty")
        return self.tail.data

    def removeFirst(self):
        if self.isEmpty():
            raise Exception(f"Cannot remove first node as the list is empty.")
        elif self.head == self.tail:
            nodeValue = self.head.data
            self.head = None
            self.tail = None
            return nodeValue
        else:
            nodeValue = self.head.data
            self.head = self.head.next
            self.head._prev = None
            self.nodes -= 1
            return nodeValue 

    def removeLast(self):
        if self.isEmpty():
            raise Exception(f"Cannot remove last node as the list is empty.")
        elif self.head == self.tail:
            nodeValue = self.head.data
            self.head = None
            self.tail = None
            return nodeValue
        else:
            nodeValue = self.tail.data
            self.tail = self.tail.data
            self.tail.next = None
            self.nodes -= 1
            return nodeValue

    def insertFirst(self, value: object):
        if self.isEmpty():
            newNode = self.DSAListNode(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = self.DSAListNode(value, self.head)
            self.head.prev = newNode
            self.head = newNode
        self.nodes += 1

    def insertLast(self, value: object):
        if self.isEmpty():
            newNode = self.DSAListNode(value, self.head)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = self.DSAListNode(value, None, self.tail)
            self.tail.next = newNode
            self.tail = newNode
        self.nodes += 1

    def display(self):
        nextNode = self.head
        valueString = ""

        for i in range(self.nodes):
            valueString += f"{str(nextNode.data)} "
            nextNode = nextNode.next
        return valueString

    def find(self, data):
        nextNode = self.head

        while nextNode is not None:
            if nextNode.data == data:
                return nextNode
            nextNode = nextNode.next
        raise Exception("Node with given data not found")