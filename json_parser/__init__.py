from parser import File

# We need to make sure that we can't load the module
# if even a single .json file is missing

for path in File.all_files():
    if not path.exists():
        raise FileNotFoundError(f"File {path} is not found")
