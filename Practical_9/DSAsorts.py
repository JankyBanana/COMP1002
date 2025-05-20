#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
# Copied from Practical 1
#

def bubbleSort(A):
    for passes in range(A.size - 1):
        for i in range(A.size - passes - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]

def insertionSort(A):
    for p in range(1, A.size):
        i = p
        while i > 0 and A[i - 1] > A[i]:
            A[i], A[i - 1] = A[i - 1], A[i]
            i -= 1

def selectionSort(A):
    for p in range(A.size - 1):
        min_index = p
        for i in range(min_index + 1, A.size):
            if A[i] < A[min_index]:
                min_index = i
        A[min_index], A[p] = A[p], A[min_index]

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


