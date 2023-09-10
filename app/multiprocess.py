import os
import signal

from app.app import main
from app.log import logger as app_logger
from discord_bot.bot import process as discord_bot_process
from discord_bot.log import logger as discord_logger


def graceful_exit(signum, frame):
    os.kill(discord_bot_process.pid, signal.SIGTERM)
    discord_logger.warning("Stopping discord bot")
    app_logger.warning("Stopping application")


def start_processes():
    signal.signal(signal.SIGINT, graceful_exit)
    signal.signal(signal.SIGTERM, graceful_exit)
    discord_bot_process.start()
    main()
