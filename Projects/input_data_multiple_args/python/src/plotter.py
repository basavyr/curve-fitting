import matplotlib.pyplot as plt


def plotter(data):
    x_data_1, x_data_2 = data[0]
    y_data_exp_1, y_data_exp_2 = data[1]

    plt.style.use('science')

    fig, ax = plt.subplots()

    plt.plot(x_data_1, y_data_exp_1, 'ok', markersize=2, label='exp.')
    plt.plot(x_data_2, y_data_th_2, '-b', linewidth=2, label='th.')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('fit_results.pdf', dpi=300, bbox_inches='tight')
    plt.close()


def simple_plotter(data):
    x_data = data[0]
    y_data_exp = data[1]
    y_data_th = data[2]

    plt.style.use('science')

    fig, ax = plt.subplots()

    plt.plot(x_data, y_data_exp, 'ok', markersize=3, label='exp.')
    plt.plot(x_data, y_data_th, '-r', linewidth=1, label='th.')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('fit_results.pdf', dpi=300, bbox_inches='tight')
    plt.close()
