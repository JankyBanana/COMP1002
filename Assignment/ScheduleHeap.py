#
# Luke Lummis, 22229146 - COMP1002 Assignment
#
# Implementation of a heap to handle scheduling deliveries accounting for priority and
# estimated delivery time using data from the customer hash-table and the route graph
#


import DSAHeap as h
import RouteGraph as RG


def main():
    schedule_heap = h.DSAHeap(size=110)

    hash_import = input("Import customer data from: ")
    graph_import =input("Import address data from: ")

    route_graph = RG.export('import', file=graph_import)

    with open(hash_import, 'r') as hash_file:
        line = hash_file.readline().strip('\n')

        while line:
            id = ""
            name = ""
            address = ""
            priority = ""
            status = ""

            current_field = 1
            i = 0

            while i < len(line):
                c = line[i]

                if c == ',':
                    current_field += 1
                    i += 1
                    continue

                if current_field == 1:
                    id += c
                elif current_field == 2:
                    name += c
                elif current_field == 3:
                    address += c
                elif current_field == 4:
                    priority += c
                elif current_field == 5:
                    status += c

                i += 1
            print(line)
            line = hash_file.readline().strip('\n')


            travel_time = RG.export('travel_time', graph=route_graph, start='a', end=address)
            if priority == 'None':
                priority = 0

            if travel_time == 0:
                priority = (6 - int(priority))
            else:
                priority = (6 - int(priority)) + 1000 / travel_time
            data = id
            schedule_heap.add(priority, travel_time, data)
    schedule_heap.heap_sort()
    schedule_heap.display()

    with open("ScheduleHeap.csv", "w") as f:
        txt_string = ''

        for entry in schedule_heap.heap_array:
            if entry is None:
                pass
            else:
                txt_string += f'{entry.priority},{entry.travel_time},{entry.data}\n'
        f.write(txt_string)

if __name__ == "__main__":
    main()
