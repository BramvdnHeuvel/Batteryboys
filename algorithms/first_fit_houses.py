import random

def first_fit_houses(self, houses, batteries):
    connected = []
    random.shuffle(batteries)
    random.shuffle(houses)

    for house in houses:
        for battery in batteries:
            if not house in connected and battery.capacity > house.output:
                house.connection(battery)
                battery.capacity -= house.output
                connected.append(house)
    return(len(connected))

