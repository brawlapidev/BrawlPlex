from . import player, clubs, brawlers, events, rankings
# This function only reads the API key form a file
def get_API_key(file_path:str=""):
    if file_path == "":
        raise ValueError("File path was not given.")
    with open(file_path, 'r') as file:
        key = file.read()
        return key