import parser

for path in (parser.File.FIRST_NAMES, parser.File.SURNAMES):
    if not path.exists():
        raise FileNotFoundError(f"File {path} is not found")
