from map import Map


grid = Map(1)

@grid.execute
def foo(self,houses,batteries):
    
    # Write a specific algorithm to execute here.
    pass

grid.start()