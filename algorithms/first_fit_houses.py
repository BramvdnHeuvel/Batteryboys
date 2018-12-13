import random

def first_fit_houses(self, houses, batteries):
    connected = []


    for house in houses:
        for battery in batteries:
            if not house in connected and battery.power > house.output:
                self.connect(house, battery)
                connected.append(house)
    print(len(connected))
    print(self.moneyspent)
    for battery in self.batteries:
        battery.reset()
