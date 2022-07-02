from json import load
from pathlib import Path

class File:
    PATH = Path("../source/names/")
    FIRST_NAMES = PATH / "first_names.json"
    SURNAMES = PATH / "surnames.json"

    def __init__(self, request):
        match request:
            case "first":   self.path = self.FIRST_NAMES
            case "surname": self.path = self.SURNAMES
            case _ :        raise ValueError("No such data available")

        with open(str(self.path), "r") as file:
            self.data = load(file)

    def get_value(self, index):
        return self.data[index]
    
    def length(self):
        return len(self.data)

# I probably should remove this altogether
def main():
    from random import randint
    from os.path import basename

    names_f = File("surname")
    names_f_short = basename(str(names_f.path))
    length = names_f.length()

    print(f"Random value from {names_f_short}: {names_f.get_value(randint(0, length))}")
    print(f"The length of {names_f_short} is: {length}")

if __name__ == "__main__":
    main()
