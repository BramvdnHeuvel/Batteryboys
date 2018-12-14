import random
import matplotlib.pyplot as plt


def first_fit_batteries(self,houses,batteries):
    """
    For the first battery, try to connect the first house. Then, move to the next.
    Keep track of which houses are connected.
    If battery power is lower than the houses output, do not connect.
    """
    moneys = []
    connected = []
    # random.shuffle(batteries)
    # random.shuffle(houses)

    for battery in batteries:
        for house in houses:
            if not house in connected and battery.power > house.output:
                self.connect(house, battery)
                connected.append(house)
    print(len(connected))
    moneys.append(self.moneyspent)
    