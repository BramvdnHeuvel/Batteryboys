import matplotlib.pyplot as plt
from classes.battery import Battery
from classes.house import House
from moveit.get import __load_batteries
from moveit.get import __load_houses
import random

def visualization(self, huizen, battery_list):      
         # plot batteries and houses
        x = list(map(lambda x: x[0], battery_list))
        y = list(map(lambda x: x[1], battery_list))
        x1 = list(map(lambda x: x[0], huizen))
        y1 = list(map(lambda x: x[1], huizen))

        plt.scatter(x, y, color ='red')
        plt.scatter(x1, y1, color='blue')

        plt.grid(True)

        return plt.show()

# def visualize_connections(self)
#         first line between coordinates of house and x or y coordinate from battery(randomly chosen) and 
#         depending on this decision y or x coordinate from house
#         second line 