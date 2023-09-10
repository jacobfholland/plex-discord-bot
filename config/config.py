import os

from dotenv import load_dotenv


def load_envs(root_dir='.'):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file == '.env':
                env_file_path = os.path.join(root, file)
                load_dotenv(env_file_path)


load_envs()


class Config:

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

    DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
    DISCORD_GUILD_ID = os.environ.get("DISCORD_GUILD_ID")
    DISCORD_BOT_ID = os.environ.get("DISCORD_BOT_ID")

    LOG_SENSITIVE_DATA = eval(os.environ.get("LOG_SENSITIVE_DATA"))
    LOG_LEVEL = os.environ.get("LOG_LEVEL").upper()

    TIMEZONE = os.environ.get("TIMEZONE")
