#
# Rebuild of directional graph class implementation for practical 6
#


import DSALinkedList as ll
import DSAStack as s
import DSAQueue as q


def alpha_order(char: str):
    ascii_value = ord(char)

    if 97 <= ascii_value <= 122:
        return ascii_value - 70
    elif 65 <= ascii_value <= 90:
        return ascii_value - 64


class DSAGraph:
    class DSAGraphEdge:
        def __init__(self, target_label: str, weight: float = 1.0):
            self.target_label = target_label
            self.weight = weight

    class DSAGraphVertex:
        def __init__(self, label: str, data: object = None):
            self.label = label
            self.data = data
            self.visited = False
            self.degree = 0
            self.edges = ll.DSALinkedList()

        def _add_edge(self, target_label: str, weight: float = 1.0):
            current_edge = self.edges.head

            while current_edge is not None:
                if current_edge.data.target_label == target_label:
                    current_edge.data.weight = weight
                    return
                current_edge = current_edge.next

            new_edge = DSAGraph.DSAGraphEdge(target_label, weight)
            self.edges.insert_last(new_edge)
            self.degree += 1

        def _remove_edge(self, target_label: str):
            current_edge = self.edges.head

            while current_edge is not None:
                if current_edge.data.target_label == target_label:
                    self.edges.remove(current_edge.data)
                    self.degree -= 1
                    return True
                current_edge = current_edge.next

            return False

        def _get_adjacent(self):
            return self.edges

        def _get_edge_weight(self, target_label):
            current_edge = self.edges.head

            while current_edge is not None:
                if current_edge.data.target_label == target_label:
                    return current_edge.data.weight
                current_edge = current_edge.next

            return None

        def set_visited(self):
            self.visited = True

        def clear_visited(self):
            self.visited = False

        def _sort_edges(self):
            if self.edges.count <= 1:
                return

            current_edge = self.edges.head

            while current_edge is not None:
                next_edge = current_edge.next
                smallest_edge = current_edge

                while next_edge is not None:
                    if alpha_order(next_edge.data.target_label) < alpha_order(smallest_edge.data.target_label):
                        smallest_edge = next_edge
                    next_edge = next_edge.next

                if smallest_edge != current_edge:
                    temp_data = current_edge.data
                    current_edge.data = smallest_edge.data
                    smallest_edge.data = temp_data

                current_edge = current_edge.next

    def __init__(self):
        self.vertices = ll.DSALinkedList()
        self.current_vertex = None

    def add_vertex(self, label: str, data: object = None):
        if label is None:
            raise ValueError("Vertex must have a label")

        current_vertex = self.vertices.head

        while current_vertex is not None:
            if current_vertex.data.label == label:
                raise ValueError(f"Vertex with label '{label}' already exists")

            current_vertex = current_vertex.next

        new_vertex = self.DSAGraphVertex(label, data)
        self.vertices.insert_last(new_vertex)

    def add_edge(self, source: str, sink: str, weight: float):
        source_vertex = self.get_vertex(source)
        sink_vertex = self.get_vertex(sink)

        if source_vertex is None:
            raise ValueError(f"Source vertex '{source}' not found")
        if sink_vertex is None:
            raise ValueError(f"Sink vertex '{sink}' not found")

        source_vertex.data._add_edge(sink, weight)
        if source is not sink:
            sink_vertex.data._add_edge(source, weight)

    def delete_vertex(self, target_label: str):
        current_vertex = self.vertices.head

        while current_vertex is not None:
            if current_vertex.data._remove_edge(target_label):
                pass
            current_vertex = current_vertex.next

        current_vertex = self.vertices.head

        while current_vertex is not None:
            if current_vertex.data.label == target_label:
                self.vertices.remove(current_vertex.data)
                return
            current_vertex = current_vertex.next

        raise ValueError(f"Vertex '{target_label}' not found")

    def delete_edge(self, source: str, sink: str):
        source_vertex = self.get_vertex(source)
        sink_vertex = self.get_vertex(sink)

        if source_vertex is None:
            raise ValueError(f"Source vertex '{source}' not found")
        if sink_vertex is None:
            raise ValueError(f"Sink vertex '{sink}' not found")

        source_removed = source_vertex.data._remove_edge(sink)

        if source != sink:
            sink_vertex.data._remove_edge(source)

        if not source_removed:
            raise ValueError(f"Edge from '{source}' to '{sink}' not found")

    def has_vertex(self, vertex_label: str):
        return self.get_vertex(vertex_label) is not None

    def vertex_count(self):
        return self.vertices.count

    def edge_count(self):
        total_edges = 0
        current_vertex = self.vertices.head

        while current_vertex is not None:
            current_edge = current_vertex.data.edges.head

            while current_edge is not None:
                if current_vertex.data.label <= current_edge.data.target_label:
                    total_edges += 1
                current_edge = current_edge.next
            current_vertex = current_vertex.next

        return total_edges

    def get_vertex(self, vertex_label: str):
        current_vertex = self.vertices.head

        while current_vertex is not None:
            if current_vertex.data.label == vertex_label:
                return current_vertex
            current_vertex = current_vertex.next

        return None

    def get_adjacent(self, vertex_label: str):
        vertex = self.get_vertex(vertex_label)

        if vertex is None:
            raise ValueError(f"Vertex '{vertex_label}' not found")
        return vertex.data.get_adjacent()

    def is_adjacent(self, source: str, sink: str):
        source_vertex = self.get_vertex(source)

        if source_vertex is None:
            return False

        current_edge = source_vertex.data.edges.head

        while current_edge is not None:
            if current_edge.data == sink:
                return True
            current_edge = current_edge.next

        return False

    def display_as_list(self):
        self.sort()

        display_list = ""
        current_vertex = self.vertices.head

        while current_vertex is not None:
            current_vertex.data._sort_edges()
            display_list += f"{current_vertex.data.label} |"
            current_edge = current_vertex.data.edges.head

            while current_edge is not None:
                display_list += f" {current_edge.data.target_label}({current_edge.data.weight})"
                current_edge = current_edge.next

            display_list += "\n"
            current_vertex = current_vertex.next

        print(f"Graph adjacency list:\n{display_list}")

    def sort(self):
        if self.vertices.count <= 1:
            return

        current_vertex = self.vertices.head

        while current_vertex is not None:
            next_vertex = current_vertex.next
            smallest_vertex = current_vertex

            while next_vertex is not None:
                if alpha_order(next_vertex.data.label) < alpha_order(smallest_vertex.data.label):
                    smallest_vertex = next_vertex
                next_vertex = next_vertex.next

            if smallest_vertex != current_vertex:
                temp_data = current_vertex.data
                current_vertex.data = smallest_vertex.data
                smallest_vertex.data = temp_data

            current_vertex = current_vertex.next

    def clear_visited(self):
        current_node = self.vertices.head

        while current_node is not None:
            current_node.data.visited = False
            current_node = current_node.next

    def breadth_first_search(self, start_label: str = None):
        self.sort()
        self.clear_visited()

        output_string = f"\nVertices reachable from vertex '{start_label}': [Vertex, Hops]\n"
        vertex_queue = q.ShufflingQueue()
        hop_queue = q.ShufflingQueue()

        if start_label:
            start_vertex = self.get_vertex(start_label)

            if start_vertex is None:
                raise ValueError(f"Start vertex '{start_label}' not found")

            if start_vertex.data.edges.count == 0:
                return ""

            output_string = self._bfs(start_vertex, output_string, vertex_queue, hop_queue)

        current_vertex_node = self.vertices.head

        while current_vertex_node is not None:
            if not current_vertex_node.data.visited:
                if current_vertex_node.data.edges.count == 0:
                    current_vertex_node.data.visited = True
                else:
                    output_string = self._bfs(current_vertex_node, output_string, vertex_queue, hop_queue)
            current_vertex_node = current_vertex_node.next

        return output_string.strip()

    def _bfs(self, start_vertex, output_string, vertex_queue, hop_queue):
        start_vertex.data.visited = True
        vertex_queue.enqueue(start_vertex)
        hop_queue.enqueue(0)
        hop_string = ''

        while not vertex_queue.is_empty():
            current_vertex = vertex_queue.dequeue()
            current_hops = hop_queue.dequeue()

            edge_node = current_vertex.data.edges.head

            while edge_node is not None:
                sink_vertex_node = self.get_vertex(edge_node.data.target_label)

                if sink_vertex_node and not sink_vertex_node.data.visited:
                    sink_vertex_node.data.visited = True
                    new_hops = current_hops + 1

                    vertex_queue.enqueue(sink_vertex_node)
                    hop_queue.enqueue(new_hops)

                    hop_string += f"{sink_vertex_node.data.label}, {new_hops}\n"
                    output_string += f"{current_vertex.data.label}{sink_vertex_node.data.label} "

                edge_node = edge_node.next

        return f"{output_string}\n{hop_string}"

    def depth_first_search(self, start_label: str = None):
        self.sort()
        self.clear_visited()

        output_string = f"\n\nStart vertex: {start_label}\n"
        vertex_stack = s.DSAStack()
        path_stack = s.DSAStack()
        cycle_list = ll.DSALinkedList()

        if start_label:
            start_vertex = self.get_vertex(start_label)

            if start_vertex is None:
                raise ValueError(f"Start vertex '{start_label}' not found")
            if start_vertex.data.edges.count == 0:
                return ""

            output_string = self._dfs(start_vertex, output_string, vertex_stack, path_stack, cycle_list)

        current_vertex_node = self.vertices.head

        while current_vertex_node is not None:
            if not current_vertex_node.data.visited:
                if current_vertex_node.data.edges.count == 0:
                    current_vertex_node.data.visited = True
                else:
                    output_string = self._dfs(current_vertex_node, output_string, vertex_stack, path_stack, cycle_list)
            current_vertex_node = current_vertex_node.next

        output_string += self.cycle_format(cycle_list)

        return output_string.strip()

    def _dfs(self, source_vertex, output_string, vertex_stack, path_stack, cycle_list):
        vertex_stack.push(source_vertex)
        path_stack.push(source_vertex.data.label)
        source_vertex.data.visited = True

        while not vertex_stack.is_empty():
            current_vertex = vertex_stack.peek()
            current_edge = current_vertex.data.edges.head

            found_unvisited = False

            while current_edge is not None:
                sink_vertex = self.get_vertex(current_edge.data.target_label)

                if sink_vertex:
                    if self.in_path(path_stack, current_edge.data.target_label):
                        cycle_nodes = self.cycle_path(path_stack, current_edge.data.target_label)

                        length = 0
                        node = cycle_nodes.head

                        while node is not None:
                            length += 1
                            node = node.next

                        if length >= 4:
                            cycle_list.insert_last(cycle_nodes)

                    if not sink_vertex.data.visited:
                        output_string += f"{current_vertex.data.label}{sink_vertex.data.label} "
                        sink_vertex.data.visited = True
                        vertex_stack.push(sink_vertex)
                        path_stack.push(sink_vertex.data.label)
                        found_unvisited = True
                        break

                current_edge = current_edge.next

            if not found_unvisited:
                vertex_stack.pop()

                if not path_stack.is_empty():
                    path_stack.pop()

        return output_string

    def in_path(self, path_stack, target_label):
        if path_stack.is_empty():
            return False

        temp_stack = s.DSAStack()
        found = False

        while not path_stack.is_empty():
            current_label = path_stack.pop()
            temp_stack.push(current_label)

            if current_label == target_label:
                found = True

        while not temp_stack.is_empty():
            path_stack.push(temp_stack.pop())

        return found

    def cycle_path(self, path_stack, cycle_start):
        temp_stack = s.DSAStack()
        cycle_nodes = ll.DSALinkedList()
        found_start = False

        while not path_stack.is_empty():
            label = path_stack.pop()
            temp_stack.push(label)

        while not temp_stack.is_empty():
            label = temp_stack.pop()
            path_stack.push(label)

            if label == cycle_start:
                found_start = True

            if found_start:
                cycle_nodes.insert_last(label)

        cycle_nodes.insert_last(cycle_start)

        return cycle_nodes

    def cycle_format(self, cycle_list):
        if cycle_list.is_empty():
            return "\nNo cycles detected."

        output = f"\n\n{cycle_list.count} Cycles detected:\n"
        cycle_number = 1
        current_cycle = cycle_list.head

        while current_cycle is not None:
            output += f"{cycle_number}. {current_cycle.data}\n"
            cycle_number += 1
            current_cycle = current_cycle.next

        return output

    def quickest_path(self, source_vertex, target_vertex):
        bfs_output = self.breadth_first_search(source_vertex)
        bfs_string = ''
        new_line_count = 0
        output_idx = 0

        while new_line_count < 2:
            output_element = bfs_output[output_idx]
            if output_element == '\n':
                new_line_count += 1

            if new_line_count < 1:
                output_idx += 1
            elif new_line_count < 2:
                bfs_string += bfs_output[output_idx]
                output_idx += 1

        bfs_string = bfs_string.strip()
        quickest_path = ''
        idx = len(bfs_string) - 1

        while idx > 0:
            element = bfs_string[idx]
            if element == target_vertex:
                quickest_path += f" {bfs_string[idx]}{bfs_string[idx-1]}"
                target_vertex = bfs_string[idx - 1]
                idx -= 6
            else:
                idx -= 3

        quickest_path = quickest_path[::-1]
        travel_time = 0
        idx = 0

        while idx < len(quickest_path):
            travel_time += int(self.get_vertex(quickest_path[idx]).data._get_edge_weight(quickest_path[idx + 1]))
            idx += 3

        return quickest_path.strip(), travel_time