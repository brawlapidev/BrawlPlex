_config = {
    "base_URL": "https://api.brawlstars.com/v1/brawlers"
}
# Returns a list of all brawlers
def get_brawler_list(API_key) -> str:
    from requests import get
    from .errors import NetworkError
    response = get(f"{_config['base_URL']}", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return NetworkError(response.status_code)
# Gets info on a brawler by its tag
def get_brawler_info(brawler_tag:str="", API_key:str="") -> str:
    from requests import get
    from .errors import NetworkError
    if brawler_tag == "":
        raise ValueError("Didn't give a Brawl Stars player tag.")
    elif brawler_tag.startswith('#') == True:
        raise ValueError("# is not needed.")
    response = get(f"{_config['base_URL']}/{brawler_tag}", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return NetworkError(response.status_code)