from matplotlib import pyplot as plt

import model


def plot_data(data):
    x_data, y_data_th, y_data_exp = data

    plt.plot(x_data, y_data_th, '-r', linewidth=2, label='th')
    plt.plot(x_data, y_data_exp, 'ok', label='exp')
    plt.legend(loc='best')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.savefig('plot.pdf', dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.close()


def main():
    test_param_set = [2.2, 2.5]


if __name__ == '__main__':
    main()
