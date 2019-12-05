import Basket
import copy

class Execution:

    file_name = ""
    baskets_list = list()

    def __init__(self, file_name):
        self.file_name = file_name


    def read_input_into_list(self):
        """Read input file into list"""

        input_list = list()
        file_object = open(self.file_name, "r")
        for line in file_object:
            if line.rstrip() != "":
                input_list.append(line.rstrip())
        
        return input_list
    

    def add_baskets_and_items(self, input_list):
        """Add baskets to a list and place the items in those baskets"""

        temp_basket = Basket.Basket()
        for entry in input_list:
            
            if "shopping basket" in entry.lower():
                if temp_basket.basket_name is not None:
                    self.baskets_list.append(copy.copy(temp_basket))
                    temp_basket.empty_basket()

                temp_basket.set_basket_name(entry)

            else:
                if temp_basket is not None:
                    temp_basket.add_item_to_basket(entry)

        self.baskets_list.append(temp_basket)

    def print_result(self):
        """Print the desired results"""

        for basket in self.baskets_list:
            print(basket.basket_name)
            for item in basket.basket_items:
                print(item.item_name + ": " + item.after_tax_price)
            print("Sales Taxes: " + str(basket.basket_total_tax))
            print("Total: " + str(basket.basket_total_price))
            print()

        
if __name__ == "__main__":
    file_name = "input.txt"
    execution = Execution("input.txt")
    input_list = execution.read_input_into_list()
    print(input_list)
    execution.add_baskets_and_items(input_list)
    execution.print_result()