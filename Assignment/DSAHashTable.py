#
# Implementation of a hash table data structure using linear probing
# for Assignment module 2
#
# Based on hashtable.py from the practical 7 submission
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
        self.ID = None
        self.Name = None
        self.Address = None
        self.Priority = None
        self.Status = None
        self.state = 0  # 0 = Never used, 1 = Currently used, -1 = Previously used

    def __str__(self):
        return self._get()

    def _put(self, id, name, address, priority, status):
        self.ID = id
        self.Name = name
        self.Address = address
        self.Priority = priority
        self.Status = status
        self.state = 1

    def _get(self):
        return (f"ID: {self.ID}  Name: {self.Name}  Address: {self.Address}  "
                f"Priority: {self.Priority}  Status: {self.Status}")

    def _remove(self):
        self.ID = ''
        self.Name = ''
        self.Address = ''
        self.Priority = -1
        self.Status = ''
        self.state = -1


class DSAHashTable:
    def __init__(self, init_size: int = 31):
        self.init_size = init_size
        self.actual_size = next_prime(init_size)
        self.hash_array = np.full(shape=self.actual_size, fill_value=None, dtype=object)
        for i in range(self.actual_size):
            self.hash_array[i] = DSAHashEntry()

        self.num_elements = 0

    def put(self, id, name, address, priority, status):
        hash_index = self.hash(id)
        original_index = hash_index
        hash_found = False

        while not hash_found:
            hash_entry = self.hash_array[hash_index]

            if hash_entry.state == 0 or hash_entry.state == -1:
                self.num_elements += 1
                self.hash_array[hash_index]._put(id, name, address, priority, status)
                hash_found = True

            elif hash_entry.state == 1 and hash_entry.ID == id:
                self.hash_array[hash_index]._put(id, name, address, priority, status)

            else:
                hash_index = (hash_index + 1) % self.actual_size
                if hash_index == original_index:
                    raise RuntimeError("Hashtable full or key not found.")

        lf = self.load_factor()
        if lf < 0.3 or lf > 0.7:
            self.resize()

    def remove(self, id: int):
        hash_idx = self.hash(id)
        original_idx = hash_idx
        found = False
        stop = False

        while not found and not stop:
            if self.hash_array[hash_idx].state == 0:
                stop = True
            elif self.hash_array[hash_idx].ID == id:
                found = True
            else:
                hash_idx = (hash_idx + 1) % self.actual_size

                if hash_idx == original_idx:
                    stop = True

        if not found:
            return None

        return self.hash_array[hash_idx]._remove()

    def get(self, id: int):
        hash_idx = self.hash(id)
        original_idx = hash_idx
        found = False
        stop = False

        while not found and not stop:
            if self.hash_array[hash_idx].state == 0:
                stop = True
            elif self.hash_array[hash_idx].ID == id:
                found = True
            else:
                hash_idx = (hash_idx + 1) % self.actual_size

                if hash_idx == original_idx:
                    stop = True

        if not found:
            return None

        return self.hash_array[hash_idx]._get()

    def has_id(self, id: int):
        if self.get(id) is not None:
            return True

    def hash(self, id: int):
        hash_index = 0
        hash_string = str(id)

        for i in range(len(hash_string)):
            hash_index += ord(hash_string[i])

        return hash_index % self.actual_size

    def display(self):
        for entry in self.hash_array:
            print(f"ID: {entry.ID}  Name: {entry.Name}  Address: {entry.Address}  "
                f"Priority: {entry.Priority}  Status: {entry.Status}")
        print(f'Load factor: {self.load_factor()}\n')

    def load_factor(self):
        return self.num_elements / self.actual_size

    def resize(self):
        lf = self.load_factor()

        if lf > 0.7:
            new_size = int(self.actual_size * 1.5)
            new_actual_size = next_prime(new_size)
        elif lf < 0.3:
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
                id = old_array[i].ID
                name = old_array[i].Name
                address = old_array[i].Address
                priority = old_array[i].Priority
                status = old_array[i].Status

                hash_index = self.hash(id)
                original_index = hash_index
                hash_found = False

                while not hash_found:
                    hash_entry = self.hash_array[hash_index]

                    if hash_entry.state == 0 or hash_entry.state == -1:
                        self.hash_array[hash_index]._put(id, name, address, priority, status)
                        hash_found = True

                    elif hash_entry.state == 1 and hash_entry.ID == id:
                        self.hash_array[hash_index]._put(id, name, address, priority, status)

                    else:
                        hash_index = (hash_index + 1) % self.actual_size
                        if hash_index == original_index:
                            raise RuntimeError("Hashtable full or key not found.")

                if self.hash_array[hash_index].state != 1:
                    self.num_elements += 1
