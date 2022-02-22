import numpy as np

from scipy.optimize import curve_fit
import random as rd

import plotter


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

    tupled_items = np.array([spins, even_phonons, odd_phonons, constants])

    return tupled_items


def main():
    X = generate_x_data(20)

    test_params = [0.3, 1, 2, 3, 4]

    MF = model_function(
        X, test_params[0], test_params[1], test_params[2], test_params[3])

    plotter.plot_function(X[0], MF)


if __name__ == '__main__':
    main()
