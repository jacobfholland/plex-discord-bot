import signal
from multiprocessing import Process

import discord

from addons.discord_bot.config import Config
from addons.discord_bot.log import logger


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
    from addons.discord_bot import commands


import_commands()
