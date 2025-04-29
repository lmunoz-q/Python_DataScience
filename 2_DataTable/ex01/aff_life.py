import matplotlib.pyplot as plt
from load_csv import load


def main():
    path =  "../ressources/life_expectancy_years.csv"
    df = load(path)
    var_country = "France"
    df_country = df.loc[df['country'] == var_country]
    years = df.columns[1:]
    int_years = []
    for i in years:
        int_years.append(int(i))
    life_expectancy = df_country.values[0][1:]
    plt.plot(int_years, life_expectancy)
    plt.title(f"{var_country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    plt.show()



if __name__ == "__main__":
    main()
