import sys
import os
import unittest

sys.path.append(os.path.abspath('../src'))

import Execution

class TestExecution(unittest.TestCase):
    execution = Execution.Execution("TestInput.txt")
    input_list = execution.read_input_into_list()

    def test_read_input_into_list(self):
        
        self.assertEqual(len(self.input_list),12)
        self.assertEqual(self.input_list[0], "Shopping Basket 1:")
        self.assertEqual(self.input_list[5], "1 imported bag of Vanilla-Hazelnut Coffee at 11.00")
        self.assertEqual(self.input_list[11], "1 300# bag of Fair-Trade Coffee at 997.99")
    

    def test_add_baskets_and_items(self):
        self.execution.add_baskets_and_items(self.input_list)

        self.assertEqual(len(self.execution.baskets_list), 3)
        self.assertEqual(self.execution.baskets_list[0].basket_name, "Shopping Basket 1:")
        self.assertEqual(self.execution.baskets_list[1].basket_name, "Shopping Basket 2:")
        self.assertEqual(self.execution.baskets_list[2].basket_name, "Shopping Basket 3:")