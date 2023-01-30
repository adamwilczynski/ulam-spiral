import itertools
from itertools import cycle

import numpy as np

from PIL import Image


def sieve_of_eratosthenes_from_zero_to(n: int):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0], sieve[1] = False, False
    for i, is_prime in enumerate(sieve):
        if is_prime:
            for j in range(i + i, sieve.size, i):
                sieve[j] = False
    return sieve


sieve_result = sieve_of_eratosthenes_from_zero_to(10)

RIGHT = np.array((0, 1))
UP = np.array((-1, 0))
LEFT = np.array((0, -1))
DOWN = np.array((1, 0))


def create_ulam_spiral(size):
    if size % 2 == 0:
        raise ValueError("Must be odd, so that 1 stays in the middle.")

    # spiral = np.zeros((size, size))
    current_number = 1

    n_moves = 0
    center = size // 2
    current_index = np.array([center, center])
    for i, direction in enumerate(itertools.cycle((RIGHT, UP, LEFT, DOWN))):
        if current_number >= size * size:
            break
        if i % 2 == 0:
            n_moves += 1
        for _ in range(n_moves):
            yield current_index.copy()
            # spiral[*current_index] = current_number
            current_number += 1
            current_index += direction
    # return spiral


# Image.fromarray(sieve_result)

print(sieve_result, sieve_result.size * sieve_result.itemsize)
print(create_ulam_spiral(5))

print(list(create_ulam_spiral(5)))
