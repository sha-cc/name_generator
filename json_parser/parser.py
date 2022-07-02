import json

class File:
    def __init__(self, path):
        self.path = path
        with open(str(self.path), "r") as file:
            self.data = json.load(file)

    def get_value(self, index):
        return self.data[index]
    
    def length(self):
        return len(self.data)

def main():
    from random import randint
    from os.path import basename

    names_f = File("../source/names/first_names.json")
    names_f_short = basename(str(names_f.path))
    length = names_f.length()
    
    print(f"Random value from {names_f_short}: {names_f.get_value(randint(0, length))}")
    print(f"The length of {names_f_short} is: {length}")

if __name__ == "__main__":
    main()