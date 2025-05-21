#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
# Copied from Practical 1
#

import numpy as np


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
    left_index = 0
    right_index = A.size
    mergeSortRecurse(A, left_index, right_index)


def mergeSortRecurse(A, left_index, right_index):
    if left_index < right_index:
        mid_index = (left_index + right_index) // 2

        mergeSortRecurse(A, left_index, mid_index)
        mergeSortRecurse(A, mid_index + 1, right_index)

        merge(A, left_index, mid_index, right_index)
    return A


def merge(A, left_index, mid_index, right_index):
    temp_size = right_index - left_index + 1
    temp_array = np.zeros(temp_size)
    ii = left_index
    jj = mid_index + 1
    kk = 0

    while ii <= mid_index and jj <= right_index:
        if A[ii] <= A[jj]:
            temp_array[kk] = A[ii]
            ii += 1
        else:
            temp_array[kk] = A[jj]
            jj += 1
        kk += 1

    for ii in range(ii, mid_index):
        temp_array[kk] = A[ii]
        kk += 1

    for jj in range(jj, jj + 1):
        temp_array[kk] = A[jj]
        kk += 1

    for kk in range(left_index, right_index):
        A[kk] = temp_array[kk - left_index]

    return A


def quickSort(A):
    left_index = 0
    right_index = A.size
    quickSortRecurse(A, left_index, right_index)


def quickSortRecurse(array, left_index, right_index):
    if right_index > left_index:  # Making sure array has size
        pivot_index = (left_index + right_index) // 2  # Middle element selection
        new_pivot_index = doPartitioning(array, left_index, right_index, pivot_index)

        quickSortRecurse(array, left_index, new_pivot_index - 1)  # Sort left partition
        quickSortRecurse(array, new_pivot_index + 1, right_index)  # Sort right partition
    return array


def doPartitioning(array, left_index, right_index, pivot_index):
    pivot_value = array[pivot_index]
    # Moves pivot to end for easier sorting of smaller values into left sub-array
    array[pivot_index], array[right_index] = array[right_index], pivot_value

    current_index = left_index  # The inserting index of left sub-array

    for ii in range(left_index, right_index):
        if array[ii] < pivot_value:  # Array element is smaller than pivot
            array[ii], array[current_index] = array[current_index], array[ii]
            current_index += 1

    new_pivot_index = current_index  # Accounts for uneven array sizes
    # Moving start of right sub-array to end of right sub-array
    array[right_index] = array[new_pivot_index]
    array[new_pivot_index] = pivot_value  # Re-placing pivot at end of left array

    return new_pivot_index
