import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import random as rd


def model_function(X, a, b):
    """
    - the analytical expression for the model that aims at describing the experimental data
    - the X argument is an array of tuples of the form X=[,...,(xi_1,xi_2),...]
    """
    x = X
    f = a * x[0] + (b - pow(x[1], 2)) * a * b
    return f


def generate_x_data(size):
    x_data = [(rd.randrange(1, 3), rd.randrange(4, 6)) for _ in range(size)]
    return x_data


def main():
    x_data = generate_x_data(10)
    for x in x_data:
        print(model_function(x, 1, 1))


if __name__ == '__main__':
    main()
