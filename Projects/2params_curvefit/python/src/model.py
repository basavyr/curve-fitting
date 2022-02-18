import numpy as np
import random as rd
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt


def model_function(x, p1, p2):
    """
    - the function that needs to be modeled by the data
    - the param_set is a list of two parameters (p1, p2)
    """
    # p1, p2 = param_set
    try:
        assert p1 >= 0 and p2 >= 0
    except AssertionError as error:
        print(
            f'Cannot compute the model function since the two parameters are invalid -> {param_set}')
        return -1
    else:
        pass
    f = pow(x, 2) * p1 - (pow(p2, 3) + 2)
    return f


def generateTestData(param_set):
    x_0 = 5.0
    shift_quantity = 2.5
    step = 0.1

    p1, p2 = param_set

    x_data = np.arange(-x_0, x_0 + step, step)

    y_data = [model_function(x, p1, p2) for x in x_data]
    y_data_shifted = [model_function(
        x, p1, p2) + rd.uniform(-shift_quantity, shift_quantity) for x in x_data]

    data = [[round(x[0], 4), round(x[1], 4), round(x[2], 4)]
            for x in zip(x_data, y_data, y_data_shifted)]

    with open('data.dat', 'w+') as f:
        for data_element in data:
            f.write(str(data_element[0]) + ' ' +
                    str(data_element[1]) + ' ' + str(data_element[2]))
            f.write('\n')

    return (x_data, y_data, y_data_shifted)


def find_fit(data, initial_guess):
    x_data = data[0]
    y_data_th = data[2]
    if(initial_guess == -1):
        fittedParameters, pcov = curve_fit(model_function, xdata=x_data,
                                           ydata=y_data_th)
    else:
        fittedParameters, pcov = curve_fit(model_function, xdata=x_data,
                                           ydata=y_data_th, p0=initial_guess)

    return fittedParameters


def plotFitResults(data, model_params, curve_fit_params):
    """
    - create a plot comparison between the data evaluated with the initial set of parameters and the parameters obtained via the curve fit
    """

    x_data = data[0]

    p1_exp, p2_exp = model_params
    y_data_exp = [model_function(x, p1_exp, p2_exp) for x in x_data]

    p1_th, p2_th = curve_fit_params
    y_data_th = [model_function(x, p1_th, p2_th) for x in x_data]

    plt.plot(x_data, y_data_exp, 'ok', label='exp.')
    plt.plot(x_data, y_data_th, '-r', label='th.')
    plt.legend(loc='best')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.tight_layout()
    plt.savefig('curve_fit_plot.pdf', dpi=300, bbox_inches='tight')
    plt.close()


def main():
    test_param_set = [2.2, 2.5]
    initial_guess = [1, 3]
    data = generateTestData(test_param_set)
    cvf1 = find_fit(data, -1)
    cvf2 = find_fit(data, initial_guess)
    print(
        f'results for the fit without initial guess -> {cvf1}\nThe actual model parameters -> {test_param_set}')
    print(
        f'results for the fit WITH initial guess -> {cvf2}\nThe actual model parameters -> {test_param_set}')
    plotFitResults(data, test_param_set, cvf1)


if __name__ == '__main__':
    main()
