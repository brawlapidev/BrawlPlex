_config = {
    "base_URL": "https://api.brawlstars.com/v1/players/%23"
}
# Returns player battle log
def get_player_battlelog(tag:str="", API_key:str="") -> str:
    from requests import get
    from .errors import NetworkError
    if tag == "":
        raise ValueError("Didn't give a Brawl Stars player tag.")
    elif tag.startswith('#') == True:
        raise ValueError("# is not needed.")
    response = get(f"{_config['base_URL']}{tag}/battlelog", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return NetworkError(response.status_code)
# Gets player info
def get_player_info(tag:str="", API_key:str="") -> str:
    from requests import get
    from .errors import NetworkError
    if tag == "":
        raise ValueError("Didn't give a Brawl Stars player tag.")
    elif tag.startswith('#') == True:
        raise ValueError("# is not needed.")
    response = get(f"{_config['base_URL']}{tag}", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return NetworkError(response.status_code)