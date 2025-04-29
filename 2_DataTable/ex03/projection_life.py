import matplotlib.pyplot as plt
from load_csv import load


def main():
    year = "1900"
    df_life = load("../ressources/life_expectancy_years.csv")
    df_product = load("../ressources/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_country = df_life[year]
    df_product = df_product[year]

    plt.scatter(df_product, df_country)
    plt.show()

if __name__ == "__main__":
    main()
