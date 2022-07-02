from json import load
from pathlib import Path

class File:
    PATH = Path("../source")
    AVAILABLE_REQUESTS = {
        "first name":   "names/first_names.json",
        "surname":      "names/surnames.json"
    }

    def __init__(self, request):
        # If AVAILABLE_REQUESTS has the key that we are asking for,
        # get its value (path to .json) and make in into the full path
        try:
            self.path = self.PATH / self.AVAILABLE_REQUESTS.get(request)
        except Exception:
            raise ValueError(f"\"{request}\" is not a valid option")

        with open(self.path, "r") as file:
            self.data = load(file)

    def get_value(self, index):
        return self.data[index]
    
    def length(self):
        return len(self.data)

    @classmethod
    def all_files(cls):
        files = []
        for value in cls.AVAILABLE_REQUESTS.values():
            files.append(cls.PATH / Path(value))
        return files

# I probably should write unit tests at this point
def main():
    from random import randint
    from os.path import basename

    names = File("surname")
    names_short = basename(str(names.path))
    length = names.length()

    print(f"Random value from {names_short}: {names.get_value(randint(0, length))}")
    print(f"The length of {names_short} is: {length}")

if __name__ == "__main__":
    main()
