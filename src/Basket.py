import Item
import math

class Basket:

    basket_name = None
    basket_items = list()
    basket_total_price = 0.00
    basket_total_tax = 0.00

    def __init__(self, basket_name):
        self.basket_name = basket_name
        # self.basket_total_price = 0.00
        # self.basket_total_sales_tax = 0.00
    

    def parse_item_text(self, item_text):
        """Function takes the full text of an item and breaks it up into the price and the item name"""

        if "at" not in item_text:
            print("Item is not properly formatted. Should be of form <ITEM> at <PRICE>")
            proper_format = False
            return "Improper Format"

        else:
            return item_text.split(" at ")
    

    def add_item_to_basket(self, item_text):
        """Function takes in item text, processes text, appends item to the basket, and updates the basket pricing"""
        # item_reference variable refers to the array of the item and the price
        item_reference = self.parse_item_text(item_text)
        
        added_item = Item.Item(item_reference[0], item_reference[1])
        self.basket_items.append(added_item)
        self.update_basket_pricing(added_item)


    def update_basket_pricing(self, item):
        self.basket_total_price = self.round_to_penny(self.basket_total_price + float(item.after_tax_price))
        self.basket_total_tax = self.round_to_penny(self.basket_total_tax + float(item.after_tax_price) - float(item.orig_price))

    def round_to_penny(self, money):
        """Rounds the money to the nearest penny to deal with python's math precision issues"""

        return round(money/0.01) * 0.01 
