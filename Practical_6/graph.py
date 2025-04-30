#
# Rebuild of directional graph class implementation for practical 6
#


import linkedlist as ll


class DSAGraph:
    class DSAGraphVertex:
        def __init__(self, label: str, data: object):
            self.label = label
            self.data = data
            self.visited = False
            self.in_degree = 0
            self.out_degree = 0
            self.edges = ll.DSALinkedList()

        def _get_adjacent_to(self):
            next_edge = self.edges.head
            adjacent_list = ll.DSALinkedList()

            while next_edge is not None:
                if next_edge.data[0] == self.label:
                    adjacent_list.insertLast(next_edge.data)
                next_edge = next_edge.next
            return adjacent_list

        def _get_adjacent_from(self):
            next_connection = self.edges.head
            adjacent_list = ll.DSALinkedList()

            while next_connection is not None:
                if next_connection.data[1] == self.label:
                    adjacent_list.insertLast(next_connection.data)
                next_connection = next_connection.next
            return adjacent_list

        def _add_edge(self, target_label: str, direction: str="o"):
            if direction == "o":
                edge = self.label + target_label
            elif direction == "i":
                edge = target_label + self.label
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

    def has_vertex(self):
        pass

    def has_edge(self):
        pass

    def vertex_count(self):
        pass

    def edge_count(self):
        pass

    def get_vertex(self):
        pass

    def get_adjacent_to(self):
        pass

    def get_adjacent_from(self):
        pass

    def is_adjacent_to(self):
        pass

    def is_adjacent_from(self):
        pass

    def display_as_list(self):
        pass

    def display_as_matrix(self):
        pass

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
        pass

    def depth_search(self):
        pass

    def breadth_search(self):
        pass