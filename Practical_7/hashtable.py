#
# Implementation of the hash table values structure for COMP1002 practical 7
#


def next_prime(start_value):
    start_value = int(start_value) + 1
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


class DSAHashTable:
    def __init__(self, init_size: int = 31):
        self.init_size = init_size

    def put(self):
        pass

    def get(self):
        pass

    def remove(self):
        pass

    def has_key(self):
        pass

    def hash(self):
        pass

    def step_hash(self):
        pass

    def display(self):
        pass

    def load_factor(self):
        pass

    def resize(self):
        pass

    def _find(self):
        pass


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
        self.key: str = None
        self.data: object = None
        self.state = -1