import get
import scheme
import unittest

from classes.battery import Battery
from classes.house import House

class Test_Algorithms(unittest.TestCase):

    # This class tests functions and makes sure they work.
    # If the function's name starts with "test", the test is executed.
    
    def test_obvious_stuff(self):
        self.assertEqual(2+2, 4)
        self.assertEqual(4*4, 16)
        self.assertGreater(1000, 1)

        self.assertTrue(1 != 0)
    

    def good_thing_this_function_is_ignored(self):
        self.assertEqual(1,2)
    
    def test_battery_class(self):
        battery = Battery(1,2,1500)

        self.assertEqual(battery.x, 1)
        self.assertEqual(battery.y, 2)
        self.assertEqual(battery.max_capacity, 1500)
        self.assertEqual(battery.power, 1500)

        battery.store(500)

        self.assertEqual(battery.max_capacity, 1500)
        self.assertEqual(battery.power, 1000)

    # Change this name when you're working on this part.
    def t3st_importer_batteries(self):
        self.assertEqual(get.batteries(1),[Battery(38,12,1507.0), Battery(43,13,1507.0), Battery(42,3,1507.0), Battery(49,23,1507.0), Battery(3,45,1507.0)])
        self.assertEqual(get.batteries(2),[Battery(19,20,1508.25), Battery(1,36,1508.25), Battery(34,49,1508.25), Battery(41,21,1508.25), Battery(26,22,1508.25)])
        self.assertEqual(get.batteries(3),[Battery(18,34,1506.75), Battery(32,11,1506.75), Battery(41,1,1506.75), Battery(3,35,1506.75), Battery(39,41,1506.75)])

    # Change this name when you're working on this part.
    def t3st_importer_houses(self):

        first_house = get.houses(1)[0]
        second_house = get.houses(1)[1]
        random_house = get.houses(3)[2]

        self.assertEqual(first_house.x, 34)
        self.assertEqual(first_house.y, 47)
        self.assertEqual(first_house.output, 53.97543253)

        self.assertEqual(second_house.x, 24)
        self.assertEqual(second_house.y, 22)
        self.assertEqual(second_house.output, 66.13020717)

        self.assertEqual(random_house.x, 25)
        self.assertEqual(random_house.y, 31)
        self.assertEqual(random_house.output, 51.81241388)

    def test_dr_manhattan(self):
        self.assertEqual(scheme.manhattan_distance(10,0,0,0),10)
        self.assertEqual(scheme.manhattan_distance(0,10,0,0),10)
        self.assertEqual(scheme.manhattan_distance(0,0,10,0),10)
        self.assertEqual(scheme.manhattan_distance(0,0,0,10),10)
        
        self.assertEqual(scheme.manhattan_distance(10,0,0,10),20)
        self.assertEqual(scheme.manhattan_distance(-10,0,0,0),10)
        self.assertEqual(scheme.manhattan_distance(-10,0,10,0),20)
        self.assertEqual(scheme.manhattan_distance(1,2,3,4),4)
        self.assertEqual(scheme.manhattan_distance(10,0,100,1000),1090)

