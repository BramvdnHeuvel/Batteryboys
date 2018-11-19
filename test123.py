from classes.battery import Battery
from classes.house import House
import re
import pandas as pd
import matplotlib.pyplot as plt

INPUT='resources/wijk1_batterijen.txt'
INPUT_HOUSE = 'resources/wijk1_huizen.csv'

# get battery location
battery_list=[]
with open(INPUT,'r') as file:
    next(file)
    for line in file:
        result = re.findall(r'\d+.?\d*\b', line)
        x = result[0]
        y = result[1]
        capacity = result[2]
        z= [x, y, capacity]
        battery_list.append(z)
    print(battery_list)

# get house location
data = pd.read_csv(INPUT_HOUSE)
huizen = []
for index, row in data.iterrows():
    x = row['x']
    y = row['y']
    output = row['max. output']
    z= [x, y, capacity]
    huizen.append(z)
print(huizen)

# plot batteries
x = list(map(lambda x: x[0], battery_list))
y = list(map(lambda x: x[1], battery_list))

plt.scatter(x, y)

plt.grid(True)

plt.show()