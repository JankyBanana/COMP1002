#
# Implementation of the Binary Search Tree data structure for practical 5
#
from adodbapi import OperationalError
from nbformat.current import current_nbformat


class DSABinarySearchTree():
    class _DSATreeNode():
        def __init__(self, key, data):
            self._key = key
            self._data = data
            self._left = None
            self._right = None

        def __str__(self):
            """Print 'Key: self._key  Data: self._data' when calling the node object"""
            print(f"Key: {self._key}  Data: {self._data}")

    def __init__(self):
        self._root = None

    def __str__(self):
        return self._root

    def find(self, key):
        return self._recFind(key, self._root)

    def insert(self, key, data):
        if self._root is None:
            self._root = self._DSATreeNode(key, data)
        else:
            self._recInsert(key, data, self._root)

    #def delete(self, key):

    #def display(self):

    def height(self):
        return self._recHeight(self._root)

    def min(self, currentNode=None):
        if currentNode is None:
            if self._root is None:
                raise Exception("Binary search tree is empty")
            else:
                return self.min(self._root)
        else:
            if currentNode._left is not None:
                return self.min(currentNode._left)
            else:
                return currentNode._key

    def max(self, currentNode = None):
        if currentNode is None:
            if self._root is None:
                raise Exception("Binary search tree is empty")
            else:
                return self.max(self._root)
        else:
            if currentNode._right is not None:
                return self.max(currentNode._right)
            else:
                return currentNode._key

# --------------- Private class methods --------------- #

    def _recFind(self, key, currentNode):
        data = None
        if currentNode == None:                                 # Case 1: not found
            raise ValueError(f"Key {key} not found")
        elif key == currentNode._key:                           # Case 2: found
            data = currentNode._data
        elif key < currentNode._key:                            # Case 3: go left
            data = self._recFind(key, currentNode._left)
        else:                                           # Case 4: go right
            data = self._recFind(key, currentNode._right)
        return data

    def _recInsert(self, key, data, currentNode):
        if key == currentNode._key:
            raise ValueError("Key already in use. Key must be unique")
        elif key < currentNode._key:
            if currentNode._left is None:
                currentNode._left = self._DSATreeNode(key, data)
            else:
                self._recInsert(key, data, currentNode._left)

        else:
            if currentNode._right is None:
                currentNode._right = self._DSATreeNode(key, data)
            else:
                self._recInsert(key, data, currentNode._right)

    def _recHeight(self, currentNode):
        if currentNode is None:
            currentHeight = -1
        else:
            leftHt = self._recHeight(currentNode._left)
            rightHt = self._recHeight(currentNode._right)
            if leftHt > rightHt:
                currentHeight = leftHt + 1
            else:
                currentHeight = rightHt + 1
        return currentHeight