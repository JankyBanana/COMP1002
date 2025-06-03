#
# Implementation of a double-headed, doubly linked list for the COMP1002 Assignment.
# Based on linkedlist.py from the Practical_6 submission
#


class DSALinkedList:
    class DSAListNode:
        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.prev = previous

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def peek_first(self):
        if self.is_empty():
            raise Exception(f"Cannot peek the first node of an empty list")
        return self.head.data

    def peek_last(self):
        if self.is_empty():
            raise Exception(f"Cannot peek last node as the list is empty")
        return self.tail.data

    def insert_first(self, data: object):
        new_node = self.DSAListNode(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node

        self.count += 1

    def insert_last(self, data: object):
        new_node = self.DSAListNode(data, self.head)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception(f"Cannot remove the first node from an empty list")

        node_data = self.head.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1

        return node_data

    def remove_last(self):
        if self.is_empty():
            raise Exception(f"Cannot remove the last node from an empty list")

        node_data = self.tail.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.data
            self.tail.next = None

        self.count -= 1
        return node_data

    def remove(self, data):
        if self.is_empty():
            raise Exception("Cannot remove from an empty list.")

        current = self.head

        while current is not None:
            if current.data == data:
                if current == self.head:
                    if self.head == self.tail:
                        self.head = 0
                        self.tail = 0
                    else:
                        self.head = current.next
                        self.head.prev = None

                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.count -= 1
                return True

            current = current.next

        return False

    def find(self, data):
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next

        return None

    def display(self):
        if self.is_empty():
            return ""

        current_node = self.head
        display_string = ""

        while current_node is not None:
            display_string += f"{str(current_node.data)} "
            current_node = current_node.next

        return display_string
