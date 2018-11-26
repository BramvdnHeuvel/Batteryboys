from classes.map import Map
import random

grid = Map(3)

def first_fit_batteries(self,houses,batteries):
    
    connected = []
    random.shuffle(batteries)
    random.shuffle(houses)

    for battery in self.batteries:
        for house in self.houses:
            if not house in connected and battery.capacity > house.output:
                house.connection(battery)
                print(battery)
                battery.capacity -= house.output
                connected.append(house)
                print(house)
    print(len(connected)) 

@grid.execute
def first_fit_houses(self, houses, batteries):
    connected = []
    random.shuffle(batteries)
    random.shuffle(houses)
    for house in self.houses:
        for battery in self.batteries:
            if not house in connected and battery.capacity > house.output:
                house.connection(battery)
                print(battery)
                battery.capacity -= house.output
                connected.append(house)
                print(house)
    print(len(connected)) 

grid.start()