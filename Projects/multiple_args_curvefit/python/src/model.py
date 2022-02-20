import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import random as rd

import plotter


def model_function(X, a, b, c):
    """
    - the analytical expression for the model that aims at describing the experimental data
    - the X argument is an array of tuples of the form X=[,...,(xi_1,xi_2),...]
    """
    nw1, nw2, I = X

    f = a * pow(I, 2) * (nw1 + 0.5) + b * I * (nw2 + 0.5) + c
    return f


def generate_x_data(size):

    spin = lambda x: (2 * x) + 0.5
    phonon = lambda: rd.choice([0, 1, 2])

    x_data = [(phonon(), phonon(), spin(idx)) for idx in range(size)]
    return x_data


def generate_data_from_params(params):
    x_data = generate_x_data(10)
    p1, p2, p3 = params

    y_data_exp = [model_function(x, p1, p2, p3) for x in x_data]

    print(y_data_exp)


def main():
    x_data = generate_x_data(10)
    test_params = [3, 4, 0]
    # generate_data_from_params(test_params)
    # u = lambda x: (2 * x) + 0.5 if x % 2 == 0 else (2 * x) - 0.5
    w = generate_x_data(10)
    print(w)


if __name__ == '__main__':
    main()
