import random

class Generation:
    def __init__(self, houses, batteries, generation, mutation):
        self.houses = houses
        self.batteries = batteries
        self.mutation = mutation

        self.generation = generation

    def __next__(self):
        winners = self.select_successors()
        new_generation = []

        for i in range(len(winners)//2):
            parent_one = winners[2*i]
            parent_two = winners[2*i+1]

            new_generation.append(parent_one)
            new_generation.append(parent_two)

            new_generation.append(self.__create_child(parent_one, parent_two, self.mutation))
            new_generation.append(self.__create_child(parent_one, parent_two, self.mutation))
        
        other = Generation(self.houses, self.batteries, new_generation, self.mutation)

        if other.find_best_one()[1][0] == len(self.batteries):
            print("Found it!")
            print(other.find_best_one()[1][0])

        return other

    def find_best_one(self):
        victor = self.generation[0]

        for challenger in self.generation:
            victor = self.__compare_individuals(victor, challenger)
        
        return (victor, self.__calculate_score(victor))

    def select_successors(self):
        random.shuffle(self.generation)
        parents = []

        for i in range(len(self.generation)//2):
            individual_one = self.generation[2*i]
            individual_two = self.generation[2*i+1]

            winner = self.__compare_individuals(individual_one,individual_two)
            parents.append(winner)
        
        return parents


    def __create_child(self, parent_one, parent_two, off_put):
        child = []

        for house_parents in zip(parent_one, parent_two):
            decision = random.random()

            # Choose a random genome
            if decision < (1-off_put)/float(2):
                child.append(house_parents[0])
            elif decision < (1-off_put):
                child.append(house_parents[1])
            else:
                child.append(random.randint(0,len(self.batteries)-1))
        
        return child


    def __compare_individuals(self, individual_one, individual_two):
        score_one = self.__calculate_score(individual_one)
        score_two = self.__calculate_score(individual_two)

        if score_one[0] != score_two[0]:
            score_one = score_one[0]
            score_two = score_two[0]
        elif score_one[1] != score_two[1]:
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
        selection_order = [i for i in range(len(individual))]
        random.shuffle(selection_order)
        # selection_order = range(len(individual))

        amount_score = 0
        cost_score = 0

        for i in selection_order:
            house = self.houses[i]
            battery = self.batteries[individual[i]]

            # Connect the house if it still fits.
            if house.output <= battery.power:
                house.connect(battery)
                amount_score += 1
                cost_score += -1 * distance(house, battery)

        power_score = -1 * sum([battery.power for battery in self.batteries])
        # power_score += sum([battery.capacity for battery in self.batteries])

        for battery in self.batteries:
            battery.reset()

        return (amount_score, power_score, cost_score)
