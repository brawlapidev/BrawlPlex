# NetworkError is custam error for when the api returns anything but status code 200
class NetworkError(Exception):
    def __init__(self, message:str) -> None:
        self.message = message
        super().__init__(self.message)