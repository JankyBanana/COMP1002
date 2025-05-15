#
# Main program section for running practical 8 code, uses code from Practical_7's main.py
#


import numpy as np

import heap as h

with open('RandomNames7000.csv', 'r') as csv_file:
    csv_array = np.full(7000, None, dtype=object)

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

        for i in range(comma_index + 1, len(line) - 1):
            data += line[i]

        csv_array[x] = h.DSAHeapEntry(int(priority), data)

# saving csv array
with open("csv_array.txt", "w") as f:
    txt_string = ''

    for entry in csv_array:
        txt_string += f'{entry.priority},{entry.data}\n'
    f.write(txt_string)

# creating csv heap from csv array and saving it
csv_heap = h.DSAHeap(size=7000)
for entry in csv_array:
    csv_heap.add(entry.priority, entry.data)

with open("csv_heap_raw.txt", "w") as f:
    txt_string = ''

    for entry in csv_heap.heap_array:
        txt_string += f'{entry.priority},{entry.data}\n'
    f.write(txt_string)

# heapSorting and saving csv heap
csv_heap.heap_sort()
with open("RandomNames_HeapSort.txt", "w") as f:
    txt_string = ''

    for entry in csv_heap.heap_array:
        txt_string += f'{entry.priority},{entry.data}\n'
    f.write(txt_string)
