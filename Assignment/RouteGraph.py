#
# Luke Lummis, 22229146 - COMP1002 Assignment
#
# Implementation of an undirected graph for delivery route optimization using Breadth-First Searches
# to identify any inefficient loops and the fastest route between 2 nodes
#
# Based on main.py from the Practical 6 submission
#


from Assignment.DSAModules import DSAGraph as g
import numpy as np


def main():
    user_input = input(f"\nGraph operations listed below. Select using square brackets [...]\n"
                       f"------------------------\n"
                       f" Add Vertex             [ADDV <LABEL> <DATA>]\n"
                       f" Add Edge               [ADDE <SOURCE> <SINK> <WEIGHT>]\n"
                       f" Delete Vertex          [DELV <LABEL>]\n"
                       f" Delete Edge            [DELE <SOURCE> <SINK>]\n"
                       f" Display as List        [DAL]\n"
                       f" Breadth First Search   [BFS]\n"
                       f" Depth First Search     [DFS]\n"
                       f" Import graph           [IMPORT <filename.txt>]\n"
                       f"------------------------\n"
                       f"Input: ")

    route_graph = g.DSAGraph()
    inputs = string_seperator(user_input)

    while 1:
        try:
            inputs[0] = inputs[0].upper()

            if inputs[0] == "ADDV":
                label = inputs[1]
                try:
                    data = inputs[2]
                except IndexError:
                    data = None

                route_graph.add_vertex(label, data)
                print(f"Adding vertex with label '{label}' and data '{data}'")

            elif inputs[0] == "ADDE":
                route_graph.add_edge(inputs[1], inputs[2], inputs[3])
                print(f"Adding edge from '{inputs[1]}' to '{inputs[2]}' with weight '{inputs[3]}'")

            elif inputs[0] == "DELV":
                route_graph.delete_vertex(inputs[1])
                print(f"Deleting vertex with label '{inputs[1]}'")

            elif inputs[0] == "DELE":
                route_graph.delete_edge(inputs[1], inputs[2])
                print(f"Deleting edge from vertex '{inputs[1]}' to vertex '{inputs[2]}'")

            elif inputs[0] == "DAL":
                route_graph.display_as_list()

            elif inputs[0] == "BFS":
                print(route_graph.breadth_first_search())

            elif inputs[0] == "DFS":
                print(route_graph.depth_first_search())

            elif inputs[0] == "IMPORT":
                with open(inputs[1], 'r') as graph_file:

                    print(f"Importing graph from {inputs[1]}")
                    line = graph_file.readline()
                    line_idx = 0

                    for i in range(len(line)):
                        if line[line_idx] != ',' and line[line_idx] != '\n':
                            route_graph.add_vertex(line[line_idx])
                            print(f"Adding vertex with label '{line[line_idx]}'")
                        line_idx += 1

                    line = graph_file.readline().strip('\n')

                    while line:
                        route_graph.add_edge(line[0], line[1], float(line[3:]))
                        print(f"Adding edge from '{line[0]}' to '{line[1]}' with weight '{line[3:]}'")
                        line = graph_file.readline().strip('\n')

            elif inputs[0] == "EXIT":
                print("Exiting")
                break

            else:
                print("Invalid input.")

        except Exception as e:
            print(e)

        user_input = input("Input: ")
        inputs = string_seperator(user_input)


def string_seperator(input_str):
    temp_string = ""
    word_count = 1

    for idx in range(1, len(input_str)):
        if input_str[idx - 1] != " " and input_str[idx] == " ":
            word_count += 1

    results = np.full(word_count, None)
    result_idx = 0

    for idx in range(len(input_str)):
        if input_str[idx] != " ":
            temp_string += input_str[idx]

        elif idx > 0 and input_str[idx - 1] != " ":
            results[result_idx] = temp_string
            temp_string = ""
            result_idx += 1

    if temp_string:
        results[result_idx] = temp_string

    return results


main()
