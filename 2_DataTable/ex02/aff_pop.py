from load_csv import load
import matplotlib.pyplot as plt


def main():
    path = "../ressources/population_total.csv"
    df = load(path)
    my_country = "France"
    other_country = "Belgium"
    xmin = 1800
    xmax = 2050
    df_mcountry = df.loc[df['country'] == my_country]
    df_ocountry = df.loc[df['country'] == other_country]
    years = df.columns[1:]
    int_years = []
    for i in years:
        int_years.append(int(i))
    mpopulation = df_mcountry.values[0][1:]
    opopulation = df_ocountry.values[0][1:]
    plt.plot(int_years, mpopulation, label=my_country)
    plt.plot(int_years, opopulation, label=other_country)
    plt.xlim(xmin, xmax)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
