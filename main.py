from classes.map import Map


grid = Map(1)

@grid.execute
def foo(self,houses,batteries):
    
    # Write a specific algorithm to execute here.
    print(houses[0])
    print("En nu de batteries!")
    print(batteries[4])

grid.start()