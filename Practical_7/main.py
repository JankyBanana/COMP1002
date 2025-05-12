#
# Main program file for practical 7
#


import hashtable as ht

demo = ht.DSAHashTable()
demo.display()

for i in range(31):
    print(f"Inserting key: {i}, Data: {i}, Hash Index: {demo.hash(str(i))}")
    demo.put(str(i), i)
print('\n')

demo.display()

print(f"Getting 27 gives: {demo.get('27')}")
print('\n')

demo.display()

demo.remove('24')
demo.display()

print(f"Does demo have the key '23'? {demo.has_key('23')}")
print(f"Does demo have the key '31'? {demo.has_key('31')}")