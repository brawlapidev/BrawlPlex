_config = {
    "base_URL": "https://api.brawlstars.com/v1/clubs/%23"
}
# Gets the info of a club.
def get_club_info(tag:str="", API_key:str="") -> str:
    from requests import get
    from .errors import NetworkError
    if tag == "":
        raise ValueError("Didn't give a Brawl Stars club tag.")
    elif tag.startswith('#') == True:
        raise ValueError("# is not needed.")
    response = get(f"{_config['base_URL']}{tag}", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise NetworkError(f"The Brawl Stars API returned status code <{response.status_code}>")
# Returns all club members
def get_club_members(tag:str="", API_key:str="") -> str:
    from requests import get
    from .errors import NetworkError
    if tag == "":
        raise ValueError("Didn't give a Brawl Stars club tag.")
    elif tag.startswith('#') == True:
        raise ValueError("# is not needed.")
    response = get(f"{_config['base_URL']}{tag}/members", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise NetworkError(f"The Brawl Stars API returned status code <{response.status_code}>")