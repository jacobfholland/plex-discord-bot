from datetime import datetime
from config.config import Config
# from app.plex import plex
from plexapi.myplex import MyPlexAccount

IGNORED_KEYS = ["screenResolution", "screenDensity", "provides"]
account = MyPlexAccount(Config.PLEX_USERNAME, Config.PLEX_PASSWORD)
response = "CLIENT LIST (ordered by Last Seen)"
response += "\n--------------------\n"
print(response)

devices = account.devices()
devices.sort(key=lambda device: device.lastSeenAt, reverse=True)

for device in devices:
    max_key_length = max(
        len(key)
        for key in device.__dict__.keys()
        if not key.startswith("_")
    )

    for key, value in device.__dict__.items():
        if key.startswith("_") or key in IGNORED_KEYS:
            continue
        if not value:
            continue
        if isinstance(value, (str, int, float)):
            print(f"{key.ljust(max_key_length)}: {value}")
        elif isinstance(value, list):
            print(f"{key.ljust(max_key_length)}: {', '.join(value)}")
        elif isinstance(value, datetime):
            print(
                f"{key.ljust(max_key_length)}: {value.strftime('%Y-%m-%d %H:%M:%S')}")
        elif hasattr(value, '__class__'):
            print(f"{key.ljust(max_key_length)}: {value.__class__.__name__}")
        else:
            print(f"{key.ljust(max_key_length)}: {value}")
    print("\n")


# print(type(account._server))
