from app.plex import plex
from config.config import Config


class Library:
    def __init__(self) -> None:
        self.library = plex.library

    def search(self, title, **kwargs):
        return self.library.search(title=title, **kwargs)[:Config.PLEX_SEARCH_LIMIT]
