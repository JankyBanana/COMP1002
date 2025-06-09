#
# Luke Lummis, 22229146 - COMP1002 Assignment
#
# Implementation of merge and quick sorting algorithms for the sorting and storage
# of each day's delivery records
#
# Based on DSAsorts.py from practical 9 submission
#

import numpy as np


def mergeSort(A):
    left_index = 0
    right_index = A.size - 1
    mergeSortRecurse(A, left_index, right_index)


def mergeSortRecurse(array, left_index, right_index):
    if left_index < right_index:
        mid_index = (left_index + right_index) // 2

        mergeSortRecurse(array, left_index, mid_index)
        mergeSortRecurse(array, mid_index + 1, right_index)

        merge(array, left_index, mid_index, right_index)
    return array


def merge(array, left_index, mid_index, right_index):
    temp_size = right_index - left_index + 1
    temp_array = np.zeros(temp_size)
    ii = left_index
    jj = mid_index + 1
    kk = 0

    while ii <= mid_index and jj <= right_index:
        if array[ii] <= array[jj]:
            temp_array[kk] = array[ii]
            ii = ii + 1
        else:
            temp_array[kk] = array[jj]
            jj = jj + 1
        kk = kk + 1

    for ii in range(ii, mid_index + 1):
        temp_array[kk] = array[ii]
        kk = kk + 1

    for jj in range(jj, right_index + 1):
        temp_array[kk] = array[jj]
        kk = kk + 1

    for kk in range(left_index, right_index + 1):
        array[kk] = temp_array[kk - left_index]

    return array


def quickSortMedian3(array):
    left_index = 0
    right_index = len(array) - 1
    quickSortRecurseMedain3(array, left_index, right_index)


def quickSortRecurseMedain3(array, left_index, right_index):
    if right_index > left_index:  # Making sure array has size
        pivot_index = medianOf3(array, left_index, right_index)  # Median of 3 elements selection
        new_pivot_index = doPartitioning(array, left_index, right_index, pivot_index)

        quickSortRecurseMedain3(array, left_index, new_pivot_index - 1)  # Sort left partition
        quickSortRecurseMedain3(array, new_pivot_index + 1, right_index)  # Sort right partition
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


def medianOf3(array, low, high):
    low_index = low
    high_index = high
    mid_index = (low_index + high_index) // 2

    low = array[low_index]
    mid = array[mid_index]
    high = array[high_index]

    if mid <= low <= high or high <= low <= mid:
        median_index = low_index
    elif low <= mid <= high or high <= mid <= low:
        median_index = mid_index
    else:
        median_index = high_index

    return median_index
