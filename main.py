from classes.map import Map
import random

grid = Map(1)

@grid.execute
def foo(self,houses,batteries):
    
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

    # Write a specific algorithm to execute here.
    # nu print het 150 huizen, allemaal in een v/d 5 batterijen. zien nu welke batterij + huis.

grid.start()