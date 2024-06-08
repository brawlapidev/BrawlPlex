_config = {
    "base_URL": "https://api.brawlstars.com/v1/rankings/"
}
# Gets player rankings in a serten region
def get_player_rankings(region_code: str, limit:str, return_after:str = "", return_before:str = "", API_key: str = "") -> str:
    from requests import get
    from .errors import NetworkError
    URL_addon = f"{region_code}/players?"
    needs_and = False
    if return_after != "" and return_before != "":
        raise ValueError('Use only one of "start_from" or "end_at", not both.')
    elif return_after != "":
        URL_addon += f"after={return_after}"
        needs_and = True
    elif return_before != "":
        if needs_and:
            URL_addon += f"&before={return_before}"
        else:
            URL_addon += f"before={return_before}"
    if needs_and:
        URL_addon += f"&limit={limit}"
    else:
        URL_addon += f"limit={limit}"
    url = _config['base_URL'] + URL_addon
    response = get(url, headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise NetworkError(f"The Brawl Stars API returned status code {response.status_code}")
# Gets brawler rankings in one region
def get_brawler_rankings(region_code: str, limit:str, brawler_tag:str, return_after:str = "", return_before:str = "", API_key: str = "") -> str:
    from requests import get
    from .errors import NetworkError
    URL_addon = f"{region_code}/brawlers/{brawler_tag}?"
    needs_and = False
    if return_after != "" and return_before != "":
        raise ValueError('Use only one of "return_after" or "return_before", not both.')
    elif return_after != "":
        URL_addon += f"after={return_after}"
        needs_and = True
    elif return_before != "":
        if needs_and:
            URL_addon += f"&before={return_before}"
        else:
            URL_addon += f"before={return_before}"
    if needs_and:
        URL_addon += f"&limit={limit}"
    else:
        URL_addon += f"limit={limit}"
    response = get(f"{_config["base_URL"]}{URL_addon}", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise NetworkError(f"The Brawl Stars API returned status code {response.status_code}")
# Get club ranking in one region
def get_club_rankings(region_code: str, limit:str, return_after:str = "", return_before:str = "", API_key: str = "") -> str:
    from requests import get
    from .errors import NetworkError
    URL_addon = f"{region_code}/clubs?"
    needs_and = False
    if return_after != "" and return_before != "":
        raise ValueError('Use only one of "return_after" or "return_before", not both.')
    elif return_after != "":
        URL_addon += f"after={return_after}"
        needs_and = True
    elif return_before != "":
        if needs_and:
            URL_addon += f"&before={return_before}"
        else:
            URL_addon += f"before={return_before}"
    if needs_and:
        URL_addon += f"&limit={limit}"
    else:
        URL_addon += f"limit={limit}"
    response = get(f"{_config["base_URL"]}{URL_addon}", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise NetworkError(f"The Brawl Stars API returned status code {response.status_code}")
# Gets powrplay season tag and start and end dates
def get_powerplay_seasons(region_code: str, limit:str, return_after:str = "", return_before:str = "", API_key: str = "") -> str:
    from requests import get
    from .errors import NetworkError
    URL_addon = f"{region_code}/powerplay/seasons?"
    needs_and = False
    if return_after != "" and return_before != "":
        raise ValueError('Use only one of "return_after" or "return_before", not both.')
    elif return_after != "":
        URL_addon += f"after={return_after}"
        needs_and = True
    elif return_before != "":
        if needs_and:
            URL_addon += f"&before={return_before}"
        else:
            URL_addon += f"before={return_before}"
    if needs_and:
        URL_addon += f"&limit={limit}"
    else:
        URL_addon += f"limit={limit}"
    print(f"{_config['base_URL']}{URL_addon}")
    response = get(f"{_config["base_URL"]}{URL_addon}", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise NetworkError(f"The Brawl Stars API returned status code {response.status_code}")
# Returns ranking for a powrplay season
# Season tags are region spasific
def get_powerplay_season_rankings(region_code: str, season_tag:str, limit:str, return_after:str = "", return_before:str = "", API_key: str = "") -> str:
    from requests import get
    from .errors import NetworkError
    URL_addon = f"{region_code}/powerplay/seasons/{season_tag}?"
    needs_and = False
    if return_after != "" and return_before != "":
        raise ValueError('Use only one of "return_after" or "return_before", not both.')
    elif return_after != "":
        URL_addon += f"after={return_after}"
        needs_and = True
    elif return_before != "":
        if needs_and:
            URL_addon += f"&before={return_before}"
        else:
            URL_addon += f"before={return_before}"
    if needs_and:
        URL_addon += f"&limit={limit}"
    else:
        URL_addon += f"limit={limit}"
    response = get(f"{_config["base_URL"]}{URL_addon}", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise NetworkError(f"The Brawl Stars API returned status code {response.status_code}")