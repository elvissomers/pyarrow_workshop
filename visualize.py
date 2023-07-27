import matplotlib.pyplot as plt

def bar_plot_first_10(data, variable):
    df = data.to_pandas().head(10)
    df.plot(kind='bar', x='neighbourhood', y=variable+"_mean", legend=False)

    plt.xlabel('Neighbourhood')
    plt.ylabel(variable)
    plt.title(variable + ' for the best 10 neighbourhoods')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig('bar_plot_' + variable + '.png')