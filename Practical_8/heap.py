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
        pass

    def remove(self):
        pass

    def display(self):
        pass

    def _trickle_up(self, index: int):
        pass

    def _trickle_down(self, index: int):
        pass


def heat_sort(array):
    pass
