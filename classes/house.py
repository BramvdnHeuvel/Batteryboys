class House:
    # open file, go through houses

    def __init__(self, x, y, output):
        self.x = x 
        self.y = y 
        self.output = output
        self.connected = None
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


    def connect(self, battery):
        self.connected = battery
        battery.store(self.output)
        return self.connected
    
    def __repr__(self):
        return '<House x={} y={} out={}>'.format(self.x,self.y,self.output)

    
