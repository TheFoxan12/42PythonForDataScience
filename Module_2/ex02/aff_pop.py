from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load


def format_with_units(x, pos):
    """function used to format the display of big numbers"""
    if x >= 1e6:
        return f'{x/1e6:.1f}M'
    elif x >= 1e3:
        return f'{x/1e3:.1f}K'
    else:
        return f'{x:.0f}'


def main():
    """displays the comparison between population of France and Belgium"""
    data = load("population_total.csv")
    if data.empty:
        return
    data.set_index("country", inplace=True)

    france_data = (data.loc["France"]
                   .replace({'M': 'e+06', 'K': 'e+03'}, regex=True)
                   .astype(float)
                   .astype(int))
    france_keys = data.loc["France"].index.astype(int)
    plt.plot(france_keys, france_data, label="France")

    belgium_data = (data.loc["Belgium"]
                    .replace({'M': 'e+06', 'K': 'e+03'}, regex=True)
                    .astype(float)
                    .astype(int))
    belgium_keys = data.loc["Belgium"].index.astype(int)
    plt.plot(belgium_keys, belgium_data, label="Belgium")

    plt.xlim(1800, 2050)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_with_units))
    plt.show()


if __name__ == '__main__':
    main()
