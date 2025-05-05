#
# Hash table implementation for COMP1002 practical 7
#


import numpy as np
from pandas.core.util.hashing import hash_array


def next_prime(start_value: int):
    if start_value % 2 == 0:
        prime_value = start_value - 1
    else:
        prime_value = start_value

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
            self.used = 0

    def __init__(self, size: int):
        self.size = size
        self.actual_size = next_prime(self.size)
        self.hash_array = np.full(self.actual_size, fill_value=None, dtype=object)
        for i in range(self.actual_size):
            self.hash_array[i] = self.HashEntry(value=i)

    def get(self, key: str):
        hash_index = self.strange_hash(key)
        original_index = hash_index
        found = False
        stop = False

        while not found and not stop:
            if self.hash_array[hash_index] == 0 and not stop:
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

    @staticmethod
    def strange_hash(key: str):
        hash_index = 0

        for i in range(len(key)):
            hash_index = (31 * hash_index) + ord(key[i])

        return hash_index % 31

