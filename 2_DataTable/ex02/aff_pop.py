from load_csv import load
import matplotlib.pyplot as plt


def latoi(index) -> list:
    """
    Convet a list of numbers given as strings into integers.

    Parameters
    ----------
    index : list
        List of numbers as strings.

    Returns
    -------
    list
        List of numbers as integers.
    """
    to_int = []
    for i in index:
        to_int.append(int(i))
    return to_int


def latof(index) -> list:
    """
    Comvert a list of numbers given as strings into floats, scaling 'M' as
    millions and 'k' as thousands.

    Parameters
    ----------
    index : list
        List of numbers as strings.

    Returns
    -------
    list
        List of numbers as floats.
    """

    to_float = []
    for i in index:
        if "M" in i:
            i = float(i.replace("M", ""))
            to_float.append(i * 1_000_000)
        elif "k" in i:
            i = float(i.replace("k", ""))
            to_float.append(i * 1_000)
    return to_float


def main():
    path = "../ressources/population_total.csv"
    df = load(path)
    my_country = "France"
    other_country = "Belgium"
    xmin = 1800
    xmax = 2050
    df_mcountry = df.loc[df['country'] == my_country]
    df_ocountry = df.loc[df['country'] == other_country]
    int_years = latoi(df.columns[1:])
    mpopulation = latof(df_mcountry.values[0][1:])
    opopulation = latof(df_ocountry.values[0][1:])
    plt.plot(int_years, mpopulation, label=my_country)
    plt.plot(int_years, opopulation, label=other_country)
    plt.xlim(xmin, xmax)
    plt.yticks([20_000_000, 40_000_000, 60_000_000], ["20M", "40M", "60M"])
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
