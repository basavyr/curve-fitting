from matplotlib import pyplot as plt


def plot_data(data):
    x_data = data[0]
    y_data_exp = data[1]
    y_data_th = data[2]

    fig, ax = plt.subplots()

    # set the theme to a scientific aspect
    try:
        plt.style.use('science')
    except Exception as issue:
        print(f'cannot set the theme to scientific -> {issue}')
    else:
        pass

    plt.plot(x_data, y_data_exp, 'ok', markersize=2, label='exp')
    plt.plot(x_data, y_data_th, '-r', linewidth=2, label='th.')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(loc='best')
    plt.savefig('plot_comparison.pdf', dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.close()
