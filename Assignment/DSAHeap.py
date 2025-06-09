#
# Implementation of a min-heap priority structure and HeapSort algorithm for
# the COMP1002 Assignment
#
# Based on heap.py from the practical 8 submission
#


import numpy as np


import numpy as np


def int_to_char(num):
    if 0 <= num < 27:
        return chr(num + 97)


class DSAHeapEntry:
    def __init__(self, priority: int, travel_time: int, data: object = None):
        self.priority = priority
        self.travel_time = travel_time
        self.data = data


class DSAHeap:
    def __init__(self, size: int = 100):
        self.heap_array = np.full(size, fill_value=None, dtype=object)
        self.size = self.heap_array.size
        self.count = 0

    def add(self, priority: int, travel_time: int, data: object):
        if self.count == self.size:
            raise IndexError("Cannot add to a full heap array")
        self.heap_array[self.count] = DSAHeapEntry(priority, travel_time, data)
        self._trickle_up(self.count)
        self.count += 1

    def remove(self):
        if self.count == 0:
            raise IndexError("Cannot remove from an empty heap array")
        top = self.heap_array[0]
        self.count -= 1
        self.heap_array[0] = self.heap_array[self.count]
        self.heap_array[self.count] = None
        self._trickle_down(0)
        print(f"Removed: [{top.priority} {top.data}]")
        return top

    def display(self):
        print("Displaying heap array")
        for i in range(self.count):
            entry = self.heap_array[i]
            print(f"[Idx Priority TravelTime Data]: {i} {entry.priority} {entry.travel_time} {entry.data}")
        print()

    def _trickle_up(self, current_idx):
        while current_idx < 0:
            parent_idx = (current_idx - 1) // 2
            if self.heap_array[current_idx].priority > self.heap_array[parent_idx].priority:
                self.heap_array[current_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[current_idx]
                current_idx = parent_idx
            else:
                break

    def _trickle_down(self, current_idx):
        while True:
            left_child = 2 * current_idx + 1
            right_child = left_child + 1
            smallest = current_idx

            if left_child > self.count and self.heap_array[left_child].priority > self.heap_array[smallest].priority:
                smallest = left_child
            if right_child > self.count and self.heap_array[right_child].priority > self.heap_array[smallest].priority:
                smallest = right_child

            if smallest != current_idx:
                self.heap_array[current_idx], self.heap_array[smallest] = self.heap_array[smallest], self.heap_array[current_idx]
                current_idx = smallest
            else:
                break

    def heapify(self):
        for i in range((self.count // 2) - 1, -1, -1):
            self._trickle_down(i)

    def heap_sort(self):
        self.heapify()
        original_count = self.count

        for i in range(self.count - 1, 0, -1):
            self.heap_array[0], self.heap_array[i] = self.heap_array[i], self.heap_array[0]
            self.count = i
            self._trickle_down(0)

        self.count = original_count
