#
# Main program section for practical 6
#

from Practical_6 import graph
import numpy as np


def string_seperator(input_str):
    temp_string = ""
    word_count = 1

    for idx in range(1, len(input_str)):
        if input_str[idx - 1] != " " and input_str[idx] == " ":
            word_count += 1

    results = np.full(word_count, None)
    result_indx = 0

    for idx in range(len(input_str)):
        if input_str[idx] != " ":
            temp_string += input_str[idx]
        elif idx > 0 and input_str[idx - 1] != " ":
            results[result_indx] = temp_string
            temp_string = ""
            result_indx += 1

    if temp_string:
        results[result_indx] = temp_string

    return results


demo = graph.DSAGraph()

userInput = input(f"\nGraph operations listed below. Select using square brackets [...]\n"
                  f"------------------------\n"
                  f" Add Vertex             [ADDV <LABEL> <DATA>]\n"
                  f" Add Edge               [ADDE <SOURCE> <SINK>]\n"
                  f" Delete Vertex          [DELV <LABEL>]\n"
                  f" Delete Edge            [DELE <SOURCE> <SINK>]\n"
                  f" Display as List        [DAL]\n"
                  f" Display as Matrix      [DAM]\n"
                  f" Breadth First Search   [BFS]\n"
                  f" Depth First Search     [DFS]\n"
                  f"------------------------\n"
                  f"Input: ")

inputs = string_seperator(userInput)

while 1:
    try:
        inputs[0] = inputs[0].upper()

        if inputs[0] == "ADDV":
            try:
                demo.add_vertex(inputs[1], inputs[2])
            except IndexError:
                demo.add_vertex(inputs[1], None)
        elif inputs[0] == "ADDE":
            try:
                demo.add_edge(inputs[1], inputs[2])
            except IndexError:
                raise Exception
        elif inputs[0] == "DELV":
            demo.delete_vertex(inputs[1])
        elif inputs[0] == "DELE":
            demo.delete_edge(inputs[1])
        elif inputs[0] == "DAL":
            demo.display_as_list()
        elif inputs[0] == "DAM":
            demo.display_as_matrix()
        elif inputs[0] == "BFS":
            print(demo.breadth_first_search())
        elif inputs[0] == "DFS":
            print(demo.depth_first_search())
        elif inputs[0] == "EXIT":
            break
        else:
            print("Invalid input. Ensure that all commands are capitalised.")
    except Exception:
        print("\nCommand provided was either invalid or missing an argument.")
    userInput = input("Input: ")
    inputs = string_seperator(userInput)