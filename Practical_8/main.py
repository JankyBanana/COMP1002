#
# Main program section for running practical 8 code, uses code from Practical_7's main.py
#


import heap
import numpy as np

from Practical_8.heap import DSAHeap, DSAHeapEntry

csv_file = open('RandomNames7000.csv', 'r')
array = np.full(7000,None, dtype=object)

for x in range(7000):
    line = csv_file.readline()

    priority = ''
    data = ''
    comma_index = 0
    comma_found = False

    for i in range(len(line)):
        if line[i] == ',':
            comma_found = True
            comma_index = i
            break

    for i in range(comma_index):
        priority += line[i]
    priority = int(priority)

    for i in range(comma_index + 1, len(line) - 1):
        data += line[i]

    array[x] = DSAHeapEntry(priority, data)

sorted_array = DSAHeap.heap_sort(array)
print(sorted_array[0].priority)
print(sorted_array[1].priority)
print(sorted_array[2].priority)



# Testing code for heap.py
# def int_to_char(num):
#     if 0 < num < 27:
#         return chr(num + 96)
#
# x = heap.DSAHeap(size=30)
#
# for i in range(1, 27):
#     x.add(i, int_to_char(i))
#
# x.display()
#
# a = x.remove()
# x.display()
# print(a.priority, a.priority)
