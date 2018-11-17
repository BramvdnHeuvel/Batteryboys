from classes.map import Map


grid = Map(1)

@grid.execute
def foo(self,houses,batteries):
    
    # Write a specific algorithm to execute here.
    pass

@grid.execute
def first_fit_algorithm(self,houses,batteries):
    for i in range(len(self.houses)):
        house = self.houses[i]

        for battery in self.batteries:
            if battery.power > house.output:
                self.connect(house,battery)
                break
        
        # =========================================
        print("Ran out of batteries.\n\nMoney spent: " + self.moneyspent)
        print("\nPower left in batteries:\n" + [battery.power for battery in self.batteries])
        print("\nHouses left to distribute:")
        for j in range(len(self.houses) - i):
            unused_house = self.houses[i+j]
            print(unused_house.output)
        raise IndexError("Ran out of batteries to place houses in")

    print("Successfully distributed houses!")
    print("Money spent: " + self.moneyspent)

grid.start()