from plexapi.server import PlexServer

from config.config import Config


class Plex():
    def __init__(self, obj):
        self.obj = obj


connection = PlexServer(
    baseurl=f"{Config.PLEX_IP_ADDRESS}:{Config.PLEX_PORT}",
    token=Config.PLEX_TOKEN
)
plex = Plex(connection).obj
