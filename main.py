from classes.map import Map
import matplotlib.pyplot as plt

from algorithms.differential_evolution import evolve_victor
from algorithms.first_fit_houses import first_fit_houses
from algorithms.first_fit_batteries import first_fit_batteries
from algorithms.genetic_race import find_raced_fit
from algorithms.hillclimber import hillclimber
import random

from algorithms.differential_evolution import DEGeneration

first_generation = []

while len(first_generation) < 4:
    try:
        grid = Map(1)
        grid.execute(first_fit_batteries)
        grid.execute(hillclimber)
        grid.start()
        print(f"Before: {grid.moneyspent}\tAfter: {grid.refresh_cost()}")

        if [house.id for house in grid.houses if house.connected == None] == []:
            print(f"Found a child that costs {grid.moneyspent}!")
            first_generation.append(grid.get_list())
    except AttributeError:
        print("Failed attempt.")

grid = Map(1)
generation = DEGeneration(grid.houses, grid.batteries, first_generation, mutation=0.03)
print(generation.find_best_one())
scores = []

for i in range(100000):
    generation = next(generation)
    if (i + 1) % 100 == 0:
        print(f"Reached generation {i+1}!")
    scores.append(-1*generation.find_best_one()[1][2])

import matplotlib.pyplot as plt

print(generation.find_best_one())
plt.plot(scores)
plt.show()