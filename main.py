from classes.map import Map
from algorithms.differential_evolution import evolve_victor
from algorithms.first_fit_houses import first_fit_houses
from algorithms.first_fit_batteries import first_fit_batteries
import random

grid = Map(3)
grid.execute(evolve_victor)
grid.start()
grid.visualize()