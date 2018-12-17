import matplotlib.pyplot as plt
import sys
from classes.map import Map
from algorithms.differential_evolution import evolve_victor
from algorithms.first_fit_houses import first_fit_houses
from algorithms.first_fit_batteries import first_fit_batteries
from algorithms.genetic_race import find_raced_fit
from algorithms.hillclimber import hillclimber
from algorithms.bounds import first_distance
from algorithms.bounds import highest_distance
import random
from algorithms.differential_evolution import DEGeneration

first_generation = []
use_map = int(input("Which neighbourhood do you want? "))
if use_map > 3 or use_map < 1:
    sys.exit("Please choose a map from 1 to 3")
     
algorithm_func = {'hill': hillclimber, 'diff': evolve_victor, 'ffb': first_fit_batteries, 'ffh': first_fit_houses, 'gn': find_raced_fit}
algorithm = input("Which algorithm do you want to use? ")
if algorithm.lower() in algorithm_func:
    print("Let's go")
else:
    sys.exit("\nPlease use a good algorithm.\n\nFor hillclimber, choose \tHILL.\nFor differential, choose \tDIFF.\nFor first fit, choose   \tFFB or FFH. \nFor genetic race, choose     \tGN")

while len(first_generation) < 4:
    try:
        grid = Map(use_map)
        grid.execute(algorithm_func[algorithm.lower()])
        grid.start()

        if [house.id for house in grid.houses if house.connected is None] == []:
            print(f"Found a child that costs {grid.moneyspent}!")
            first_generation.append(grid.get_list())
        else:
            print("Found an insufficient child.")
      
    except AttributeError:
        print("Failed attempt.")

grid = Map(use_map)
generation = DEGeneration(grid.houses, grid.batteries, first_generation, mutation=0.03)
print(generation.find_best_one())
scores = []

for i in range(1000):
    generation = next(generation)
    if (i + 1) % 100 == 0:
        print(f"Reached generation {i+1}!")
    scores.append(-1*generation.find_best_one()[1][2])

print(generation.find_best_one())
plt.plot(scores)
plt.show()
grid.visualize()
