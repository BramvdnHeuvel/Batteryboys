import matplotlib.pyplot as plt
import random
import time

import config

def evolve_victor(self, houses, batteries, population=4):
    generation = __create_generation(houses, batteries, population, mutation=0.03)
    best_cost = []

    for i in range(10000):
        next(generation)

        score = generation.find_best_one()[1]

        if score[0] < 150:
            best_cost.append(5300 * config.cost_per_grid_section)
        else:
            best_cost.append(-1*score[2])

        if (i + 1) % 1000 == 0:
            print(f"Generation {i+1} reached!")
    
    plt.plot(range(len(best_cost)),best_cost,'r-')
    plt.show()

    victor = generation.find_best_one()
    scores = victor[1]
    print(f'{victor[0]}\nAantal huizen:\t{scores[0]}\nStroom vrij:\t{-1*scores[1]}\nKosten:\t\t{-1*scores[2]}')
    
# -------------------------------------------------------------------------------------------

def __create_generation(houses, batteries, population=4, mutation=0.03):
    generation_individuals = []

    for i in range(population):
        individual = __create_first_individual(houses, batteries)
        generation_individuals.append(individual)
    
    return DEGeneration(houses, batteries, generation_individuals, mutation)


def __create_first_individual(houses, batteries):
    individual = []

    for i in range(len(houses)):
        connection = random.randint(0, len(batteries)-1)
        individual.append(connection)
    
    return individual


def distance(house, battery):
    return abs(house.x - battery.x) + abs(house.y - battery.y)


class DEGeneration:
    def __init__(self, houses, batteries, generation, mutation):
        self.houses = houses
        self.batteries = batteries
        self.mutation = mutation

        self.generation = generation

    def __next__(self):
        for i in range(len(self.generation)):
            parent = self.generation[i]
            child = self.__create_child(parent)

            self.generation[i] = self.__compare_individuals(parent, child)
        
        return self


    def find_best_one(self):
        victor = self.generation[0]

        for challenger in self.generation:
            victor = self.__compare_individuals(victor, challenger)
        
        return (victor, self.__calculate_score(victor))


    def __create_child(self, parent):
        imitators = random.sample(self.generation, 4)
        if parent in imitators:
            imitators.remove(parent)

        R = random.randint(0, len(parent)-1)
        a = imitators[0]
        b = imitators[1]
        c = imitators[2]
        child = []

        for i in range(len(parent)):
            value_p = parent[i]
            value_a = a[i]
            value_b = b[i]
            value_c = c[i]

            if random.random() < self.mutation or i == R:
                new_value = value_a + (value_b - value_c)
                new_value = min(len(self.batteries)-1, max(0, new_value))       # Keep value within bounds
                child.append(new_value)
            else:
                child.append(value_p)
        
        return child


    def __compare_individuals(self, individual_one, individual_two):
        score_one = self.__calculate_score(individual_one)
        score_two = self.__calculate_score(individual_two)

        if score_one[0] != score_two[0]:
            score_one = score_one[0]
            score_two = score_two[0]
        elif abs(score_one[1] - score_two[1]) > 0.0001:
            score_one = score_one[1]
            score_two = score_two[1]
        else:
            score_one = score_one[2]
            score_two = score_two[2]

            while score_one == score_two:
                score_one += random.random()
                score_two += random.random()
        
        if score_one > score_two:
            return individual_one
        else:
            return individual_two


    def __calculate_score(self, individual):
        # selection_order = [i for i in range(len(individual))]
        # random.shuffle(selection_order)
        selection_order = range(len(individual))

        amount_score = 0
        cost_score = 0

        for i in selection_order:
            house = self.houses[i]
            battery = self.batteries[individual[i]]

            # Connect the house if it still fits.
            if house.output <= battery.power:
                house.connect(battery)
                amount_score += 1
                cost_score += -1 * distance(house, battery) * config.cost_per_grid_section

        power_score = -1 * sum([battery.power for battery in self.batteries])
        # power_score += sum([battery.capacity for battery in self.batteries])

        for battery in self.batteries:
            battery.reset()

        return (amount_score, power_score, cost_score)
