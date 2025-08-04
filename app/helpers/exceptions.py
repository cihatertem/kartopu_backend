class NotFoundException(Exception):
    def __init__(self, not_found_name: str) -> None:
        self.not_found_name: str = not_found_name
