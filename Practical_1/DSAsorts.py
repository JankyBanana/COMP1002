#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    swapped = True

    while swapped:
        swapped = False
        for index in range(len(A) - 1):
            if A[index] > A[index + 1]:
                A[index], A[index + 1] = A[index + 1], A[index]
                swapped = True

def insertionSort(A):
    for sortIndex in range(1, len(A)):
        key = A[sortIndex]
        subArrayIndex = sortIndex - 1

        A[subArrayIndex + 1] = A[subArrayIndex]
        subArrayIndex -= 1
    A[subArrayIndex + 1] = key

def selectionSort(A):
    for index in range(len(A)):
        minValIndex = index
        for unsortIndex in range(index + 1, len(A)):
            if A[unsortIndex] < A[minValIndex]:
                minValIndex = unsortIndex

        minVal = A[minValIndex]
        A[minValIndex] = A[index]
        A[index] = minVal

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


