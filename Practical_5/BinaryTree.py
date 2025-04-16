#
# Implementation of the Binary Search Tree data structure for practical 5
#

class DSABinarySearchTree():
    class _DSATreeNode():
        def __init__(self, key, data):
            self._key = key
            self._data = data
            self._left = None
            self._right = None

        def __str__(self):
            print(f"Key: {self._key}  Data: {self._data}")

    def __init__(self):
        self.root = None

    #def find(self):

    #def insert(self, key, value):

    #def delete(self, key):

    #def display(self):

    #def height(self):