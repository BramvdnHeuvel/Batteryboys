class House:
    def __init__(self,x,y,output):
        self.x              = int(x)
        self.y              = int(y)
        self.output         = float(output)
        self.connection     = None
        self.route          = []
    
    def connect(self,connected_obect):
        """Connect the house to another object. The route also needs to be determined here."""

        pass # TODO


def batteries(neighbourhood):
    """Gain a list of batteries from a given neighbourhood. The neighbourhood is an integer."""

    pass # TODO


def houses(neighbourhood):
    """Gain a list of houses from a given neighbourhood. The neighbourhood is an integer."""

    pass # TODO