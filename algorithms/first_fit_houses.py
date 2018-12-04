import random

def first_fit_houses(self, houses, batteries):
    connected = []
    random.shuffle(batteries)
    random.shuffle(houses)

    for house in houses:
        for battery in batteries:
            if not house in connected and battery.power > house.output:
                self.connect(house, battery)
                connected.append(house)
    print(len(connected))
    print(self.moneyspent)