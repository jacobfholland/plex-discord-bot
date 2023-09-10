from datetime import datetime, timedelta

import discord
import pytz
import signal
import os
import time
from discord_bot.config import Config
from discord_bot.log import logger
from plex.client import client
from plex.library import Library
from plex.plex import plex
from multiprocessing import Process


def run_bot():
    def exit(signum, frame):
        # Perform any cleanup
        exit(0)

    signal.signal(signal.SIGTERM, exit)
    logger.info("Starting Discord bot")
    bot.run(Config.DISCORD_BOT_TOKEN)


process = Process(target=run_bot)
bot = discord.Bot()


def import_commands():
    from discord_bot import commands


import_commands()
