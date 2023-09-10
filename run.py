from config.config import Config
from plex.plex import plex
from bot.discord import bot
from plex.client import client
from register_commands import register


# register()
bot.run(Config.DISCORD_BOT_TOKEN)
