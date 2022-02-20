import random as rd

import operator

import numpy as np

from scipy.optimize import curve_fit


def generate_x_data(size, phonon1, phonon2, even_state):
    phonon = lambda: rd.choice([0, 1])

    if(even_state == 1):
        s0 = 2.5
    else:
        s0 = 3.5

    x_data = [(s0 + 2 * k, phonon1, phonon2) for k in range(size)]

    return x_data


def create_experimental_data(size):
    even_data = 'band1.dat'
    odd_data = 'band2.dat'

    even_spins = generate_x_data(size, 0, 0, 1)  # zero phonon states
    odd_spins = generate_x_data(size, 1, 0, 0)  # one-phonon wobbling states

    with open(even_data, 'w+') as f:
        for I_even in even_spins:
            f.write(str(I_even[0]) + ' ' +
                    str(I_even[1]) + ' ' + str(I_even[2]))
            f.write('\n')

    with open(odd_data, 'w+') as f:
        for I_odd in odd_spins:
            f.write(str(I_odd[0]) + ' ' +
                    str(I_odd[1]) + ' ' + str(I_odd[2]))
            f.write('\n')

    return [even_spins, odd_spins]


def model_function(X, a, b, c):
    spin, phonon1, phonon2 = X

    f = a * pow(spin, 3) * (phonon1 + 0.5) + b * \
        pow(spin, 2) * (phonon2 + 0.5) + c * spin

    return f


def generate_spin_bands(size, params):
    even_spins, odd_spins = create_experimental_data(size)
    band1 = [w for w in even_spins]
    band2 = [w for w in odd_spins]

    p1, p2, p3 = params

    model_band_1 = [model_function(x, p1, p2, p3) for x in band1]
    model_band_2 = [model_function(x, p1, p2, p3) for x in band2]

    model_data = model_band_1 + model_band_2

    bands = band1 + band2
    bands.sort(key=operator.itemgetter(0))

    return bands


def generate_model_data(x_data, params):
    p1, p2, p3 = params
    y_data = [model_function(X, p1, p2, p3) for X in x_data]

    return y_data


def fit_model(model_function, data):
    x_data, y_data = data

    fitted_params, _ = curve_fit(model_function, x_data, y_data)

    return fitted_params


def main():
    test_params = [0.02, 0.3, 1]

    spin_data = generate_spin_bands(15, test_params)
    model_data = generate_model_data(spin_data, test_params)

    tupled_data = ([x[0] for x in spin_data], [x[1]
                                               for x in spin_data], [x[2] for x in spin_data])

    data = [tupled_data, model_data]

    P = fit_model(model_function, data)

    print(P)


if __name__ == '__main__':
    main()
