import os

from app.config import Config as AppConfig


class Config(AppConfig):
    PLEX_IP_ADDRESS = os.environ.get("PLEX_URL")
    PLEX_PORT = int(os.environ.get("PLEX_PORT"))
    PLEX_URL = os.environ.get("PLEX_URL")
    PLEX_TOKEN = os.environ.get("PLEX_TOKEN")
    PLEX_PASSWORD = os.environ.get("PLEX_PASSWORD")
    PLEX_USERNAME = os.environ.get("PLEX_USERNAME")
    PLEX_MACHINE_IDENTIFIER = os.environ.get("PLEX_MACHINE_IDENTIFIER")
    PLEX_SEARCH_LIMIT = int(os.environ.get("PLEX_SEARCH_LIMIT"))
    PLEX_ATTEMPTS = int(os.environ.get("PLEX_ATTEMPTS")) + 2
    PLEX_ATTEMPT_TIMEOUT = int(os.environ.get("PLEX_ATTEMPT_TIMEOUT"))
