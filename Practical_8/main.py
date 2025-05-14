#
# Main program section for running practical 8 code
#


import heap


def int_to_char(num):
    if 0 < num < 27:
        return chr(num + 96)


x = heap.DSAHeap(size=30)

for i in range(1, 27):
    x.add(i, int_to_char(i))

    for i in range(x.count):
        print(i, x.heap_array[i].priority, x.heap_array[i].data)
    print('\n')