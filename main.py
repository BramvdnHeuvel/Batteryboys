from classes.map import Map
from algorithms.differential_evolution import evolve_victor
import random

grid = Map(1)
grid.execute(evolve_victor)
grid.start()