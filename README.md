# plex-discord-bot

## Installation
After cloning the repository navigate to the project directory

- Create a Discord application. Review the Discord documentation for mor information about [creating an application](https://discord.com/developers/docs/getting-started).

- Install PIP requirements
```
pip install -r requirements.txt
```

- Set your environment variables
    - You can modify the name of `.env-example` to `.env` and use it as a template
    - You can create your own `.env` file
    - See [environment variables](#environment-variables) for more info

- Run the application
```
python3 run.py
```

- Invite the Discord bot. The invite URL can be found in your Discord [developer portal](https://discord.com/developers/applications/) under *OAuth2->URL Generator*. Select *bot* and then whatever required permissions that are applicable to your requirements. 

After installing, you will only ever need to use `python3 run.py` to run the bot. You **do not** need to create an application and invite every time you launch.
## Commands
- `/search <title> <year(opt)>` 
    - Search for media items in the library. Will return a set of results that include media_ids which can be used in other commands.
- `/queue` 
    - Get the current queue and the play times of each item in the queue
- `/play <media_id>` 
    - Plays the media item
- `/add <media_id>` 
    - Add a media item next in the queue
- `/pause` 
    - Pauses playback
- `/resume` 
    - Resumes play back

## Environment Variables
TODO: Environment variables will not-reset themselves if they already exist at run time. Allowing people passing them through a Docker container or other methods to set them out-side of the *.env* file
#### APP
- `APP_NAME` *(str)*
    - The name of your application
- `APP_TIMEZONE` *(str)*
    - Timezone to be used for time related functionality

#### LOG
- `LOG_SENSITIVE_DATA` *(bool)*
    - Determines if sensitive data like machine identifiers and IP addresses display in the logs
- `LOG_LEVEL` *(str) [debug | info | warning | critical | error]*
    - Console and logging level
- `LOG_PATH` *(str)*
    - Path location where log output is stored

#### PLEX
- `PLEX_URL`
    - The URL of your plex server. Including HTTP/HTTPS protocal. (Ex http://192.168.0.69)
- `PLEX_PORT` *(int)*
    - Port for the plex server
- `PLEX_TOKEN` *(str)*
    - Plex server authentication token. To find this see obtaining a [Plex Token](#)
- `PLEX_MACHINE_IDENTIFIER` *(str)*
    - Plex client machine identifier (client identifier). To find this see obtaining a [Machine Identifier](#). A machine identifier is a unique ID for the plex client you are controlling.
- `PLEX_USERNAME` *(str)*
    - Plex username
- `PLEX_PASSWORD` *(str)*
    - Plex password
- `PLEX_SEARCH_LIMIT` *(int)*
    - The number of results to be returned when running commands that return multiple records, such as */search* and */queue*. Discord has a 2,000 character limit. Keep that in mind when setting this value.
- `PLEX_ATTEMPTS` *(int)*
    - Due to some weird Plex API quirks occasionally multiple request attempts must be made for a successful data response. This should usually not require more than 3.
- `PLEX_ATTEMPT_TIMEOUT` *(int)*
    - The timeout between *PLEX_ATTEMPTS* in seconds. Usually 1 second is fine. You may need 2 seconds if you are noticing significant failures.

#### DISCORD
- `DISCORD_BOT_TOKEN` *(str)*
    - Discord bot token found on your Discord [developer portal](https://discord.com/developers/applications/)
- `DISCORD_BOT_ID` *(int)*
    - Discord bot ID (application ID) found on your Discord [developer portal](https://discord.com/developers/applications/)
- `DISCORD_GUILD_ID` *(int)*
    - The Discord server ID. You can right click the server and select *Copy Server ID*
