from classes.house import House

def batteryswitch(self, houses, batteries):
# change x and y for batteries so that grid distance is minimal
# if battery is full connect house to second closest battery
    for battery in self.batteries:

        x_values = [house.x for house in self.houses if house.connected.id == battery.id]
        y_values = [house.y for house in self.houses if house.connected.id == battery.id]

        x_values.sort()
        y_values.sort()

        x_index = (len(x_values) - 1)//2
        y_index = (len(y_values) - 1)//2

        median_x = x_values[x_index]
        median_y = y_values[y_values]

        battery.x = median_x
        battery.y = median_y