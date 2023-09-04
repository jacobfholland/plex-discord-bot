import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:

    PLEX_IP_ADDRESS = "http://192.168.0.61"
    PLEX_PORT = "32400"
    PLEX_URL = os.environ.get("PLEX_URL")
    PLEX_TOKEN = os.environ.get("PLEX_TOKEN")
    PLEX_PASSWORD = os.environ.get("PLEX_PASSWORD")
    PLEX_USERNAME = os.environ.get("PLEX_USERNAME")
    PLEX_MACHINE_IDENTIFIER = os.environ.get("PLEX_MACHINE_IDENTIFIER")
    PLEX_SEARCH_LIMIT = int(os.environ.get("PLEX_SEARCH_LIMIT"))

    DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
    DISCORD_GUILD_ID = os.environ.get("DISCORD_GUILD_ID")
    DISCORD_BOT_ID = os.environ.get("DISCORD_BOT_ID")
