# This class is the representation 

import math

class Item:

    raw_item_text = None
    proper_format = None
    item_name = None
    is_imported = None
    is_tax_exempt = None
    orig_price = None
    after_tax_price = None

    # Candy types is hard coded here as a quick and dirty solution
    # The proper way would be to read it from a config file or database, or one 
    # could use a hash map to make the lookup time much faster
    candy_types = ["Skittles", "Snickers", "Nerds", "Twix", "Gobstoppers"]

    def __init__(self, item_name, item_price):
        self.item_name = item_name.rstrip()
        self.orig_price = item_price.rstrip().replace(",", "")
        self.is_imported = self.is_item_imported()
        self.is_tax_exempt = self.is_item_tax_exempt()
        self.after_tax_price = self.calculate_final_price()
    
    
    def is_item_imported(self):
        """Function returns boolean for whether the item is determined to be imported"""

        if "imported" in self.item_name.lower():
            return True
        else: 
            return False
    
    def is_item_tax_exempt(self):
        """Function returns boolean for whether the item is determined to be tax exempt"""
        if "coffee" in self.item_name.lower():
            return True
        
        if "popcorn" in self.item_name.lower(): 
            return True

        for candy in self.candy_types:
            if candy.lower() in self.item_name.lower():
                return True
        
        return False


    def calculate_final_price(self):
        """Function calculates the after tax price of the item as a string"""
        
        

        try: 
            numerical_orig_price = float(self.orig_price)
            final_price = numerical_orig_price
        except ValueError:
            print("Price is not in a readable format")
            proper_format = False
            return "Improper Format"
        
        if not self.is_tax_exempt:
            final_price = final_price + self.round_tax(numerical_orig_price * 0.1)

        if self.is_imported: 
            import_tax = numerical_orig_price * 0.05
            final_price = final_price + self.round_tax(import_tax)
    

        return str("{:.2f}".format((round(final_price,2))))

    
    def round_tax(self, tax):
        """Rounds the tax up to the nearest 0.05"""

        return math.ceil(tax/0.05) * 0.05 







        