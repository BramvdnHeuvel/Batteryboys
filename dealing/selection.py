import random

class Generation:
    def __init__(self,parent_generation,houses,batteries):
        self.houses = houses
        self.batteries = batteries

        self.generation = 

    def __natural_selection(self,parent_one,parent_two,off_put=0.2):
        child = []

        for house_parents in zip(parent_one, parent_two):
            decision = random.random()

            # Choose a random genome
            if decision < (1-off_put)/float(2):
                child.append(house_parents[0])
            elif decision < (1-off_put):
                child.append(house_parents[1])
            else:
                child.append(random.randint(0,random_size-1))
        
        return child

    def __calculate_score(individual):

        for choice in zip(individual, self.houses):
            house = choice[1]
            battery = self.batteries[choice[0]]

            # Connect the house if it still fits.
            if house.output <= battery.power:
                house.connect(battery)
        score = sum([battery.max_capacity for battery in batteries]) - sum([battery.power for battery in batteries])

        for battery in batteries:
            battery.reset()

        return score
