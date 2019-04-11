import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """testing max_list_iter for returning the highest value in teh list or raising a ValueError if an empty list is passed into the function"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1, 2, 3]), 3)
        self.assertEqual(max_list_iter([5, 3, 1]), 5)
        self.assertEqual(max_list_iter([0, 9, 0]), 9)
        self.assertEqual(max_list_iter([1, 4, 4]), 4)
        self.assertEqual(max_list_iter([9, 9, 9]), 9)
        self.assertEqual(max_list_iter([]), None)


    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,2,2]),[2,2,1])
        self.assertEqual(reverse_rec([6, 5, 7, 9]), [9, 7, 5, 6])
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])
        self.assertEqual(reverse_rec([2,0,2]),[2,0,2])
        self.assertEqual(reverse_rec([0]),[0])
        self.assertEqual(reverse_rec([]),[])
        

    def test_bin_search(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(1, 0, 1, tlist)
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 7 )
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1 )
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), None )
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None )

if __name__ == "__main__":
        unittest.main()

    
