import matplotlib.pyplot as plt
from load_csv import load


def main():
    path =  "../ressources/life_expectancy_years.csv"
    df = load(path)
    country = df.loc[df['country'] == "France"]
    years = df.columns[1:]
    life_expectancy = country.values[0][1:]
    plt.plot(years, life_expectancy)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Years")
    plt.ylabel("Life expectancy")

    plt.show()



if __name__ == "__main__":
    main()
