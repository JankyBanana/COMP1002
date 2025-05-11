#
# Main program section for practical 7
#


import DSAHashTable as HT

demo = HT.HashTable(31)
demo.display()
print('\n')

for i in range(31):
    print(f"Inserting key: {i}, Value: {demo.hash(str(i))}")
    demo.put(str(i), i)
print('\n')

demo.display()
print('\n')

print(f"Does demo have key 25? {demo.has_key("25")}")
print(f"Does demo have key 25? {demo.has_key("32")}")
print('\n')

a = demo.find("11")
print(f"Key of a: {a.key}, Value of a: {a.value}")
print('\n')

demo.remove('11')
demo.display()
print("\nValue of key 12 is:", demo.get("12"))