import sys
import os
import unittest

sys.path.append(os.path.abspath('../src'))

import Item

class TestItem(unittest.TestCase):
    test_item_1 = Item.Item("1 16lb bag of Skittles", "16.00")
    test_item_2 = Item.Item("1 Walkman", "99.99")
    test_item_3 = Item.Item("1 bag of microwave Popcorn", "0.99")
    test_item_4 = Item.Item("1 imported bag of Vanilla-Hazelnut Coffee", "11.00")
    test_item_5 = Item.Item("1 Imported Vespa", "15,001.25")
    test_item_6 = Item.Item("1 imported crate of Almond Snickers", "75.99")
    test_bad_item = Item.Item("bad", "input")

    # def test_parse_item_text(self):
    #     item_1_split_by_at = self.test_item_1.parse_item_text()
    #     bad_input = self.test_bad_item.parse_item_text()
    #     self.assertEqual(item_1_split_by_at[0], "1 16lb bag of Skittles")
    #     self.assertEqual(bad_input, "Improper Format")

    def test_is_item_imported(self):
        self.assertFalse(self.test_item_1.is_item_imported())
        self.assertTrue(self.test_item_4.is_item_imported())
    
    def test_is_item_tax_exempt(self):
        self.assertTrue(self.test_item_1.is_item_tax_exempt())
        self.assertFalse(self.test_item_2.is_item_tax_exempt())
        self.assertTrue(self.test_item_3.is_item_tax_exempt())
        self.assertTrue(self.test_item_4.is_item_tax_exempt())
        self.assertFalse(self.test_item_5.is_item_tax_exempt())
        self.assertTrue(self.test_item_6.is_item_tax_exempt())
        self.assertFalse(self.test_bad_item.is_item_tax_exempt())
    
    def test_calculate_final_price(self):
        self.assertEqual(self.test_item_1.calculate_final_price(), "16.00")
        self.assertEqual(self.test_item_2.calculate_final_price(), "109.99")
        self.assertEqual(self.test_item_3.calculate_final_price(), "0.99")
        self.assertEqual(self.test_item_4.calculate_final_price(), "11.55")
        self.assertEqual(self.test_item_5.calculate_final_price(), "17251.50")
        self.assertEqual(self.test_item_6.calculate_final_price(), "79.79")
        self.assertEqual(self.test_bad_item.calculate_final_price(), "Improper Format")

    def test_round_tax(self):
        self.assertEqual(1.75, self.test_item_1.round_tax(1.72))
        self.assertEqual(15.50, self.test_item_1.round_tax(15.50))
        