#
# Implementation of the linked list for the Graph class, imported from practical 5
# DSALinkedList object point to head/tail listNodes
# --> ListNodes contain data in data and point to adjacent listNodes


class DSALinkedList:
    class DSAListNode:
        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.prev = previous

    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = 0

    def is_empty(self):
        return self.nodes == 0

    def peek_first(self):
        if self.is_empty():
            raise Exception(f"Cannot peek the first node of an empty list")
        return self.head.data

    def peek_last(self):
        if self.is_empty():
            raise Exception(f"Cannot peek last node as the list is empty")
        return self.tail.data

    def remove_first(self):
        if self.is_empty():
            raise Exception(f"Cannot remove the first node from an empty list")
        elif self.head == self.tail:
            node_value = self.head.data
            self.head = None
            self.tail = None
            return node_value
        else:
            node_value = self.head.data
            self.head = self.head.next
            self.head._prev = None
            self.nodes -= 1
            return node_value

    def remove_last(self):
        if self.is_empty():
            raise Exception(f"Cannot remove the last node from an empty list")
        elif self.head == self.tail:
            node_value = self.head.data
            self.head = None
            self.tail = None
            return node_value
        else:
            node_value = self.tail.data
            self.tail = self.tail.data
            self.tail.next = None
            self.nodes -= 1
            return node_value

    def insert_first(self, value: object):
        if self.is_empty():
            new_node = self.DSAListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = self.DSAListNode(value, self.head)
            self.head.prev = new_node
            self.head = new_node
        self.nodes += 1

    def insert_last(self, value: object):
        if self.is_empty():
            new_node = self.DSAListNode(value, self.head)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = self.DSAListNode(value, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node
        self.nodes += 1

    def display(self):
        next_node = self.head
        value_string = ""

        for i in range(self.nodes):
            value_string += f"{str(next_node.data)} "
            next_node = next_node.next
        return value_string

    def find(self, data):
        next_node = self.head

        while next_node is not None:
            if next_node.data == data:
                return next_node
            next_node = next_node.next
        raise Exception("Node with given data not found")

    def remove(self, value):
        if self.is_empty():
            raise Exception("Cannot remove from an empty list.")

        current = self.head

        while current is not None:
            if current.data == value:
                if current == self.head:
                    self.head = current.next

                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev

                    if self.tail is not None:
                        self.tail.next = None
                    else:
                        self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.nodes -= 1
                return
            current = current.next
        raise ValueError("Value not found in the list.")