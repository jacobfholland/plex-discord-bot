from config.config import Config
from app.plex import plex
from disc.discord import bot
from app.client import client
from register_commands import register


# register()
bot.run(Config.DISCORD_BOT_TOKEN)
