#
# Rebuild of directional graph class implementation for practical 6
#


from Practical_6 import linkedlist as ll
import numpy as np


def alpha_order(char:str):
    ascii_value = ord(char)

    if ascii_value >= 97 and ascii_value <= 122:
        return ascii_value - 70
    elif ascii_value >= 65 and ascii_value <= 90:
        return ascii_value - 64

class DSAGraph:
    class DSAGraphVertex:
        def __init__(self, label: str, data: object):
            self.label = label
            self.data = data
            self.visited = False
            self.in_degree = 0
            self.out_degree = 0
            self.edges = ll.DSALinkedList()

        def _get_adjacent(self):
            return self.edges

        def _add_edge(self, target_label: str, direction: str="o"):
            if direction == "o":
                edge = self.label + target_label
                self.out_degree += 1
            elif direction == "i":
                edge = target_label + self.label
                self.in_degree += 1
            else:
                raise ValueError("Invalid direction arg")

            current_edge = self.edges.head
            while current_edge is not None:
                if edge == current_edge.data:
                    raise ValueError("Edge already present")
                current_edge = current_edge.next

            self.edges.insertLast(edge)

        def set_visited(self):
            self.visited = True

        def clear_visited(self):
            self.visited = False

        def _sort(self):
            current_edge = self.edges.head

            while current_edge is not None:
                next_edge = current_edge.next
                smallest_edge = current_edge

                while next_edge is not None:
                    if alpha_order(next_edge.data[0]) == alpha_order(smallest_edge.data[0]):
                        if alpha_order(next_edge.data[1]) < alpha_order(smallest_edge.data[1]):
                            smallest_edge = next_edge
                        next_edge = next_edge.next
                    elif alpha_order(next_edge.data[0]) != alpha_order(smallest_edge.data[0]):
                        if alpha_order(next_edge.data[0]) < alpha_order(smallest_edge.data[0]):
                            smallest_edge = next_edge
                        next_edge = next_edge.next

                if smallest_edge is not current_edge:
                    temp_data = current_edge.data
                    current_edge.data = smallest_edge.data
                    smallest_edge.data = temp_data

                current_edge = current_edge.next

    def __init__(self):
        self.vertices = ll.DSALinkedList()
        self.current_vertex = None

    def add_vertex(self, label: str, data: object=None):
        next_vertex = self.vertices.head

        while next_vertex is not None:
            if next_vertex.data.label == label:
                raise ValueError("Label is already in use by another vertex in the graph")
            next_vertex = next_vertex.next

        self.vertices.insertLast(self.DSAGraphVertex(label, data))

    def add_edge(self, source: str, sink: str):
        next_vertex = self.vertices.head

        source_exist = False
        sink_exist = False

        while next_vertex is not None:
            if next_vertex.data.label == source:
                source_exist = True
                source_vertex = next_vertex

            if next_vertex.data.label == sink:
                sink_exist = True
                sink_vertex= next_vertex

            next_vertex = next_vertex.next

        if not source_exist:
            raise Exception("Source not found")
        elif not sink_exist:
            raise Exception("Sink not found")

        source_vertex.data._add_edge(sink, "o")
        sink_vertex.data._add_edge(source, "i")

    def has_vertex(self, vertex_label: str):
        next_vertex = self.vertices.head

        while next_vertex is not None:
            if next_vertex.data.label == vertex_label:
                return True
            next_vertex = next_vertex.next
        return False

    def vertex_count(self):
        return self.vertices.nodes

    def edge_count(self):
        next_vertex = self.vertices.head
        in_degree_sum = 0
        out_degree_sum = 0

        while next_vertex is not None:
            in_degree_sum = in_degree_sum + next_vertex.data.in_degree
            out_degree_sum = out_degree_sum + next_vertex.data.out_degree
            next_vertex = next_vertex.next

        if in_degree_sum - out_degree_sum == 0:
            return in_degree_sum
        else:
            raise Exception("Sum of in-degrees and out-degrees do not match")

    def get_vertex(self, vertex_label: str):
        next_vertex = self.vertices.head

        while next_vertex is not None:
            if next_vertex.data.label == vertex_label:
                return next_vertex
            next_vertex = next_vertex.next

        return ValueError("Vertex not found")

    def get_adjacent(self, vertex_label: str):
        vertex = self.get_vertex(vertex_label)
        return vertex.data._get_adjacent()

    def is_adjacent(self, source: str, sink: str):
        source_vertex = self.get_vertex(source)
        next_edge = source_vertex.data.edges.head

        while next_edge is not None:
            if next_edge.data[0] == sink or next_edge.data[1] == sink:
                return True

            next_edge = next_edge.next
        return False

    def display_as_list(self):
        display_string = ""
        next_vertex = self.vertices.head

        while next_vertex is not None:
            next_edge = next_vertex.data.edges.head

            for i in range(next_vertex.data.edges.nodes):
                if (next_edge is not None and next_edge.data not in display_string
                        and next_edge.data[0] == next_vertex.data.label):
                    display_string += next_edge.data + " "
                next_edge = next_edge.next
            next_vertex = next_vertex.next
        print(display_string)

    def display_as_matrix(self):
        self.sort()

        vertex_array = np.zeros(self.vertices.nodes, dtype=str)
        size = self.vertices.nodes
        display_matrix = "  |"
        current_vertex = self.vertices.head

        for i in range(self.vertices.nodes):
            display_matrix += " " + current_vertex.data.label
            vertex_array[i] = current_vertex.data.label
            current_vertex = current_vertex.next

        display_matrix += "\n--+" + "--"*size
        current_vertex = self.vertices.head

        while current_vertex is not None:
            display_matrix += "\n" + current_vertex.data.label + " |"
            current_vertex.data._sort()
            vertex_edges = current_vertex.data.edges.display()

            for i in range(self.vertices.nodes):
                edge = current_vertex.data.label + vertex_array[i]

                if edge in vertex_edges:
                    display_matrix += " 1"
                else:
                    display_matrix += " 0"
            current_vertex = current_vertex.next
        print(display_matrix)

    def degree_in(self):
        pass

    def degree_out(self):
        pass

    def has_data(self):
        pass

    def next_vertex(self, mode: str=None, type: str="n"):
        if self.current_vertex is None:
            self.current_vertex = self.vertices.head

            if type == "n":
                return self.current_vertex
            elif type == "v":
                return self.current_vertex.data
        elif mode == "c":
            self.current_vertex = None
            return None

        if self.current_vertex.next is not None:
            self.current_vertex = self.current_vertex.next

            if type == "n":
                return self.current_vertex
            elif type == "v":
                return self.current_vertex.data
        else:
            self.current_vertex = self.current_vertex.next
            return self.current_vertex

    def sort(self):
        current_vertex = self.vertices.head

        while current_vertex is not None:
            next_vertex = current_vertex.next
            smallest_vertex = current_vertex

            while next_vertex is not None:
                if alpha_order(next_vertex.data.label) < alpha_order(smallest_vertex.data.label):
                    smallest_vertex = next_vertex
                next_vertex = next_vertex.next

            if smallest_vertex is not current_vertex:
                temp_data = current_vertex.data
                current_vertex.data = smallest_vertex.data
                smallest_vertex.data = temp_data

            current_vertex = current_vertex.next

    def depth_search(self):
        pass

    def breadth_search(self):
        pass