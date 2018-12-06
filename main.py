from classes.map import Map
from algorithms.differential_evolution import evolve_victor
from algorithms.first_fit_houses import first_fit_houses
from algorithms.first_fit_batteries import first_fit_batteries
from algorithms.genetic_race import find_raced_fit
from algorithms.hillclimber import hillclimber
import random

grid = Map(3)
for i in range(100):
    grid.execute(first_fit_batteries)
# grid.execute(hillclimber)
grid.start()
# grid.visualize()