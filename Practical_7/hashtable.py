#
# Implementation of the hash table values structure for COMP1002 practical 7
#


import numpy as np


def next_prime(start_value):
    start_value = int(start_value)

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


class DSAHashEntry:
    def __init__(self):
        self.key: str = None
        self.data: object = None
        self.state = 0  # 0 = Never used, 1 = Currently used, -1 = Previously used

    def _put(self, key: str, data: object):
        self.key = key
        self.data = data
        self.state = 1

    def _get(self):
        return self.data

    def _remove(self):
        self.key = None
        self.data = None
        self.state = -1


class DSAHashTable:
    def __init__(self, init_size: int = 31):
        self.init_size = init_size
        self.actual_size = next_prime(init_size)
        self.hash_array = np.full(shape=self.actual_size, fill_value=None, dtype=object)
        for i in range(self.actual_size):
            self.hash_array[i] = DSAHashEntry()
        self.num_elements = 0

    def put(self, key: str, data: object):
        hash_index = self._find(key)

        if self.hash_array[hash_index].state != 1:
            self.num_elements += 1

        self.hash_array[hash_index]._put(key, data)
        lf = self.load_factor()

        if lf > 0.7 or lf < 0.4:
            self.resize()

    def get(self, key: str):
        hash_index = self._find(key)
        if self.hash_array[hash_index].state != 1:
            raise KeyError(f"Key '{key}' not found")
        return self.hash_array[hash_index]._get()

    def remove(self, key: str):
        hash_index = self._find(key)
        if self.hash_array[hash_index].state == 1:
            self.num_elements -= 1
            self.hash_array[hash_index]._remove()

        lf = self.load_factor()
        if lf > 0.7 or lf < 0.4:
            self.resize()

    def has_key(self, key: str):
        try:
            hash_index = self._find(key)
            return self.hash_array[hash_index].state == 1
        except:
            return False

    def hash(self, key: str):
        hash_index = 0

        for i in range(len(key)):
            hash_index += ord(key[i])

        return hash_index % self.actual_size

    def step_hash(self, key: str):
        max_step = self.actual_size
        string_ascii = 0

        for i in range(len(key)):
            string_ascii += ord(key[i])

        probe_step = max_step - (string_ascii % max_step)
        return probe_step

    def display(self):
        for i in range(self.hash_array.size):
            hash_entry = self.hash_array[i]
            print(f"Key: {hash_entry.key} Data: {hash_entry.data} Index: {i} State: {hash_entry.state}")
        print(f'Load factor: {self.load_factor()}\n')

    def load_factor(self):
        return self.num_elements / self.actual_size

    def resize(self):
        lf = self.load_factor()

        if lf > 0.7:
            new_size = int(self.actual_size * 1.5)
            new_actual_size = next_prime(new_size)
        elif lf < 0.4:
            new_size = int(self.actual_size / 1.5)
            new_actual_size = next_prime(new_size)
        else:
            return

        old_array = self.hash_array
        old_size = self.actual_size

        self.actual_size = new_actual_size
        self.hash_array = np.full(shape=self.actual_size, fill_value=None, dtype=object)
        for i in range(self.actual_size):
            self.hash_array[i] = DSAHashEntry()

        for i in range(old_size):
            if old_array[i].state == 1:
                key = old_array[i].key
                data = old_array[i].data

                hash_index = self.hash(key)
                probe_step = self.step_hash(key)
                original_index = hash_index

                while self.hash_array[hash_index].state == 1:
                    hash_index = (hash_index + probe_step) % self.actual_size

                self.hash_array[hash_index]._put(key, data)

    def _find(self, key: str):
        hash_index = self.hash(key)
        probe_step = self.step_hash(key)
        original_index = hash_index

        while True:
            hash_entry = self.hash_array[hash_index]

            if hash_entry.state == 0:
                return hash_index
            elif hash_entry.state == 1 and hash_entry.key == key:
                return hash_index
            else:
                hash_index = (hash_index + probe_step) % self.actual_size
                if hash_index == original_index:
                    raise RuntimeError("Hashtable full or key not found.")
