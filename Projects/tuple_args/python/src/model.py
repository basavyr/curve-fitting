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
    f2 = np.round(spins + even_phonons)

    return f, f2


def generate_x_data(size):
    spins = [idx for idx in range(0, 2 * size, 2)]
    even_phonons = [rd.choice([0, 1]) for _ in range(len(spins))]
    odd_phonons = [0 if x == 1 else 1 for x in even_phonons]
    constants = [rd.randint(1, 10) for _ in range(len(spins))]

    # tupled_items = (spins, even_phonons, odd_phonons, constants)
    tupled_items = np.array([spins, even_phonons, odd_phonons, constants])

    return tupled_items


def main():
    X = generate_x_data(8)

    test_params = [0.3, 1, 2, 3, 4]

    print(model_function(
        X, test_params[0], test_params[1], test_params[2], test_params[3]))


if __name__ == '__main__':
    main()
