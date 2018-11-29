import matplotlib.pyplot as plt
from classes.battery import Battery
from classes.house import House
from get import __load_batteries
from get import __load_houses

def visualization(self, houses, batteries):
        # plot batteries and houses
        x = list(map(lambda x: x[0], battery_list))
        y = list(map(lambda x: x[1], battery_list))
        x1 = list(map(lambda x: x[0], huizen))
        y1 = list(map(lambda x: x[1], huizen))

        plt.scatter(x, y, color ='red')
        plt.scatter(x1, y1, color='blue')

        plt.grid(True)

        plt.show()