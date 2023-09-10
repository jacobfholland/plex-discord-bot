import pytz
from datetime import datetime, timedelta
from plex.client import client
from discord_bot.config import Config


def append_items():
    response = "**QUEUE ITEMS**"
    response += "\n--------------------\n"
    timezone = pytz.timezone(Config.APP_TIMEZONE)
    play_time = datetime.now(timezone)
    for item in client.items:
        runtime = (item.duration - item.viewOffset)
        time_delta = timedelta(milliseconds=runtime)
        response += f"{item.title} ({item.year}) **[{play_time.strftime('%b %d | %I:%M %p %Z')}]**\n"
        play_time = play_time + time_delta
    return response


def append_search(results):
    response = "**SEARCH RESULTS**"
    response += "\n--------------------\n"
    response += "*(use /play command with Media ID to play item)*\n"
    response += "*(use /add command with Media ID to queue item next)*"
    response += "\n--------------------\n"
    for result in results:
        if result.type == "collection":
            continue
        response += f"{result.title} ({result.year}) **[media_id: {result.ratingKey}]**\n"
    return response
