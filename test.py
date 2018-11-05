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