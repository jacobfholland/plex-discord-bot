from plexapi.myplex import MyPlexAccount
from plexapi.playqueue import PlayQueue
from app.library import Library

from app.plex import plex
from config.config import Config


def custom_sort_key(url):
    if '127.0' in url:
        return (0, url)
    elif '192.168' in url:
        return (1, url)
    else:
        return (2, url)


class Client:
    def __init__(self) -> None:
        self.client = self.connect_client()

    def connect_client(self):
        print("Logging into Plex account")
        account = MyPlexAccount(Config.PLEX_USERNAME, Config.PLEX_PASSWORD)
        print("Logged in!")
        print("Finding client")
        for device in account.devices():
            if device.clientIdentifier == Config.PLEX_MACHINE_IDENTIFIER:
                print("Connecting to Plex client")
                # print(type(device.connections))
                device.connections = sorted(
                    device.connections, key=custom_sort_key)
                # print(device.connections)
                client = device.connect()
                # print(vars(device))
                print("Connected to Plex client!")
                return client

    def play(self):
        self.client.play()

    def pause(self):
        self.client.pause()

    def stop(self):
        self.client.stop()

    def seek(self, offset):
        # Offset in milliseconds
        self.client.seekTo(offset=offset)

    def next(self):
        self.client.skipNext()

    def previous(self):
        self.client.skipPrevious()

    def skip_to(self, key):
        # Key from media object
        self.client.skipTo(key)

    def step_back(self):
        self.client.stepBack()

    def step_forward(self):
        self.client.stepForward()

    def shuffle(self, shuffle):
        # Shuffle is integer: 0 off, 1 on
        self.client.setShuffle(shuffle)

    def play_media(self, metadata_id, offset=0):
        media = plex.fetchItem(metadata_id)
        self.client.playMedia(media)

    def timeline(self):
        return self.client.timeline

    def is_playing(self):
        # Media is media object
        return self.client.isPlayingMedia()

    def queue(self):
        queue = PlayQueue.get(
            plex,
            self.timeline().playQueueID,
            includeBefore=False
        )
        media = plex.fetchItem(self.timeline().ratingKey)
        queue.items.insert(0, media)
        self.client.refreshPlayQueue(queue.playQueueID)

        return queue

    def queue_items(self):
        queue = self.queue()
        return queue.items[:Config.PLEX_SEARCH_LIMIT]

    def queue_add(self, metadata_id, next=True):
        media = plex.fetchItem(metadata_id)
        queue = self.queue()
        queue.addItem(media, playNext=next)
        self.client.refreshPlayQueue(queue.playQueueID)
        return queue

    def queue_remove(self, metadata_id):
        media = plex.fetchItem(metadata_id)
        queue = self.queue()
        queue.removeItem(media)
        self.client.refreshPlayQueue(queue.playQueueID)
        return queue

    def queue_remove(self, metadata_id):
        media = plex.fetchItem(metadata_id)
        queue = self.queue()
        queue.removeItem(media)
        self.client.refreshPlayQueue(queue.playQueueID)
        return queue

    def queue_move(self, metadata_id):
        # TODO: afterItemID for specifying where to move to
        media = plex.fetchItem(metadata_id)
        queue = self.queue()
        queue.moveItem(media)
        self.client.refreshPlayQueue(queue.playQueueID)
        return queue


client = Client()
