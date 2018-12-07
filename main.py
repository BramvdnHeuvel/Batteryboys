from classes.map import Map
import matplotlib.pyplot as plt

from algorithms.differential_evolution import evolve_victor
from algorithms.first_fit_houses import first_fit_houses
from algorithms.first_fit_batteries import first_fit_batteries
from algorithms.genetic_race import find_raced_fit
from algorithms.hillclimber import hillclimber
import random

moneys = []
for i in range(1000):

    grid = Map(1)
    grid.execute(first_fit_houses)
    grid.start()
    moneys.append(grid.moneyspent)
# grid.execute(hillclimber)

plt.plot(range(len(moneys)),moneys,'r-')
plt.show()
# grid.visualize()