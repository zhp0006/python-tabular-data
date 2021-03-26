#! /usr/bin/ env python3

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def get_all_species():
    species_list = dataframe.species.alltypes()
    return species_list
def get_regression_plot():
    """ make scatterplots of  petal length vs sepal length
    Returns
    -------
    """
    n = 0
    for n in range(0, len(all_species())):
        df = dataframe[dataframe.species == species_list[n]]
        x = df.petal_length_cm
        y = df.sepal_length_cm
        regression = stats.linregress(x,y)
        slope =  regression.slope
        intercept =  regression.slope
        plt.scatter(x,y, label=species_list[n])
        plt.plot(x, slope * x + intercept)
        plt.xlabel("Petal length(cm)")
        plt.ylabel("Sepal length(cm)")
        plt.legend()

        plt.savefig(species_list[n] + ".png")
        plt.close()
        n += 1
if __name__ == '__main__':
    dataframe = pd.read_csv("iris.csv")
    species_list = all_species()
    print("Regression plot for" + all_species)
    get_regression_plot()
