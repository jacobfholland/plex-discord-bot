from dotenv import find_dotenv, load_dotenv
from config.config import Config
from app.client import Client
from app.library import Library
from app.plex import plex
from disc.discord import bot
from disc.register_commands import register


register()

# print(vars(Config))

# client = Client()
# client.queue_add(106775, next=False)


# # print(client.queue_items())
# client.queue_items()

# library = Library()
# print(library.search("the omen"))

bot.run(Config.DISCORD_BOT_TOKEN)
