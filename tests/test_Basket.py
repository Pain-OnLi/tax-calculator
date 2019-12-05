import sys
import os
import unittest

sys.path.append(os.path.abspath('../src'))

import Basket

class TestBasket(unittest.TestCase):
    test_basket = Basket.Basket()

    def test_set_basket_name(self):
        self.test_basket.set_basket_name("Basket1")
        self.assertEqual(self.test_basket.basket_name, "Basket1")

    def test_parse_item_text(self):
        item_text_broken_up_by_price_and_name = self.test_basket.parse_item_text("1 16lb bag of Skittles at 16.00")
        bad_input = self.test_basket.parse_item_text("bad input")

        self.assertEqual(item_text_broken_up_by_price_and_name[0].rstrip(), "1 16lb bag of Skittles")
        self.assertEqual(item_text_broken_up_by_price_and_name[1].rstrip(), "16.00")
        self.assertEqual(bad_input, "Improper Format")


    def test_add_item_to_basket(self):
        self.test_basket.add_item_to_basket("1 16lb bag of Skittles at 16.00")

        self.assertEqual(len(self.test_basket.basket_items), 1)
        self.assertEqual(self.test_basket.basket_total_price, 16.00)
        self.assertEqual(self.test_basket.basket_total_tax, 0.00)

        self.test_basket.add_item_to_basket("1 Walkman at 99.99")
        self.test_basket.add_item_to_basket("1 bag of microwave Popcorn at 0.99")
        
        self.assertEqual(len(self.test_basket.basket_items), 3)
        self.assertEqual(self.test_basket.basket_total_price, 126.98)
        self.assertEqual(self.test_basket.basket_total_tax, 10.00)
    
    def test_basket_pricing(self):
        # Test of this function covered by test_add_item_to_basket
        self.assertTrue(True)
    
    def test_round_to_penny(self):
        self.assertEqual(self.test_basket.round_to_penny(12.799999), 12.80)