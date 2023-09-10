from app.config import Config
from app.log import logger
from bot.config import Config as DiscordConfig
from bot.discord import bot

# from plex.plex import plex
# from plex.client import client

logger.info("Starting application")
bot.run(DiscordConfig.DISCORD_BOT_TOKEN)
