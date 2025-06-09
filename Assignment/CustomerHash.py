#
# Luke Lummis, 22229146 - COMP1002 Assignment
#
# Implementation of a hash-table for the storage and lookup of customer data using a customer ID
# to aid in the calculation of delivery priority for the schedule heap
#


import DSAHashTable as ht
import numpy as np


def main():
    customer_hash = ht.DSAHashTable()

    user_input = input(f"\nHash operations listed below. Select using square brackets [...]\n"
                       f"------------------------\n"
                       f" Insert Customer    [INS  <ID>, <NAME>, <ADDRESS>, <PRIORITY>, <STATUS>]\n"
                       f" Remove Customer    [RMV <ID>]\n"
                       f" Get Customer       [GET <ID>]\n"
                       f" Customer Check     [CHK <ID>]\n"
                       f" Display            [DISP]\n"
                       f" Load Factor        [LF]\n"
                       f" Import             [IMPORT <filename.csv>]\n"
                       f" Save hash table    [SAVE]\n"
                       f" Exit               [EXIT]\n"
                       f"------------------------\n"
                       f"Input: ")

    inputs = string_seperator(user_input)

    while 1:
        try:
            inputs[0] = inputs[0].upper()

            if inputs[0] == "INS":
                id = inputs[1]
                name = inputs[2]
                address = inputs[3]
                priority = inputs[4]
                status = inputs[5]

                customer_hash.put(id, name, address, priority, status)
                print(f"Adding customer - ID: {id}  NAME: {name}  ADDRESS: {address}  PRIORITY: {priority}  STATUS: {status}\n")

            elif inputs[0] == "RMV":
                customer_hash.remove(inputs[1])
                print(f"Removing customer [ID:{inputs[1]}]")

            elif inputs[0] == "GET":
                print(f"Getting customer [ID:{inputs[1]}]")
                print(customer_hash.get(inputs[1]))

            elif inputs[0] == "CHK":
                print(f"Checking if customer [ID:{inputs[1]}] is present in the hash table.")
                print(customer_hash.has_id(inputs[1]))

            elif inputs[0] == "DISP":
                print("Displaying hash table.")
                customer_hash.display()

            elif inputs[0] == "LF":
                lf = customer_hash.load_factor()
                print(f"Customer hash table load factor is: {lf}")

            elif inputs[0] == "IMPORT":
                print(f"Importing graph from {inputs[1]}")

                with open(inputs[1], 'r') as hash_file:
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
                        line = hash_file.readline().strip('\n')

                        print(f"Adding customer - ID: {id}  NAME: {name}  ADDRESS: {address}  PRIORITY: {priority}  STATUS: {status}\n")
                        customer_hash.put(id, name, address, priority, status)

            elif inputs[0] == "SAVE":
                with open('CustomerHashTable.csv', 'w') as file:
                    csv_string = ''

                    for entry in customer_hash.hash_array:
                        csv_string += f'{entry.ID},{entry.Name},{entry.Address},{entry.Priority},{entry.Status}\n'
                    file.write(csv_string)

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
