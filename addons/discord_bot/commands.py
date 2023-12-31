import discord
from addons.discord_bot.bot import bot
from addons.discord_bot.utils import append_items, append_search
from addons.discord_bot.log import logger
from addons.plex.client import client
from addons.plex.library import Library
from addons.plex.plex import plex
from addons.discord_bot.config import Config


@bot.event
async def on_ready():
    logger.info(f"Plex discord bot has logged in as {bot.user}")


def role_check(func):
    async def wrapper(ctx, *args, **kwargs):
        # Check if the author has any of the specified role IDs
        for role in ctx.author.roles:
            if role.id in Config.DISCORD_ROLE_IDS:
                # Call the original function and pass the ctx along with any other arguments
                await ctx.send("You have the required roles to use this command.")
                await func(ctx, *args, **kwargs)
        # If the author doesn't have any of the specified roles, you can handle it here
        await ctx.send("You don't have the required roles to use this command.")
    return wrapper


@role_check
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


@bot.command(description="Skips to the next media item in queue")
async def next(ctx):
    await ctx.defer()
    try:
        await ctx.respond(f"Skipping to the next queue item")
        client.next()
        response = append_items()
        await ctx.respond(response)
    except Exception as e:
        logger.error(f"An error occurred skiping queue item. {e}")
        await ctx.respond(f"An error occurred skiping queue item. {e}")


@bot.command(description="Skips to the previous media item queue")
async def prev(ctx):
    await ctx.defer()
    try:
        await ctx.respond(f"Skipping to the previous queue item (prev)")
        client.previous()
        client.previous()
        response = append_items()
        await ctx.respond(response)
    except Exception as e:
        logger.error(f"An error occurred skiping queue item. {e}")
        await ctx.respond(f"An error occurred skiping queue item. {e}")
