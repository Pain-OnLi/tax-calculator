import sys
import os
import unittest

sys.path.append(os.path.abspath('../src'))

import Execution

class TestExecution(unittest.TestCase):
    execution = Execution.Execution("TestInput.txt")

    def test_get_file_name(self):
        self.assertEqual(self.execution.get_file_name(), "TestInput.txt")

    def test_read_input(self):
        input_list = self.execution.read_input_into_list()
        self.assertEqual(len(input_list),12)
        self.assertEqual(input_list[0], "Shopping Basket 1:")
        self.assertEqual(input_list[5], "1 imported bag of Vanilla-Hazelnut Coffee at 11.00")
        self.assertEqual(input_list[11], "1 300# bag of Fair-Trade Coffee at 997.99")