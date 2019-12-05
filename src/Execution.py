import Basket

class Execution:

    file_name = ""
    baskets_list = list()

    def __init__(self, file_name):
        self.file_name = file_name
    

    def get_file_name(self):
        return self.file_name


    def read_input_into_list(self):
        input_list = list()
        file_object = open(self.file_name, "r")
        for line in file_object:
            if line.rstrip() != "":
                input_list.append(line.rstrip())
        
        return input_list
    

    def add_baskets_to_list(self, input_list):
        temp_basket = None
        for entry in input_list:
            if "shopping basket" in entry.lower():

                if temp_basket is not None:
                    self.baskets_list.append(temp_basket)

                temp_basket = Basket.Basket(entry.rstrip())
            else:
                if temp_basket is not None:
                    temp_basket.add_item_to_basket(entry)
                    
        self.baskets_list.append(temp_basket)

        



if __name__ == "__main__":
    file_name = "input.txt"
    execution = Execution("input.txt")
    print(execution.read_input_into_list())