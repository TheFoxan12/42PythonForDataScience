from matplotlib import pyplot as plt
from load_csv import load


def main():
    """displays the country information about life expectancy of France"""
    data = load("life_expectancy_years.csv")
    if data.empty:
        return
    data.set_index("country", inplace=True)

    data.loc["France"].plot()
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == '__main__':
    main()
