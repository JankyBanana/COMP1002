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

    def height(self, current_node=None):
        if current_node is None:
            return self._recHeight(self._root)
        else:
            return self._recHeight(current_node)

    def min(self, current_node=None):
        if current_node is None:
            if self._root is None:
                raise Exception("Binary search tree is empty")
            else:
                return self.min(self._root)
        else:
            if current_node._left is not None:
                return self.min(current_node._left)
            return current_node._key

    def max(self, current_node = None):
        if current_node is None:
            if self._root is None:
                raise Exception("Binary search tree is empty")
            return self.max(self._root)
        else:
            if current_node._right is not None:
                return self.max(current_node._right)
            return current_node._key

    def balance(self):
        if self._root is None:
            return 100

        minLeaf = self._minLeafDepth(self._root)
        maxLeaf = self._recHeight(self._root)       # maxLeaf depth = BST height

        if maxLeaf== 0:
            return 100

        balance = (1 - ((maxLeaf-minLeaf)/maxLeaf))*100
        return balance

# --------------- Private class methods --------------- #

    def _recFind(self, key, current_node):
        if current_node == None:                             # i.e. _recFind is passed a child of a leaf node
            raise ValueError(f"Key {key} not found")

        if key == current_node._key:                         # Key to insert already exists in the BST
            return current_node._data
        elif key < current_node._key:                        # Go down left sub-branch
            return self._recFind(key, current_node._left)
        else:                                                # Go down right sub-branch
            return self._recFind(key, current_node._right)

    def _recInsert(self, key, data, current_node):
        if key == current_node._key:
            raise ValueError("Key already in use. Key must be unique")
        elif key < current_node._key:
            if current_node._left is None:
                current_node._left = self._DSATreeNode(key, data)
            else:
                self._recInsert(key, data, current_node._left)
        else:
            if current_node._right is None:
                current_node._right = self._DSATreeNode(key, data)
            else:
                self._recInsert(key, data, current_node._right)

    def _recHeight(self, current_node):
        if current_node is None:
            currentHeight = -1
        else:
            leftHt = self._recHeight(current_node._left)
            rightHt = self._recHeight(current_node._right)

            if leftHt > rightHt:
                currentHeight = leftHt + 1
            else:
                currentHeight = rightHt + 1
        return currentHeight

    def _minLeafDepth(self, current_node, depth=0):
        if current_node is None:
            return float("inf")

        if current_node._left is None and current_node._right is None:
            return depth

        leftChild = self._minLeafDepth(current_node._left, depth + 1)
        rightChild = self._minLeafDepth(current_node._right, depth + 1)

        if leftChild > rightChild:      # Returns min value
            return rightChild
        return leftChild