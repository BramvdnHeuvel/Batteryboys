import random

def first_fit_batteries(self,houses,batteries):
    
    connected = []
    random.shuffle(batteries)
    random.shuffle(houses)

    for battery in batteries:
        for house in houses:
            if not house in connected and battery.capacity > house.output:
                house.connect(battery)
                battery.capacity -= house.output
                connected.append(house)
    print(len(connected)) 