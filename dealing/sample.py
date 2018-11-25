class FakeBattery:
    def __init__(self,max_capacity):
        self.max_capacity = max_capacity
        self.power = max_capacity
        self.connections = []
    
    def __len__(self):
        return len(self.connections)
    
    def reset(self):
        self.power = self.max_capacity
        self.connections = []

class FakeHouse:
    def __init__(self,output):
        self.output = output
    
    def connect(self,battery):
        battery.connections.append(self)
        battery.power = battery.power - self.output