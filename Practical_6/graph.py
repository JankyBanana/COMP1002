#
# Rebuild of directional graph class implementation for practical 6
#

import linkedlist as ll



class DSAGraph:
# ---------------- Private inner GraphNode class ----------------#
    class DSAGraphVertex:
        def __init__(self, label: str, data: object):
            self.label = label
            self.data = data
            self.visited = False
            self.in_degree = 0
            self.out_degree = 0
            self.edges = ll.DSALinkedList()

        def get_adjacent_to(self):
            next_edge = self.edges.head
            adjacent_list = ll.DSALinkedList()

            while next_edge is not None:
                if next_edge.data[0] == self.label:
                    adjacent_list.insertLast(next_edge.data)
                next_edge = next_edge.next
            return adjacent_list

        def get_adjacent_from(self):
            next_connection = self.edges.head
            adjacent_list = ll.DSALinkedList()

            while next_connection is not None:
                if next_connection.data[1] == self.label:
                    adjacent_list.insertLast(next_connection.data)
                next_connection = next_connection.next
            return adjacent_list

        def add_edge(self, target_label: str, direction: str="o"):
            if direction == "o":
                edge = self.label + target_label
            elif direction == "i":
                edge = target_label + self.label
            else:
                raise ValueError("Invalid direction arg")

            self.edges.insertLast(edge)

        def set_visited(self):
            self.visited = True

        def clear_visited(self):
            self.visited = False


demo = DSAGraph.DSAGraphVertex("A", 1)

demo.edges.insertLast("AB")
demo.edges.insertLast("AC")
demo.edges.insertLast("DA")
demo.edges.insertLast("EA")

print(demo.get_adjacent_to().display())
print(demo.get_adjacent_from().display())