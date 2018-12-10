import random
import matplotlib.pyplot as plt


def first_fit_batteries(self,houses,batteries):
    moneys = []
    connected = []
    random.shuffle(batteries)
    random.shuffle(houses)

    for battery in batteries:
        for house in houses:
            if not house in connected and battery.power > house.output:
                self.connect(house, battery)
                connected.append(house)
    print(len(connected))
    print(battery)
    moneys.append(self.moneyspent)
    