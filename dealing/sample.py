class FakeBattery:
    def __init__(self,id,max_capacity):
        self.id = id
        self.max_capacity = max_capacity
        self.power = max_capacity
        self.connections = []

class FakeHouse:
    def __init__(self,output):
        self.output = output
        self.connection = 0
    
    def connect(self,battery):
        battery.connections.append(self)
        self.connection = battery.id