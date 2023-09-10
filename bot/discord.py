from datetime import datetime, timedelta

import discord
import pytz

from bot.config import Config
from bot.log import logger
from plex.client import client
from plex.library import Library
from plex.plex import plex

bot = discord.Bot()


@bot.event
async def on_ready():
    logger.info(f"Plex Discord Bot has logged in as {bot.user}")


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


@bot.command(description="Media items in queue")
async def queue(ctx):
    await ctx.defer()
    try:
        response = append_items()
        logger.info(
            f"Queue retrieved")
        await ctx.respond(response)
    except Exception as e:
        logger.error(f"An error occurred retrieving the queue: {e}")
        await ctx.respond(f"An error occurred retrieving the queue: {e}")


@bot.command(description="Searches for media items")
async def search(
    ctx,
    title: discord.Option(str),
    year: discord.Option(int, required=False)
):
    await ctx.defer()
    try:
        if year:
            results = Library(plex.library).search(title=title, year=int(year))
        else:
            results = Library(plex.library).search(title=title)
        response = append_search(results)
        msg = f"Search results retrieved {len(results)} (title: {title})"
        if year:
            msg += f" (year: {year})"
        logger.info(msg)
        await ctx.respond(response)
    except Exception as e:
        logger.error(f"An error occurred attempting search: {e}")
        await ctx.respond(f"An error occurred attempting search: {e}")


@bot.command(description="Pauses playback")
async def pause(ctx):
    await ctx.defer()
    try:
        await ctx.respond(f"Playback paused")
        logger.info("Playback paused")
        client.pause()
    except Exception as e:
        logger.error(f"An error occurred attempting pause: {e}")
        await ctx.respond(f"An error occurred attempting pause: {e}")


@bot.command(description="Plays a media item")
async def play(
    ctx,
    media_id: discord.Option(str)
):
    await ctx.defer()
    try:
        media = plex.fetchItem(int(media_id))
        await ctx.respond(f"Playing: {media.title} ({media.year})")
        logger.info(
            f"Playback started (media_id: {media.ratingKey}) (title: {media.title} (year: {media.year}))")
        if media:
            client.play(media)
        await ctx.respond(f"Added to queue")
    except Exception as e:
        logger.error(f"An error occurred attempting playback:{e}")
        await ctx.respond(f"An error occurred attempting playback:{e}")


@bot.command(description="Starts playback")
async def resume(ctx):
    await ctx.defer()
    try:
        await ctx.respond(f"Playback resumed")
        logger.info("Playback resumed")
        client.resume()
    except Exception as e:
        logger.error(f"An error occurred attempting resume: {e}")
        await ctx.respond(f"An error occurred attempting resume: {e}")


@bot.command(description="Plays a media item")
async def add(
    ctx,
    media_id: discord.Option(str)
):
    await ctx.defer()
    try:
        media = plex.fetchItem(int(media_id))
        await ctx.respond(f"Adding to queue (next): {media.title} ({media.year})")
        client.add(media)
        response = append_items()
        await ctx.respond(response)
    except Exception as e:
        logger.error(f"An error occurred adding queue item. {e}")
        await ctx.respond(f"An error occurred adding queue item. {e}")