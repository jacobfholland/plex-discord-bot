from plexapi.server import PlexServer

from config.config import Config

plex = PlexServer(
    baseurl=f"{Config.PLEX_IP_ADDRESS}:{Config.PLEX_PORT}",
    token=Config.PLEX_TOKEN
)