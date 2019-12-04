import json

class Execution:

    file_name = ""
    baskets_list = list()

    def __init__(self, file_name):
        self.file_name = file_name
    
    def get_file_name(self):
        return self.file_name

    def read_input_into_list(self):
        text_input = list()
        file_object = open(self.file_name, "r")
        for line in file_object:
            if line.rstrip() != "":
                text_input.append(line.rstrip())
        
        return text_input

if __name__ == "__main__":
    file_name = "input.txt"
    execution = Execution("input.txt")
    print(execution.read_input())
