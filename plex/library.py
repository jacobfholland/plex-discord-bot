from plex.plex import plex
from config.config import Config
from app.log import logger


class Library:
    def __init__(self, obj):
        self.obj = obj

    def search(self, title, **kwargs):
        msg = f"[LIBRARY] Searching (title: {title})"
        if kwargs:
            msg += f" (kwargs: {kwargs})"
        logger.info(msg)
        return self.obj.search(title=title, **kwargs)[:Config.PLEX_SEARCH_LIMIT]
