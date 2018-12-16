import random
import matplotlib.pyplot as plt


def first_fit_batteries(map):
    """
    For the first battery, try to connect the first house. Then, move to the next.
    Keep track of which houses are connected.
    If battery power is lower than the houses output, do not connect.
    """
    moneys = []
    connected = []

    for battery in map.batteries:
        for house in map.houses:
            if not house in connected and battery.power > house.output:
                map.connect(house, battery)
                connected.append(house)
    moneys.append(map.moneyspent)
    