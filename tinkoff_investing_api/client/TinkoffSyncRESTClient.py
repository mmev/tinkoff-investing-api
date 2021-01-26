

class TinkoffSyncRESTClient:

    def __init__(self, token: str) -> None:
        self.__token = token

    @property
    def token(self) -> str:
        return self.__token
