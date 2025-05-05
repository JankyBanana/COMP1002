#
# Hash table implementation for COMP1002 practical 7
#


import numpy as np


def next_prime(start_value: int):
    if start_value % 2 == 0:
        prime_value = start_value - 1
    else:
        prime_value = start_value - 2

    is_prime = False

    while not is_prime:
        prime_value += 2
        divisor = 3
        is_prime = True
        root_value = prime_value ** (1 / 2)

        while divisor <= root_value and is_prime:
            if prime_value % divisor == 0:
                is_prime = False
            else:
                divisor += 2

    return prime_value


class HashTable:
    class HashEntry:
        def __init__(self, key: str = "", value: object = None):
            self.key = key
            self.value = value
            self.state = 0          # 0 = Never used, 1 = Currently used, -1 = Previously used

    def __init__(self, size: int = 31):
        self.size = size
        self.actual_size = next_prime(self.size)
        self.hash_array = np.full(self.actual_size, fill_value=None, dtype=object)
        for i in range(self.actual_size):
            self.hash_array[i] = self.HashEntry(value=i)

    def put(self, key):
        hash_index = self.hash(str(key))
        original_index = hash_index
        stop = False

        while not stop:
            hash_entry_key = self.hash_array[hash_index].key

            if hash_entry_key != "":
                hash_index = (hash_index + 1) % self.hash_array.size
                if hash_index == original_index:
                    stop = True
            elif hash_entry_key == key:
                raise ValueError("key already in use")
            else:
                self.hash_array[hash_index].key = key
                self.hash_array[hash_index].state = 1
                stop = True

    def get(self, key):
        hash_index = self.hash(str(key))
        original_index = hash_index
        found = False
        stop = False

        while not found and not stop:
            if self.hash_array[hash_index].state == 0:
                stop = True
            elif self.hash_array[hash_index].key == key:
                found = True
            else:
                hash_index = (hash_index + 1) % self.hash_array.size
                if hash_index == original_index:
                    stop = True

        if not found:
            raise Exception("Not found")

        return self.hash_array[hash_index].value

    def remove(self):
        pass

    def has_key(self):
        pass

    def find(self):
        pass

    def display(self):
        for i in range(self.hash_array.size):
            hash_entry = self.hash_array[i]
            print(f"Key: {hash_entry.key} Value: {hash_entry.value}")

    @staticmethod
    def hash(key: str):
        hash_index = 0

        for i in range(len(key)):
            hash_index = (31 * hash_index) + ord(key[i])

        return hash_index % 31
