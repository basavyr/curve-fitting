from matplotlib import pyplot as plt


def plot_function(x_data, y_data):
    fig, ax = plt.subplots()

    plt.style.use('science')

    plt.plot(x_data, y_data, '-ro', linewidth=2, markersize=3, label='data')
    plt.legend(loc='best')
    plt.savefig('data.pdf', dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.close()
