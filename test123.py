from classes.battery import Battery
from classes.house import House
import re
import pandas as pd

INPUT='/resources/wijk1_batterijen.txt'
INPUT_HOUSE = '/resources/wijk1_huizen.csv'


battery_list=[]
with open(INPUT,'r') as file:
    next(file)
    for line in file:
        result = re.findall(r'\d+.?\d*\b', line)
        x = result[0]
        y = result[1]
        capacity = result[2]
        battery_list.append(Battery(x, y, capacity))
print(battery_list)

data = pd.read_csv(INPUT_HOUSE)
huizen = []
for index, row in data.iterrows():
    x = row['x']
    y = row['y']
    output = row['max. output']
    huizen.append(House(x, y, output))
print(huizen)