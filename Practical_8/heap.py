#
# Implementation of a max-heap priority structure and HeapSort algorithm for COMP1002 practical 8
#


import numpy as np


def int_to_char(num):
    if 0 <= num < 27:
        return chr(num + 97)


class DSAHeapEntry:
    def __init__(self, priority: int, data: object = None):
        self.priority = priority
        self.data = data


class DSAHeap:
    def __init__(self, size: int = 100):
        self.heap_array = np.full(size, fill_value=None, dtype=object)
        self.size = self.heap_array.size
        self.count = 0

    def add(self, priority: int, data: object):
        if self.count == self.size:
            raise IndexError("Cannot add to a full heap array")
        elif self.count == 0:
            self.heap_array[0] = DSAHeapEntry(priority, data)
            self.count += 1
        else:
            end_idx = self.count
            self.heap_array[end_idx] = DSAHeapEntry(priority, data)
            self.heap_array = self._trickle_up(end_idx, self.heap_array)
            self.count += 1

    def remove(self):
        if self.count == 0:
            raise IndexError("Cannot remove from an empty heap array")
        elif self.count == 1:
            top = self.heap_array[0]
            self.heap_array[0] = None
            self.count -= 1
            print(f"Removed {top} = {top.priority} {top.data}")
            return top
        else:
            self.count -= 1
            top = self.heap_array[0]
            self.heap_array[0] = self.heap_array[self.count]
            self.heap_array[self.count] = None
            self.heap_array = self._trickle_down(0, self.heap_array)
            print(f"Removed: [{top.priority} {top.data}]")
            return top

    def display(self):
        print("Displaying heap array")
        for i in range(self.count):
            print(f"[Idx Priority Data]: {i} {self.heap_array[i].priority} {self.heap_array[i].data}")
        print('')

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

    def _trickle_down(self, current_idx, heap_array):
        left_child = current_idx * 2 + 1
        right_child = left_child + 1

        if left_child < self.count:
            bigger_child = left_child

            if right_child < self.count:
                if heap_array[left_child].priority < heap_array[right_child].priority:
                    bigger_child = right_child

            if heap_array[bigger_child].priority > heap_array[current_idx].priority:
                temp = heap_array[bigger_child]
                heap_array[bigger_child] = heap_array[current_idx]
                heap_array[current_idx] = temp
                return self._trickle_down(bigger_child, heap_array)
            else:
                return heap_array
        else:
            return heap_array

    def heapify(self):
        for i in range((self.count // 2) - 1, -1, -1):
            self.heap_array = self._trickle_down(i, self.heap_array)

    def heap_sort(self):
        self.heapify()
        original_count = self.count

        for i in range(self.count - 1, 0, -1):
            temp = self.heap_array[i]
            self.heap_array[i] = self.heap_array[0]
            self.heap_array[0] = temp
            self.count = i
            self._trickle_down(0, self.heap_array)
        self.count = original_count

print("----- Code Demo -----")
x = DSAHeap(size=30)

for i in range(0, 5):
    x.add(i, int_to_char(i))
x.display()

x.remove()
x.display()

x.heap_sort()
x.display()
