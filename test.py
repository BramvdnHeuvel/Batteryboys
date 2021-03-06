import unittest

from get_data import get
from classes.battery import Battery
from classes.house import House
from classes.map import distance

class Test_Algorithms(unittest.TestCase):
    """
    This class tests functions and makes sure they work.
    If the function's name starts with "test", the test is executed.
    """
    
    def test_obvious_stuff(self):
        self.assertEqual(2+2, 4)
        self.assertEqual(4*4, 16)
        self.assertGreater(1000, 1)

        self.assertTrue(1 != 0)
    

    def good_thing_this_function_is_ignored(self):
        self.assertEqual(1,2)

    def test_battery_class(self):
        battery = Battery(0,1,2,1500)

        self.assertEqual(battery.id, 0)
        self.assertEqual(battery.x, 1)
        self.assertEqual(battery.y, 2)
        self.assertEqual(battery.capacity, 1500)
        self.assertEqual(battery.power, 1500)

        battery.store(500)

        self.assertEqual(battery.capacity, 1500)
        self.assertEqual(battery.power, 1000)

    # Change this name when you're working on this part.
    def test_importer_batteries(self):
        self.assertEqual(get.batteries(1),[Battery(0,38,12,1507.0), Battery(1,43,13,1507.0), Battery(2,42,3,1507.0), Battery(3,49,23,1507.0), Battery(4,3,45,1507.0)])
        self.assertEqual(get.batteries(2),[Battery(0,19,20,1508.25), Battery(1,1,36,1508.25), Battery(2,34,49,1508.25), Battery(3,41,21,1508.25), Battery(4,26,22,1508.25)])
        self.assertEqual(get.batteries(3),[Battery(0,18,34,1506.75), Battery(1,32,11,1506.75), Battery(2,41,1,1506.75), Battery(3,3,35,1506.75), Battery(4,39,41,1506.75)])

    # Change this name when you're working on this part.
    def test_importer_houses(self):

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

