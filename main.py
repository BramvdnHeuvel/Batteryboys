from classes.map import Map
from algorithms.genetic_race import find_raced_fit
import random

grid = Map(1)
grid.execute(find_raced_fit)
grid.start()