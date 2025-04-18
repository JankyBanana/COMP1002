#
# Implementation of the Binary Search Tree data structure for practical 5
#


from Practical_5 import LinkedList as LL


class DSABinarySearchTree():
    class _DSATreeNode():
        def __init__(self, key, data=None):
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
        nodeData =  self._recFind(key, self._root)
        return nodeData._data

    def insert(self, key, data=None):
        if self._root is None:
            self._root = self._DSATreeNode(key, data)
        else:
            self._recInsert(key, data, self._root)

    def height(self, currentNode=None):
        if currentNode is None:
            if self._root is None:
                raise Exception("Binary search tree is empty")
            else:
                return self._recHeight(self._root)
        else:
            return self._recHeight(currentNode)

    def min(self, currentNode=None):
        if currentNode is None:
            if self._root is None:
                raise Exception("Binary search tree is empty")
            else:
                return self.min(self._root)

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
        if currentNode._right is not None:
            return self.max(currentNode._right)
        else:
            return currentNode._key

    def balance(self):
        if self._root is None:
            return 100

        minLeaf = self._minLeafDepth(self._root)
        maxLeaf = self._recHeight(self._root)       # maxLeaf depth = BST height

        if maxLeaf== 0:
            return 100

        balance = (1 - ((maxLeaf-minLeaf)/maxLeaf))*100
        return balance

    def traverse(self,method: str, currentNode=None):
        keyList = LL.DSALinkedList("keyList")

        if currentNode is None:
            if self._root is None:
                raise Exception("Binary search tree is empty")
            else:
                if method == "inorder":
                    keyList = self._inorder(self._root, keyList)
                elif method == "postorder":
                    keyList = self._postorder(self._root, keyList)
                elif method == "preorder":
                    keyList = self._preorder(self._root, keyList)
                else:
                    raise ValueError("Invalid traversal method provided.")
        else:
            if method == "inorder":
                keyList = self._inorder(self._root, keyList)
            elif method == "postorder":
                keyList = self._postorder(self._root, keyList)
            elif method == "preorder":
                keyList = self._preorder(self._root, keyList)
            else:
                raise ValueError("Invalid traversal method provided.")
        return keyList

    def delete(self, key):
        self._root = self._recDelete(key, self._root)

# --------------- Private class methods --------------- #

    def _recFind(self, key, currentNode):
        if currentNode is None:                             # i.e. _recFind is passed a child of a leaf node
            raise ValueError(f"Key {key} not found")

        if key == currentNode._key:                         # Found key
            return currentNode
        elif key < currentNode._key:                        # Go down left sub-branch
            return self._recFind(key, currentNode._left)
        else:                                                # Go down right sub-branch
            return self._recFind(key, currentNode._right)

    def _recInsert(self, key, data, currentNode):
        if key == currentNode._key:
            raise ValueError("Key already in use. Key must be unique")
        elif key < currentNode._key:
            if currentNode._left is None:
                currentNode._left = self._DSATreeNode(key, data)
            else:
                self._recInsert(key, data, currentNode._left)
        elif key > currentNode._key:
            if currentNode._right is None:
                currentNode._right = self._DSATreeNode(key, data)
            else:
                self._recInsert(key, data, currentNode._right)

    def _recHeight(self, currentNode):
        if currentNode is None:
            currentHeight = -1
        else:
            leftHeight = self._recHeight(currentNode._left)
            rightHeight = self._recHeight(currentNode._right)

            if leftHeight > rightHeight:
                currentHeight = leftHeight + 1
            else:
                currentHeight = rightHeight + 1
        return currentHeight

    def _minLeafDepth(self, currentNode, depth=0):
        if currentNode is None:
            return float("inf")
        elif currentNode._left is None and currentNode._right is None:
            return depth

        leftChild = self._minLeafDepth(currentNode._left, depth + 1)
        rightChild = self._minLeafDepth(currentNode._right, depth + 1)

        if leftChild > rightChild:      # Returns min value
            return rightChild
        return leftChild

    def _inorder(self, currentNode, keyList):
        if currentNode._left is not None:
            keyList = self._inorder(currentNode._left, keyList)

        keyList.insertLast(currentNode._key)

        if currentNode._right is not None:
            keyList = self._inorder(currentNode._right, keyList)
        return keyList

    def _preorder(self, currentNode, keyList):
        keyList.insertLast(currentNode._key)

        if currentNode._left is not None:
            keyList = self._preorder(currentNode._left, keyList)

        if currentNode._right is not None:
            keyList = self._preorder(currentNode._right, keyList)
        return keyList

    def _postorder(self, currentNode, keyList):
        if currentNode._left is not None:
            keyList = self._postorder(currentNode._left, keyList)

        if currentNode._right is not None:
            keyList = self._postorder(currentNode._right, keyList)

        keyList.insertLast(currentNode._key)
        return keyList

    def _recDelete(self, key, currentNode):
        if currentNode is None:
            return ValueError(f"Key {key} not found in the tree")

        if key < currentNode._key:
            currentNode._left = self._recDelete(key, currentNode._left)
        elif key > currentNode._key:
            currentNode._right = self._recDelete(key, currentNode._right)
        else:
            if currentNode._left is None:
                return currentNode._right
            elif currentNode._right is None:
                return currentNode._left
            else:
                successor = self._sucFind(currentNode._right)
                currentNode._key = successor._key
                currentNode._data = successor._data
                currentNode._right = self._recDelete(successor._key, currentNode._right)  # Removes original successor from BST
        return currentNode

    def _sucFind(self, currentNode):
        while currentNode._left is not None:
            currentNode = currentNode._left
        return currentNode