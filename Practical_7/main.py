#
# Main program file for practical 7
#


import hashtable as ht

csv_hash = ht.DSAHashTable()
csv_data = open('RandomNames7000.csv', 'r')
line_number = 0

while True:
    line = csv_data.readline()
    if not line:
        break

    line_number += 1

    key = ''
    data = ''
    comma_index = 0
    comma_found = False

    for i in range(len(line)):
        if line[i] == ',':
            comma_found = True
            comma_index = i
            break

    for i in range(comma_index):
        data += line[i]

    for i in range(comma_index + 1, len(line) - 1):
        key += line[i]

    csv_hash.put(key, data)
    print(f"Line number: {line_number} Line: {line}Key: {key} Data: {data}\n")
csv_data.close()

print(csv_hash.num_elements)

with open('RandomNames7000_Hashed.csv', 'w') as f:
    csv_string = ''

    for entry in csv_hash.hash_array:
        csv_string += f'{entry.data},{entry.key}\n'
    f.write(csv_string)

# Code test suite
# demo = ht.DSAHashTable()
# demo.display()
#
# for i in range(31):
#     print(f"Inserting key: {i}, Data: {i}, Hash Index: {demo.hash(str(i))}")
#     demo.put(str(i), i)
# print('\n')
#
# demo.display()
#
# print(f"Getting 27 gives: {demo.get('27')}")
# print('\n')
#
# demo.display()
#
# demo.remove('24')
# demo.display()
#
# print(f"Does demo have the key '23'? {demo.has_key('23')}")
# print(f"Does demo have the key '31'? {demo.has_key('31')}")
