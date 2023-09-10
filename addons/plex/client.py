import time

from plexapi.playqueue import PlayQueue

from app.utils import mask
from addons.plex.config import Config
from addons.plex.log import logger
from addons.plex.plex import plex


def auto_connect():
    logger.debug("Searching for client")
    for client in plex.clients():
        if client.machineIdentifier == Config.PLEX_MACHINE_IDENTIFIER:
            logger.debug(
                f"Client found {mask(client.machineIdentifier)}")
            logger.info(
                f"Connecting to {mask(client.machineIdentifier)}")
            client = client.connect()
            logger.info(
                f"Connected to {mask(client.machineIdentifier)}")
            return client


class Client():
    def __init__(self, obj):
        self.obj = obj

    def request_timeline(self, attempt=1):
        logger.info(f"Requesting timeline (attempt: {attempt})")
        if attempt == Config.PLEX_ATTEMPTS:
            return None
        timeline = self.obj.timeline
        if timeline:
            logger.info(
                f"Timeline retrieved (playQueueID: {timeline.playQueueID})")
            return timeline
        logger.warning(
            f"Timeline request failed, reattempting")
        time.sleep(Config.PLEX_ATTEMPT_TIMEOUT)
        return self.request_timeline(attempt=attempt+1)

    @property
    def queue(self):
        timeline = self.request_timeline()
        if timeline:
            queue = PlayQueue.get(
                plex,
                timeline.playQueueID,
                includeBefore=False
            )
            media = plex.fetchItem(timeline.ratingKey)
            queue.items.insert(0, media)
            return queue
        return None

    @property
    def items(self):
        queue = self.queue
        if queue:
            return queue.items[:Config.PLEX_SEARCH_LIMIT]
        return None

    def add(self, media, next=True):
        queue = self.queue
        queue.addItem(media, playNext=next)
        self.obj.refreshPlayQueue(queue.playQueueID)

    def resume(self):
        return self.obj.play()

    def pause(self):
        return self.obj.pause()

    def next(self):
        return self.obj.skipNext()

    def previous(self):
        return self.obj.skipPrevious()

    def play(self, media):
        self.add(media)
        time.sleep(2)
        self.next()


client = auto_connect()
client = Client(client)
