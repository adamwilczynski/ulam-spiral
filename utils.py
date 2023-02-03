from abc import ABC, abstractmethod
import itertools
import itertools

import PIL.Image
import numpy as np

from PIL import Image

MAX_SIZE = 10_000
FILE_NAME = "is_prime_array.npy"


class ColorMap(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class PrimeColorMap(ColorMap):
    @staticmethod
    def sieve_of_eratosthenes_from_zero_to(n: int):
        sieve = np.ones(n + 1, dtype=bool)
        sieve[0], sieve[1] = False, False
        for i, is_prime in enumerate(sieve):
            if is_prime:
                for j in range(i + i, sieve.size, i):
                    sieve[j] = False
        return sieve

    def __init__(self, composite_color, prime_color):
        with open(FILE_NAME, "rb") as f:
            self.prime_check = np.load(f)

        self.composite_color = composite_color
        self.prime_color = prime_color

    def __call__(self, n: int):
        if self.prime_check[n]:
            return self.prime_color
        return self.composite_color


class SpiralImage:
    def __init__(self, size: int, color_map: ColorMap):
        if size > MAX_SIZE:
            raise ValueError("Max size exceeded.")
        if size % 2 == 0:
            raise ValueError("Must be odd, so that 1 stays in the middle.")

        self.size = size
        self.color_map = color_map

    def get_spiral_indices(self):
        right = np.array((0, 1))
        up = np.array((-1, 0))
        left = np.array((0, -1))
        down = np.array((1, 0))

        current_number = 1

        distance = 0
        center = self.size // 2
        current_index = np.array([center, center])
        indices_n = self.size * self.size
        for direction, increase_distance in itertools.cycle(((right, True), (up, False), (left, True), (down, False))):
            if current_number >= indices_n:
                break
            if increase_distance:
                distance += 1
            for _ in range(distance):
                yield current_index.copy()
                current_number += 1
                current_index += direction

    def get_spiral_image(self):
        spiral = np.zeros((self.size, self.size, 3), dtype=np.uint8)
        for n, index in enumerate(self.get_spiral_indices(), start=1):
            spiral[*index] = self.color_map(n)
        return Image.fromarray(spiral, mode="RGB")

# with open(FILE_NAME, "wb") as f:
#     np.save(f, PrimeColorMap.sieve_of_eratosthenes_from_zero_to(MAX_SIZE * MAX_SIZE))
