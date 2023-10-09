import os

from app.config import Config as AppConfig


class Config(AppConfig):
    DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
    DISCORD_GUILD_ID = os.environ.get("DISCORD_GUILD_ID")
    DISCORD_BOT_ID = os.environ.get("DISCORD_BOT_ID")
    DISCORD_ROLE_IDS = eval(os.environ.get("DISCORD_ROLE_IDS"))
