#
# Hash table implementation for COMP1002 practical 7
#


import numpy as np


def next_prime(start_value):
    start_value = int(start_value)+1
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
        def __init__(self, key: str = None, value: object = None):
            self.key = key
            self.value = value
            self.state = 0  # 0 = Never used, 1 = Currently used, -1 = Previously used

        def _remove(self):
            self.key = None
            self.value = None
            self.state = -1

    def __init__(self, size: int = 31):
        self.size = size
        self.initial_size = next_prime(self.size)
        self.hash_array = np.full(shape=self.initial_size, fill_value=self.HashEntry(None, None), dtype=object)

    def put(self, key: str, value: object):
        hash_index = self.hash(key)
        original_index = hash_index
        stop = False

        while not stop:
            hash_entry_key = self.hash_array[hash_index].key

            if hash_entry_key != "":
                hash_index = (hash_index + self.step_hash(self.hash(key))) % self.hash_array.size
                if hash_index == original_index:
                    stop = True
            elif self.has_key(key):
                raise ValueError("key already in use")
            else:
                self.hash_array[hash_index].key = key
                self.hash_array[hash_index].value = value
                self.hash_array[hash_index].state = 1
                stop = True

    def get(self, key: str):
        hash_index = self.hash(key)
        original_index = hash_index
        found = False
        stop = False

        while not found and not stop:
            if self.hash_array[hash_index].state == 0:
                stop = True
            elif self.hash_array[hash_index].key == key:
                found = True
            else:
                hash_index = (hash_index + self.step_hash(self.hash(key))) % self.hash_array.size
                if hash_index == original_index:
                    stop = True

        if not found:
            raise Exception("Not found")

        return self.hash_array[hash_index].value

    def remove(self, key: str):
        if not self.has_key(key):
            raise ValueError("key not found")
        else:
            print(f"Removing key {key}\n")
            self.find(key)._remove()

    def has_key(self, key: str):
        for i in range(self.hash_array.size):
            hash_element = self.hash_array[i]

            if hash_element.key == key:
                return True

        return False

    def find(self, key: str):  # Returns the HashElement object with the given key
        for i in range(self.hash_array.size):
            if self.hash_array[i].key == key:
                return self.hash_array[i]

        return None

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

    def step_hash(self, key):
        return self.initial_size - ( key % self.initial_size)

    def elements(self):
        element_count = 0

        for i in range(self.hash_array.size):
            if self.hash_array[i].value is not None:
                element_count += 1

        return element_count

    def load_factor(self):
        return self.elements()/self.hash_array.size

    def resize(self):
        if self.load_factor() > 0.7:
            new_size = next_prime(int(self.hash_array.size * 1.5))
        elif self.load_factor() < 0.4:
            new_size = next_prime(int(self.hash_array.size / 1.5))
        else:
            print("Resize not required")

        new_array = np.full(new_size, fill_value=None, dtype=object)
        for i in range(new_size):
            new_array[i] = self.HashEntry(value=None)

        self.hash_array = new_array