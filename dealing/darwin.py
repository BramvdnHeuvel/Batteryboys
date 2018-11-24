from sample import FakeBattery, FakeHouse
import random

battery_list = [FakeBattery(150),  FakeBattery(175)]
house_list = [FakeHouse(i) for i in range(25) ]

def __natural_selection(parent_one, parent_two, random_size=len(battery_list), off_put=0.2):
    child = []

    for house_parents in zip(parent_one,parent_two):
        decision = random.random()

        # Choose a random genome
        if decision < (1-off_put)/float(2):
            child.append(house_parents[0])
        elif decision < (1-off_put):
            child.append(house_parents[1])
        else:
            child.append(random.randint(0,random_size-1))
    
    return child


def __calculate_score(individual, house_list=house_list, battery_list=battery_list):
    houses = house_list
    batteries = battery_list

    for choice in zip(houses,individual):
        house = choice[0]
        battery = batteries[choice[1]]

        # Connect the house if it still fits.
        if house.output <= battery.power:
            house.connect(battery)
    score = sum([battery.power for battery in batteries]) - sum([battery.max_capacity for battery in batteries])

    for battery in batteries:
        battery.reset()

    if score > 0:
        print(score)
    if score == 0:
        print("That happens suspiciously often.")
    return score


def __generate_first_generation(houses=house_list, batteries=battery_list, population=400):
    return [[random.randint(0,len(batteries)-1) for j in houses] for i in range(2*population)]

def __generate_new_generation(old_generation):
    new_generation = []
    
    for i in range(len(old_generation) // 4):
        parent_one = old_generation[2*i][1]
        parent_two = old_generation[2*i+1][1]

        child1 = __natural_selection(parent_one, parent_two)
        child2 = __natural_selection(parent_one, parent_two)
        child3 = __natural_selection(parent_one, parent_two)
        child4 = __natural_selection(parent_one, parent_two)

        new_generation.append(child1)
        new_generation.append(child2)
        new_generation.append(child3)
        new_generation.append(child4)

    return new_generation    

def generate_algorithm(amount=20, maximum=len(house_list), house_list=house_list, battery_list=battery_list):
    generation = __generate_first_generation()
    generation = [(__calculate_score(individual),individual) for individual in generation]
    generation.sort(reverse=True)20

    houses = house_list
    batteries = battery_list

    for i in range(amount):
        maximal_score = sum([house.output for house in houses]) - 

        if generation[0][0] == 0: # TODO: Take punishment into account
            print('Found optimal solution!')
            break

        if i % 10 == 0:
            print("Generation {}:\t{}".format(i,generation[0]))

        generation = __generate_new_generation(generation)
        generation = [(__calculate_score(individual),individual) for individual in generation]
        generation.sort(reverse=True)

    return generation[0]

print(generate_algorithm(200))