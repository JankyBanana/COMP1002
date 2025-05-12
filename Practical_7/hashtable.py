#
# Implementation of the hash table data structure for COMP1002 practical 7
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


class DSAHashTable:

class DSAHashEntry:
