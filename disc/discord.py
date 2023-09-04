from datetime import datetime, timedelta
import logging
import discord
from app.library import Library
from app.client import client
from app.plex import plex

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command(description="Searches for media items")
async def search(
    ctx,
    query: discord.Option(str),
    year: discord.Option(int, required=False)
):
    if year:
        results = Library().search(title=query, year=int(year))
    else:
        results = Library().search(title=query)
    response = "**SEARCH RESULTS**:"
    response += "\n--------------------\n"
    response += "*(use /play command with Media ID to play item)*"
    response += "\n--------------------\n"
    for result in results:
        if result.type == "collection":
            continue
        response += f"{result.title} ({result.year}) **[media_id: {result.ratingKey}]**\n"
    await ctx.respond(
        response
    )


@bot.command(description="Plays a media item")
async def play(
    ctx,
    media_id: discord.Option(str)
):
    try:
        media = plex.fetchItem(int(media_id))
        await ctx.respond(f"Playing: {media.title} ({media.year})")
        print("Playback started")
        client.play_media(int(media.ratingKey))
    except Exception as e:
        await ctx.respond(f"An error occurred during playback. {e}")


@bot.command(description="Pauses playback")
async def pause(ctx):
    try:
        await ctx.respond(f"Playback paused")
        print("Playback paused")
        client.pause()
    except Exception as e:
        await ctx.respond(f"An error occurred during pause. {e}")


@bot.command(description="Starts playback")
async def resume(ctx):
    try:
        await ctx.respond(f"Playback paused")
        print("Playback resumed")
        client.play()
    except Exception as e:
        await ctx.respond(f"An error occurred during pause. {e}")


@bot.command(description="Media items in queue")
async def queue(ctx):
    try:
        play_time = datetime.now()
        response = "**QUEUE ITEMS**:"
        response += "\n--------------------\n"
        for item in client.queue_items():
            runtime = (item.duration - item.viewOffset)
            time_delta = timedelta(milliseconds=runtime)
            response += f"{item.title} ({item.year}) **[{play_time.strftime('%b %d - %I:%M %p %Z')}]**\n"
            play_time = play_time + time_delta
        await ctx.respond(response)
    except Exception as e:
        await ctx.respond(f"An error occurred during playback. {e}")


@bot.command(description="Plays a media item")
async def queue_add(
    ctx,
    media_id: discord.Option(str)
):
    try:
        media = plex.fetchItem(int(media_id))
        await ctx.respond(f"Adding to queue (next): {media.title} ({media.year})")
        client.queue_add(int(media.ratingKey))
    except Exception as e:
        await ctx.respond(f"An error occurred during playback. {e}")
