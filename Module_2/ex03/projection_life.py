from matplotlib import pyplot as plt
from load_csv import load


def main():
    """projects the life expectancy as a function of GDP for every country,
in the year 1900"""
    data_year = load("life_expectancy_years.csv")
    if data_year.empty:
        return
    data_year.set_index("country", inplace=True)

    data_prod = load("income_per_person_gdppercapita_"
                     "ppp_inflation_adjusted.csv")
    if data_prod.empty:
        return
    data_prod.set_index("country", inplace=True)

    plt.xscale("log")
    for country in data_year.index:
        plt.scatter(data_prod["1900"].loc[country],
                    data_year["1900"].loc[country],
                    color='C0')
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()


if __name__ == '__main__':
    main()
