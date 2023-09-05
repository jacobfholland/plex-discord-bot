from config.config import Config
from disc.discord import bot
from register_commands import register
import logging

plexapi_logger = logging.getLogger('plexapi')
plexapi_logger.setLevel(logging.DEBUG)

# register()
bot.run(Config.DISCORD_BOT_TOKEN)
