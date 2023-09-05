import requests
import time

from config.config import Config

# Set your bot token and the ID of the target guild/server


def register():
    # Define the slash command data

    search = {
        "name": "search",
        "description": "Search the Plex library",
        "options": [
            {
                "name": "query",
                "description": "Item title",
                "type": 3,
                "required": True
            },
            {
                "name": "year",
                "description": "The year of the item",
                "type": 4,
                "required": False
            }
        ]
    }

    play_media = {
        "name": "play_media",
        "description": "Play a media item",
        "options": [
            {
                "name": "media_id",
                "description": "The media_id of the item to be played",
                "type": 4,
                "required": False
            }
        ]
    }

    pause = {
        "name": "pause",
        "description": "Pauses playback",
    }

    play = {
        "name": "play",
        "description": "Starts playback",
    }

    queue = {
        "name": "queue",
        "description": "Items in the play queue",
    }

    queue_add = {
        "name": "queue_add",
        "description": "Adds an item to the queue",
        "options": [
            {
                "name": "media_id",
                "description": "The media_id of the item to be added to the queue",
                "type": 4,
                "required": False
            }
        ]
    }

    commands = [
        search, play_media,
        pause, play, queue,
        queue_add
    ]

    # Build the URL for the slash command registration
    url = f"https://discord.com/api/v10/applications/{Config.DISCORD_BOT_ID}/guilds/{Config.DISCORD_GUILD_ID}/commands"

    # Send the GET request to fetch the existing slash commands
    headers = {
        "Authorization": f"Bot {Config.DISCORD_BOT_TOKEN}"
    }

    existing_commands_response = requests.get(url, headers=headers)

    if existing_commands_response.status_code != 200:
        print(
            f"Failed to fetch existing commands. Status code: {existing_commands_response.status_code}")
        print(existing_commands_response.json())
        return

    existing_commands = existing_commands_response.json()
    existing_command_names = {command['name'] for command in existing_commands}

    # print(vars(existing_commands_response))

    # Register new commands
    for command in commands:
        if command['name'] not in existing_command_names:
            response = requests.post(url, json=command, headers=headers)

            # Check if the request was successful
            if response.status_code == 201:
                print(
                    f"Slash command {command['name']} registered successfully!")
            else:
                print(
                    f"Failed to register slash command {command['name']}. Status code: {response.status_code}")
                print(response.json())
        else:
            print(f"Slash command {command['name']} already exists.")
        time.sleep(2)
