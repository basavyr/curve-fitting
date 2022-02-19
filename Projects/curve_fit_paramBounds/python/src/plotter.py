from matplotlib import pyplot as plt
import numpy as np

import model


def comparisonPlot(param_set1, param_set2):
    x_data = np.arange(-model.Bounds.XLIM,
                       model.Bounds.XLIM, model.Bounds.STEP)

    p11, p12, p13 = param_set1
    p21, p22, p23 = param_set2

    y_data_1 = [model.model_function(x, p11, p12, p13) for x in x_data]
    y_data_2 = [model.model_function(x, p21, p22, p23) for x in x_data]

    plt.plot(x_data, y_data_1, 'ok', markersize=3, label='exp.')
    plt.plot(x_data, y_data_2, '-r', linewidth=1.5, label='th.')
    plt.legend(loc='best')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.tight_layout()
    plt.savefig('plot_comparison.pdf', dpi=300, bbox_inches='tight')
    plt.close()


def main():
    param_set1 = [1, 2, 3]
    param_set2 = [1.1, 2.2, 3.3]
    comparisonPlot(param_set1, param_set2)


if __name__ == '__main__':
    main()
