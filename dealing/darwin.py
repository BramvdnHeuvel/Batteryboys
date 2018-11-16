from sample import FakeBattery, FakeHouse
import random

battery_list = [FakeBattery(0,3),  FakeBattery(1,4)]
house_list = [FakeHouse(2), FakeHouse(2), FakeHouse(3)]

def natural_selection(parent_one,parent_two,off_put=0.2):
    next_generation = []

    for house_parents in zip(parent_one,parent_two):
        decision = random.random()

        if decision < (1-off_put)/float(2):
            next_generation.append(house_parents[0])
        elif decision < (1-off_put):
            next_generation.append(house_parents[1])
        else:
            next_generation.append(0)
    
    return next_generation

print(natural_selection(range(10),range(11,20)))