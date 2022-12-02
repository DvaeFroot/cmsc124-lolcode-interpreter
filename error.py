class Error(Exception):
    def __init__(self, token, cause) -> None:
        self.token = token
        self.cause = cause

    def __repr__(self) -> str:
        return f'Error at {self.token}: {self.cause}'

    def __str__(self) -> str:
        return f'Error at {self.token}: {self.cause}'