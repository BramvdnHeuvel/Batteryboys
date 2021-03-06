import random

def first_fit_houses(map):
    """
    For the first house, try to connect to the first battery. Then, move to the next.
    Keep track of which houses are connected.
    If battery power is lower than the houses output, do not connect.
    """
    connected = []
    for house in map.houses:
        for battery in map.batteries:
            if not house in connected and battery.power > house.output:
                map.connect(house, battery)
                connected.append(house)
    print(len(connected))
    print(map.moneyspent)

