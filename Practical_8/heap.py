#
# Implementation of a max-heap data structure and HeapSort algorithm for COMP1002 practical 8
#


import numpy as np


class DSAHeapEntry:
    def __init__(self, priority: int, data: object = None):
        self.prior = priority
        self.data = data


class DSAHeap:
    def __init__(self, size: int = 100):
        self.size = size
        self.heap_array = np.full(size, fill_value=None, dtype=object)
        self.count = 0

    def add(self, priority: int, data: object):
        if self.count == self.size:
            raise OverflowError("Cannot add to a full heap array")
        elif self.count == 0:
            self.heap_array[0] = DSAHeapEntry(priority, data)
            self.count += 1
        else:
            end_idx = self.count
            self.heap_array[end_idx] = DSAHeapEntry(priority, data)
            self.heap_array = self._trickle_up(end_idx, self.heap_array)
            self.count += 1

    def remove(self):
        pass

    def display(self):
        pass

    def _trickle_up(self, current_idx, heap_array):
        if current_idx > 0:
            parent_idx = int((current_idx - 1) / 2)

            if heap_array[current_idx].priority > heap_array[parent_idx].priority:
                temp = heap_array[parent_idx]
                heap_array[parent_idx] = heap_array[current_idx]
                heap_array[current_idx] = temp
                return self._trickle_up(parent_idx, heap_array)
            else:
                return heap_array
        else:
            return heap_array

    def _trickle_down(self, index: int):
        pass


def heat_sort(array):
    pass
