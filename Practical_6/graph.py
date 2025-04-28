#
# Rebuild of directional graph class implementation for practical 6
#

import linkedlist as ll



class DSAGraph:
# ---------------- Private inner GraphNode class ----------------#
    class DSAGraphNode:
        def __init__(self, label: str, data: object):
            self.label = label
            self.data = data
            self.visited = False
            self.in_degree = 0
            self.out_degree = 0
            self.connections = ll.DSALinkedList()

        def get_adjacent_to(self):
            nextConnection = self.connections.head

            while nextConnection is not None:
                if nextConnection._data[0] == self.label:
