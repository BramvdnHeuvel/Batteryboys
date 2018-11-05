from resources import get
import unittest

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
    
    
    # Change this name when you're working on this part.
    def t3st_importer(self):
        self.assertEqual(get.batteries(1),[[38,12], [43,13], [42,3], [49,23], [3,45]])
        self.assertEqual(get.batteries(2),[[19,20], [1,36], [34,49], [41,21], [26,22]])
        self.assertEqual(get.batteries(3),[[18,34], [32,11], [41,1], [3,35], [39,41]])

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