import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def remove_nan(list_a, list_b) -> list:
    """
    Remove all entries with missing (NaN) values from two aligned lists.

    Parameters
    ----------
    list_a : list or pandas.Series
        First list of values (e.g., income).
    list_b : list or pandas.Series
        Second list of values (e.g., life expectancy).

    Returns
    -------
    pandas.DataFrame
        Cleaned DataFrame with two columns 'x' and 'y', containing only valid
        pairs.
    """
    df = pd.DataFrame({
        "x": list_a,
        "y": list_b
    })
    df = df.dropna()
    return df


def main():
    year = "1900"
    df_life = load("../ressources/life_expectancy_years.csv")
    df_product = load(
        "../ressources/"
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    df_clean = remove_nan(df_product[year], df_life[year])
    x = df_clean["x"]
    y = df_clean["y"]
    plt.scatter(x, y)
    plt.title(year)
    plt.ylabel("Life Expectancy")
    plt.xlabel("Gross domestic product")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()


if __name__ == "__main__":
    main()
