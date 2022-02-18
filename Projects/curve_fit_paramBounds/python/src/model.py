from matplotlib import pyplot
from scipy.optimize import curve_fit

import numpy as np
import random as rd

from timeit import default_timer

import plotter


class Bounds:
    XLIM = 5.0
    STEP = 0.1


def model_function(x, p1, p2, p3):
    try:
        assert p3 != 0
    except AssertionError as err:
        print('the parameters are invalid')
        return -1
    else:
        pass
    f = p1 * pow(x, 5) + p2 / p3 * (pow(x, 3) - p1) + p1 * p2 * p3 * x
    return f


def generateTestData(parameter_set):
    p1, p2, p3 = parameter_set

    x_data = np.arange(-Bounds.XLIM, Bounds.XLIM + Bounds.STEP, Bounds.STEP)
    x_data = [round(x, 3) for x in x_data]
    y_data_exp = [round(model_function(x, p1, p2, p3), 3) for x in x_data]

    with open('data.dat', 'w+') as f:
        for idx in range(len(x_data)):
            f.write(str(x_data[idx]) + ' ' + str(y_data_exp[idx]))
            f.write('\n')

    return (x_data, y_data_exp)


def compareData(exp_params, fit_params):
    """
    - generate a file with the numerical data for
        1. model function evaluated with the initial parameters
        2. model function evaluated with the parameters obtained from the curve fit procedure
    """
    x_data = np.arange(-Bounds.XLIM, Bounds.XLIM+Bounds.STEP, Bounds.STEP)
    x_data = [round(x, 3) for x in x_data]

    p1_exp, p2_exp, p3_exp = exp_params

    p1_fit, p2_fit, p3_fit = fit_params

    y_data_exp = [round(model_function(x, p1_exp, p2_exp, p3_exp), 3)
                  for x in x_data]
    y_data_fit = [round(model_function(x, p1_fit, p2_fit, p3_fit), 3)
                  for x in x_data]

    with open('fit_comparison.dat', 'w+') as f:
        for idx in range(len(x_data)):
            f.write(str(x_data[idx])+' ' +
                    str(y_data_exp[idx])+' '+str(y_data_fit[idx]))
            f.write('\n')

    return (x_data, y_data_exp, y_data_fit)


def main():
    param_set1 = [1, 2, 3]
    param_set2 = [1.1, 2.2, 3.3]
    generateTestData(param_set1)
    compareData(param_set1, param_set2)
    plotter.comparisonPlot(param_set1=param_set1, param_set2=param_set2)


if __name__ == '__main__':
    main()
