

class TinkoffSyncRESTClient:

    def __init__(self, token: str, is_sandbox: bool = False) -> None:
        self.__token = token
        self.__is_sandbox = is_sandbox

    @property
    def token(self) -> str:
        return self.__token

    @property
    def is_sandbox(self) -> bool:
        return self.__is_sandbox
