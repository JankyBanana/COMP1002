#
# Rebuild of directional graph class implementation for practical 6
#


import linkedlist as ll
import numpy as np
import DSAstack
import DSAqueue


def alpha_order(char:str):
    ascii_value = ord(char)

    if 97 <= ascii_value <= 122:
        return ascii_value - 70
    elif 65 <= ascii_value <= 90:
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
        self.sort()

        display_list = ""
        current_vertex = self.vertices.head

        while current_vertex is not None:
            display_list += current_vertex.data.label + " |"
            current_edge = current_vertex.data.edges.head

            while current_edge is not None:
                if (current_edge.data[0] == current_vertex.data.label
                    and current_edge.data[1] != current_vertex.data.label):
                    display_list += " " + current_edge.data[1]
                current_edge = current_edge.next
            display_list += "\n"
            current_vertex = current_vertex.next
        print(f"Graph as an adjacency list:\n\n"
              f"{display_list}")

    def display_as_matrix(self):
        self.sort()

        vertex_array = np.zeros((self.vertices.nodes, 2), dtype=str)
        size = self.vertices.nodes
        display_matrix = "  |"
        current_vertex = self.vertices.head

        for i in range(self.vertices.nodes):
            display_matrix += f" {i}"
            vertex_array[i, 1] = current_vertex.data.label
            vertex_array[i, 0] = i
            current_vertex = current_vertex.next

        display_matrix += "\n--+" + "--"*size
        current_vertex = self.vertices.head

        for i in range(self.vertices.nodes):
            display_matrix += f"\n{i} |"
            current_vertex.data._sort()
            vertex_edges = current_vertex.data.edges.display()

            for i in range(self.vertices.nodes):
                edge = current_vertex.data.label + vertex_array[i, 1]

                if edge in vertex_edges:
                    display_matrix += " 1"
                else:
                    display_matrix += " 0"
            current_vertex = current_vertex.next
        print(f"Graph as adjacency matrix:\n"
              f"Label lookup:\n{vertex_array}\n\n"
              f"{display_matrix}")

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

    def depth_first_search(self):
        self.sort()
        self.clear_visited()

        output_string = ""
        vertex_stack = DSAstack.DSAStack()

        current_vertex_node = self.vertices.head
        while current_vertex_node is not None:
            if not current_vertex_node.data.visited:
                output_string = self._dfs(current_vertex_node, output_string, vertex_stack)
            current_vertex_node = current_vertex_node.next

        return output_string

    def breadth_first_search(self):
        self.sort()
        self.clear_visited()

        output_string = ""
        vertex_queue = DSAqueue.ShufflingQueue()

        current_vertex_node = self.vertices.head

        while current_vertex_node is not None:
            if not current_vertex_node.data.visited:
                current_vertex_node.data.visited = True
                vertex_queue.enqueue(current_vertex_node)

                while not vertex_queue.is_empty():
                    current_vertex = vertex_queue.dequeue()
                    edge_node = current_vertex.data.edges.head

                    while edge_node is not None:
                        if edge_node.data[0] == current_vertex.data.label:
                            sink_vertex_node = self.get_vertex(edge_node.data[1])

                            if not sink_vertex_node.data.visited:
                                sink_vertex_node.data.visited = True
                                vertex_queue.enqueue(sink_vertex_node)
                                output_string += current_vertex.data.label + sink_vertex_node.data.label + " "
                        edge_node = edge_node.next

            current_vertex_node = current_vertex_node.next

        return output_string.strip()

    def clear_visited(self):
        current_node = self.vertices.head

        while current_node is not None:
            current_node.data.visited = False
            current_node = current_node.next

    def _dfs(self, source_vertex, output_string, vertex_stack):
        vertex_stack.push(source_vertex)
        source_vertex.data.visited = True

        while not vertex_stack.is_empty():
            current_vertex = vertex_stack.peek()
            current_edge = current_vertex.data.edges.head

            found_unvisited = False
            while current_edge is not None:
                if current_edge.data[0] == current_vertex.data.label:
                    sink_vertex = self.get_vertex(current_edge.data[1])

                    if not sink_vertex.data.visited:
                        output_string += current_vertex.data.label + sink_vertex.data.label + " "
                        sink_vertex.data.visited = True
                        vertex_stack.push(sink_vertex)
                        found_unvisited = True
                        break

                current_edge = current_edge.next

            if not found_unvisited:
                vertex_stack.pop()

        return output_string