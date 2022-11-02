import unittest
from unittest import TestCase
from main import *


class Tests(unittest.TestCase):

    def Q1(self):
        # Good case
        good_case = safe_call(f, 5, 7.0, 3)
        self.assertEqual(15.0, good_case)

        # Bad cases
        # Not the same parameter types
        self.assertRaises(ValueError, safe_call, f, 5, "abc", 3)
        self.assertRaises(ValueError, safe_call, f, 1.0, 5, 3)

        # diffrent number of args
        self.assertRaises(ValueError, safe_call, f, 5, 3.0, 3, 4)
        self.assertRaises(ValueError, safe_call, f, 5, 3.0)

    def Q2(self):
        #Good cases
        #Positive Numbers
        route = breadth_first_search(start=(0, 0), end=(0, 1), neighbor_function=four_neighbor_function)
        e1_route = [(0, 0), (0, 1)]
        self.assertEqual(route, e1_route)

        route = breadth_first_search(start=(0, 0), end=(1, 0), neighbor_function=four_neighbor_function)
        e2_route = [(0, 0), (1, 0)]
        self.assertEqual(l2, e2_route)

        route = breadth_first_search(start=(0, 0), end=(1, 1), neighbor_function=four_neighbor_function)
        e3_route = [(0, 0), (1, 0), (1, 1)]
        self.assertEqual(route, e3_route)

        route = breadth_first_search(start=(0, 1), end=(0, 0), neighbor_function=four_neighbor_function)
        e4_route = [(0, 1), (0, 0)]
        self.assertEqual(route, e4_ans)

        route = breadth_first_search(start=(0, 1), end=(1, 0), neighbor_function=four_neighbor_function)
        e5_route = [(0, 1), (1, 1), (1, 0)]
        self.assertEqual(route, e5_route)

        #Negative Numbers
        route = breadth_first_search(start=(0, 0), end=(0, -1), neighbor_function=four_neighbor_function)
        e6_route = [(0, 0), (0, -1)]
        self.assertEqual(route, e6_route)

        route = breadth_first_search(start=(0, 0), end=(-1, 0), neighbor_function=four_neighbor_function)
        e7_route = [(0, 0), (-1, 0)]
        self.assertEqual(route, e7_route)


    def Q3(self):
        #Check if sorted
        x = {"a": 5, "c": 6, "b": [1, 3, 2, 4], "e": {"apple", "banana", "cherry"}, "d": "acbd",
             "f": {"a": 5, "c": 6, "b": {"apple", "banana", "cherry"}, "d": "acbd"}}
        e1 = print_sorted(x)
        e1_ans = {'a': 5, 'b': [1, 2, 3, 4], 'c': 6, 'd': 'abcd', 'e': ['apple', 'banana', 'cherry'], 'f': {'a': 5, 'b': ['apple', 'banana', 'cherry'], 'c': 6, 'd': 'abcd'}}
        self.assertEqual(e1, e1_ans)

        y = {"a": 5, "c": 6, "b": [1, 3, 2, 4], "d": "acbd",
             "f": {"a": 5, "c": 6, "b": {"apple", "banana", "cherry"}, "d": "acbd"}}
        e2 = print_sorted(y)
        e2_ans = {'a': 5, 'b': [1, 2, 3, 4], 'c': 6, 'd': 'abcd', 'f': {'a': 5, 'b': ['apple', 'banana', 'cherry'], 'c': 6, 'd': 'abcd'}}
        self.assertEqual(e2, e2_ans)



if _name_ == '_main_':
    unittest.main()
