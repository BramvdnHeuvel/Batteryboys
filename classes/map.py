import config
import get_data.get as get
import matplotlib.pyplot as plt

class Map:
    """
    The map class represents a neighbourhood in the smart grid. Each neighbourhood has
    batteries and houses.
    """

    def __init__(self,neighbourhood,movable_batteries=False):
        """
        Initialize a Map and give it a neighbourhood.
        """
        self.batteries      = get.batteries(neighbourhood)
        self.houses         = get.houses(neighbourhood)
        self.neighbourhood  = neighbourhood
        
        self.batteries_can_be_moved = movable_batteries
        self.executions = []

    # Private function that refreshes moneyspent whenever it is called.
    def __money_get(self):
        return self.refresh_cost()
    moneyspent = property(__money_get)

    def start(self):
        """
        Execute all given algorithms.
        """
        for function in self.executions:
            function(self)

    def execute(self,func):
        """
        Append function to list of algorithms to be executed.
        """      
        self.executions.append(func)
    
    def connect(self,house,battery,must_connect_to_battery=True):
        """
        Connect a given house to a provided battery.
        """
        if house is None:
            raise TypeError("Could not find house that needed to be connected.")
        if battery is None:
            raise TypeError("Could not find house/battery that needed to be connected to.")
        if must_connect_to_battery and battery.__class__.__name__ != "Battery":
            raise TypeError("Cannot connect to a non-Battery object")

        house.connect(battery)
        moneyspent = distance(house, battery) * config.cost_per_grid_section 
        return moneyspent

    def disconnect(self,house,battery):
        """
        Disconnect a house from a battery.
        """
        battery.power += house.output
        house.connected = None

    def get_list(self):
        """
        Return battery id of connected house.
        """
        try:
            return [house.connected.id for house in self.houses]
        except AttributeError:
            print("Warning: Could not execute function 'get_list' due to some disconnected houses.")
            return None

    def refresh_cost(self):
        """
        Checks the total amount of money spent again, as a double check.
        """ 
        test_map = Map(self.neighbourhood)

        def test_connection(map):
            moneyspent = 0
            for house_index in zip(map.houses, self.houses):
                house = house_index[0]
                try:
                    bat_id = house_index[1].connected.id
                except AttributeError:
                    pass
                else:
                    battery = map.batteries[bat_id]
                    moneyspent += test_map.connect(house, battery)
            return moneyspent

        test_connection(test_map)
        if self.batteries_can_be_moved:
            test_map.reposition_batteries()
        moneyspent = test_connection(test_map)

        return moneyspent

    def reposition_batteries(self):
        """
        Reposition the batteries onto the cheapest position on the grid.
        """
        for battery in self.batteries:
            x_values = []
            y_values = []

            for house in self.houses:
                if house.connected is battery:
                    x_values.append(house.x)
                    y_values.append(house.y)
            
            x_values.sort()
            y_values.sort()

            x_index = (len(x_values) - 1)//2
            y_index = (len(y_values) - 1)//2

            median_x = x_values[x_index]
            median_y = y_values[y_index]

            battery.x = median_x
            battery.y = median_y

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
        Switch connections between two houses and their respective batteries.
        """
        battery1 = house1.connected
        battery2 = house2.connected
        self.disconnect(house1, battery1)
        self.disconnect(house2, battery2)
        self.connect(house1, battery2)
        self.connect(house2, battery1)


def distance(house, battery):
    """
    Calculate distance between battery and house.
    """
    return abs(house.x - battery.x) + abs(house.y - battery.y)
