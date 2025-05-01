class CheckerAbort(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class CheckerSkip(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
