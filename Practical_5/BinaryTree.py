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
            return f"Key: {self._key}  Data: {self._data}"

    def __init__(self):
        self._root = None

    def find(self, key):
        return self._recFind(key, self._root)

    def insert(self, key, data):
        if self._root is None:
            self._root = self._DSATreeNode(key, data)
        else:
            self._recInsert(key, data, self._root)

    #def delete(self, key):

    #def display(self):

    def height(self, currentNode=None):
        if currentNode is None:
            return self._recHeight(self._root)
        else:
            return self._recHeight(currentNode)

    def min(self, currentNode=None):
        if currentNode is None:
            if self._root is None:
                raise Exception("Binary search tree is empty")
            else:
                return self.min(self._root)
        else:
            if currentNode._left is not None:
                return self.min(currentNode._left)
            return currentNode._key

    def max(self, currentNode = None):
        if currentNode is None:
            if self._root is None:
                raise Exception("Binary search tree is empty")
            return self.max(self._root)
        else:
            if currentNode._right is not None:
                return self.max(currentNode._right)
            return currentNode._key

    def balance(self):
        if self._root is None:
            return 100

        minLeaf = self._minLeafDepth(self._root)
        maxLeaf = self._maxLeafDepth(self._root)
        height = self._recHeight(self._root)

        if height == 0:
            return 100

        balance = (1 - ((maxLeaf-minLeaf)/height))*100
        return balance

# --------------- Private class methods --------------- #

    def _recFind(self, key, currentNode):
        if currentNode == None:                             # i.e. _recFind is passed a child of a leaf node
            raise ValueError(f"Key {key} not found")

        if key == currentNode._key:                       # Key to insert already exists in the BST
            return currentNode._data
        elif key < currentNode._key:                        # Go down left sub-branch
            return self._recFind(key, currentNode._left)
        else:                                               # Go down right sub-branch
            return self._recFind(key, currentNode._right)

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

        leftHt = self._recHeight(currentNode._left)
        rightHt = self._recHeight(currentNode._right)

        if leftHt > rightHt:
            currentHeight = leftHt + 1
        else:
            currentHeight = rightHt + 1
        return currentHeight

    def _minLeafDepth(self, currentNode, depth=0):
        if currentNode is None:
            return float("inf")

        if currentNode._left is None and currentNode._right is None:
            return depth

        leftChild = self._minLeafDepth(currentNode._left, depth + 1)
        rightChild = self._minLeafDepth(currentNode._right, depth + 1)

        if leftChild > rightChild:
            return rightChild
        return leftChild

    def _maxLeafDepth(self, currentNode, depth=0):
        if currentNode is None:
            return -1  # No depth from empty node

        if currentNode._left is None and currentNode._right is None:
            return depth

        leftChild = self._maxLeafDepth(currentNode._left, depth + 1)
        rightChild = self._maxLeafDepth(currentNode._right, depth + 1)

        if leftChild > rightChild:
            return leftChild
        return rightChild