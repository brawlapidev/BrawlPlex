_config = {
    "URL": "https://api.brawlstars.com/v1/events/rotation"
}
# Returns the event rotation
def get_event_list(API_key) -> str:
    from requests import get
    from .errors import NetworkError
    response = get(f"{_config['URL']}", headers={'Authorization': f'Bearer {API_key}'})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return NetworkError(response.status_code)