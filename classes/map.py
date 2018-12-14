import config
import get_data.get as get
import matplotlib.pyplot as plt

class Map:
    """
    The map class represents a neighbourhood in the smart grid. Each neighbourhood has
    batteries and houses.
    """

    def __init__(self,neighbourhood):
        """Initialize a Map and give it a neighbourhood."""
        self.batteries  = get.batteries(neighbourhood)
        self.houses     = get.houses(neighbourhood)
        self.moneyspent = 0
        
        self.executions = []

    def start(self):
        for function in self.executions:
            function(self,self.houses,self.batteries)

    def execute(self,func):
        self.executions.append(func)
    
    def connect(self,house,battery,must_connect_to_battery=True):
        """When house is connected to battery increase moneyspent."""
        if house is None:
            raise TypeError("Could not find house that needed to be connected.")
        if battery is None:
            raise TypeError("Could not find house/battery that needed to be connected to.")
        if must_connect_to_battery and battery.__class__.__name__ != "Battery":
            raise TypeError("Cannot connect to a non-Battery object")

        house.connect(battery)
        self.moneyspent += distance(house, battery) * config.cost_per_grid_section 

    def disconnect(self,house,battery,must_connect_to_battery=True):
        """When disconnected reduce moneyspent."""
        battery.power += house.output
        self.moneyspent -= distance(house, battery) * config.cost_per_grid_section

    def get_list(self):
        return [house.connected.id for house in self.houses]

    def __connect(self,x1,y1,x2,y2,must_connect_to_battery):
        """
        Connect battery to house.
        """        
        house = self.__find_object(x1,y1)
        battery = self.__find_object(x2,y2)

        return self.connect(house,battery,must_connect_to_battery)

    def __find_object(self,x,y):
        """
        Find the object that is located on a given location.
        """
        for battery in self.batteries:
            if x == battery.x and y == battery.y:
                return battery
        
        for house in self.houses:
            if x == house.x and y == house.y:
                return house
        
        return None

    def refresh_cost(self):
        """
        Set costs to zero
        """ 
        self.moneyspent = 0

        for house_index in zip(self.houses, self.get_list()):
            house = house_index[0]
            bat_id = house_index[1]

            battery = self.batteries[bat_id]

            self.connect(house, battery)

        return self.moneyspent

    def visualize(self):
        """
        Plots houses, batteries, and connections.
        """
        batteries_x = list(battery.x for battery in self.batteries)
        batteries_y = list(battery.y for battery in self.batteries)
        houses_x = list(house.x for house in self.houses)
        houses_y = list(house.y for house in self.houses)
        
        # get x and y coords of connected battery for each house
        house_batteries = list(house.connected for house in self.houses)
        con_batteries_x = list(battery.x for battery in house_batteries)
        con_batteries_y = list(battery.y for battery in house_batteries)
        con_batteries_id = list(battery.id for battery in house_batteries)
        
        # draw lines between connected houses and batteries
        plt.figure(figsize=(10,10))
        colors = ['g', 'y', 'm', 'k', 'c']

        for i in range(len(house_batteries)):
            plt.plot([houses_x[i], con_batteries_x[i]], [houses_y[i], houses_y[i]], color = colors[con_batteries_id[i]], zorder = 1)
            plt.plot([con_batteries_x[i], con_batteries_x[i]], [houses_y[i], con_batteries_y[i]], color = colors[con_batteries_id[i]], zorder = 1)

        # draw points and plot      
        plt.scatter(houses_x, houses_y, color ='red', zorder = 2, marker="s")
        plt.scatter(batteries_x, batteries_y, color='blue', zorder = 2, marker="o")
        plt.title("Smart Grid")
        plt.grid(True)
        plt.show()

    def swap(self, house1, house2):
        """
        Swap function to switch connections between two houses and batteries.
        """
        battery1 = house1.connected
        battery2 = house2.connected
        self.disconnect(house1, battery1)
        self.disconnect(house2, battery2)
        self.connect(house1, battery2)
        self.connect(house2, battery1)

        print(self.moneyspent)

def distance(house, battery):
    """
    Calculate distance between battery and house.
    """
    return abs(house.x - battery.x) + abs(house.y - battery.y)

