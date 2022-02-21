import numpy as np

from scipy.optimize import curve_fit
import random as rd


def model_function(X, a, b, c, d):
    """
    - X is a tuple of arrays 
    """
    spins, even_phonons, odd_phonons, constants = X

    f = a * (pow(spins, 5)) * (even_phonons + 0.5) + \
        b * (pow(spins, 3)) * (odd_phonons + 0.5) + c * d * spins * constants

    return f


def generate_x_data(size):
    spins = [idx for idx in range(0, 2 * size, 2)]
    even_phonons = [rd.choice([0, 1]) for _ in range(len(spins))]
    odd_phonons = [0 if x == 1 else 1 for x in even_phonons]
    constants = [rd.randint(1, 10) for _ in range(len(spins))]

    tupled_items = (spins, even_phonons, odd_phonons, constants)

    return tupled_items


def main():
    print(generate_x_data(8))


if __name__ == '__main__':
    main()
