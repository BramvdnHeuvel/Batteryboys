import random

def first_fit_batteries(self,houses,batteries):
    
    connected = []
    random.shuffle(batteries)
    random.shuffle(houses)

    for battery in batteries:
        for house in houses:
            if not house in connected and battery.power > house.output:
                self.connect(house, battery)
                connected.append(house)
    print(len(connected))
    print(self.moneyspent)
    for battery in self.batteries:
        battery.reset()