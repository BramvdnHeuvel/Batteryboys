import matplotlib.pyplot as plt

def first_distance(self,houses,batteries):
    moneys = []
    connected = []

    lowest_distance = 9000

    
    for house in houses:
        if distance(house, battery[0]) < lowest_distance:
            lowest_distance = distance(house, battery[0])
        if distance(house, battery[1]):
            lowest_distance = distance(house, battery[1])
        if distance(house, battery[2]) < lowest_distance:
            lowest_distance = distance(house, battery[2])
        if distance(house, battery[3]) < lowest_distance:
            lowest_distance = distance(house, battery[3])
        if distance(house, battery[4]) < lowest_distance:
            lowest_distance = distance(house, battery[4])
        print(lowest_distance)
        
        distance(house, battery[2])
        distance(house, battery[3])
        distance(house, battery[4])
     '
def distance(house, battery):
    return abs(house.x - battery.x) + abs(house.y - battery.y)
    