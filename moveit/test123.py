from classes.battery import Battery
from classes.house import House
import re
import pandas as pd
import matplotlib.pyplot as plt
import random
from classes.map import Map

INPUT='resources/wijk1_batterijen.txt'
INPUT_HOUSE = 'resources/wijk1_huizen.csv'

# get battery location
battery_list=[]
with open(INPUT,'r') as file:
    next(file)
    for line in file:
        result = re.findall(r'\d+.?\d*\b', line)
        x = float(result[0])
        y = float(result[1])
        capacity = result[2]
        z= [x, y, capacity]
        battery_list.append(z)
    

# get house location
data = pd.read_csv(INPUT_HOUSE)
huizen = []
for index, row in data.iterrows():
    x = row['x']
    y = row['y']
    output = row['max. output']
    z= [x, y, output]
    huizen.append(z)

# plot batteries and houses
x = list(map(lambda x: x[0], battery_list))
y = list(map(lambda x: x[1], battery_list))
x1 = list(map(lambda x: x[0], huizen))
y1 = list(map(lambda x: x[1], huizen))

print(list((map(lambda x: x[0], battery_list))))

plt.scatter(x, y, color ='red')
plt.scatter(x1, y1, color='blue')

# create lines between houses and batteries
random.choice([x, y])
if random.choice == x:
    pass
    # choose battery y coordinate
    # plot first line
    # plot second line

elif random.choice == y:
    # choose battery x coordinate
    # plot first line
    # plot second line
    plt.plot(x, y)


plt.grid(True)

plt.show()



# def first_fit_houses(self, houses, batteries):
#     connected = []
#     random.shuffle(batteries)
#     random.shuffle(houses)

#     for house in houses:
#         for battery in batteries:
#             if not house in connected and battery.capacity > house.output:
#                 house.connection(battery)
#                 battery.capacity -= house.output
#                 connected.append(house)
#     return(len(connected))