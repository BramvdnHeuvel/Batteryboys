
def first_distance(self,houses,batteries):
    moneys = []
    connected = []

    
    
    for house in houses:
        lowest_distance = 9000
        lowest_battery = 8
        if distance(house, batteries[0]) < lowest_distance:
            lowest_distance = distance(house, batteries[0])
            lowest_battery = 0
        if distance(house, batteries[1]) < lowest_distance:
            lowest_distance = distance(house, batteries[1])
            lowest_battery = 1
        if distance(house, batteries[2]) < lowest_distance:
            lowest_distance = distance(house, batteries[2])
            lowest_battery = 2
        if distance(house, batteries[3]) < lowest_distance:
            lowest_distance = distance(house, batteries[3])
            lowest_battery = 3
        if distance(house, batteries[4]) < lowest_distance:
            lowest_distance = distance(house, batteries[4])
            lowest_battery = 4
        print(lowest_distance)
        self.connect(house, batteries[lowest_battery])
        
       
    
def distance(house, battery):
    return abs(house.x - battery.x) + abs(house.y - battery.y)
    