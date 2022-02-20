from matplotlib import pyplot as plt


def plot_data(data):
    y_data_exp = data[1]
    x_data = [idx for idx in range(len(y_data_exp))]
    y_data_th = data[2]
    
    # set the theme to a scientific aspect
    # https://github.com/garrettj403/SciencePlots
    try:
        # plt.style.use(['science','ieee'])
        plt.style.use(['science','ieee'])
        plt.style.use('science')
    except Exception as issue:
        print(f'cannot set the theme to scientific -> {issue}')
    else:
        pass

    fig, ax = plt.subplots()


    plt.plot(x_data, y_data_exp, 'ok', markersize=2, label='exp')
    plt.plot(x_data, y_data_th, '-r', linewidth=2, label='th.')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(loc='best',fontsize=12)
    plt.savefig('plot_comparison.pdf', dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.close()
