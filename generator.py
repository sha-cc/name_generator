from json import load
from pathlib import Path, PosixPath
from os.path import exists
from random import randint

class File:
    PATH = Path("./source")
    AVAILABLE_REQUESTS = {
        "first names":   "names/first_names.json",
        "surnames":      "names/surnames.json"
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

    def get_value(self, *index):
        if index:
            return self.data[index[0]]
        else:
            return self.data[randint(0, len(self.data))]

    @classmethod
    def all_files(cls) -> list[PosixPath]:
        files = []
        for value in cls.AVAILABLE_REQUESTS.values():
            files.append(cls.PATH / Path(value))
        return files


class Date:
    @classmethod
    def full_date(cls):
        return f"{cls.get_day()}.{str(cls.random_month()).zfill(2)}.{cls.random_year()}"

    @classmethod
    def get_day(cls, *args: int) -> int:
        def match_month(month: int) -> int:
            match month:
                case 1 | 3 | 5 | 7 | 8 | 10 | 12: return randint(1, 31)
                case 4 | 6 | 9 | 11: return randint(1, 30)
                case 2: return randint(1, 28)
                case other: raise ValueError(f"{other} is not a valid month")

        if args:
            return match_month(args[0])
        else:
            return match_month(cls.random_month())

    @staticmethod
    def random_month() -> int:
        return randint(1, 12)

    @staticmethod
    def random_year() -> int:
        year_first_part = randint(19, 20)
        year_last_part = "{:02d}".format(randint(0, 99))
        return int(f"{year_first_part}{year_last_part}")


def check_files():
    for file in File.all_files():
        if not exists(file):
            raise FileNotFoundError(f"File {file} not found")

def main():
    check_files()
    print(Date.full_date())

if __name__ == "__main__":
    main()