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
            """Print 'Key: self._key  Data: self._data' when calling the node object"""
            print(f"Key: {self._key}  Data: {self._data}")

    def __init__(self):
        self._root = None

    def find(self, key):
        return self._recFind(key, self._root)

    def insert(self, key, data, currentNode):
        updateNode = currentNode
        if currentNode == None:
            newNode = self._DSATreeNode(key, data)
            updateNode = newNode

        elif key == currentNode._key:
            raise ValueError("Key already in use. Key must be unique")

        elif key < currentNode._key:
            self.insert(key, data, currentNode._left)

        else:
            self.insert(key, data, currentNode._right)

    #def delete(self, key):

    #def display(self):

    #def height(self):

    def _recFind(self, key, current_node):
        data = None
        if current_node == None:                                 # Case 1: not found
            raise ValueError(f"Key {key} not found")

        elif key == current_node._key:                           # Case 2: found
            data = current_node._data

        elif key < current_node._key:                            # Case 3: go left
            data = self._recFind(key, current_node._left)

        else:                                           # Case 4: go right
            data = self._recFind(key, current_node._right)
        return data