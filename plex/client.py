import time
from plexapi.playqueue import PlayQueue
from plex.plex import plex
from app.utils import mask
from config.config import Config
from app.log import logger


def auto_connect():
    logger.debug("[CLIENT] Searching for client")
    for client in plex.clients():
        if client.machineIdentifier == Config.PLEX_MACHINE_IDENTIFIER:
            logger.debug(
                f"[CLIENT] Client found {mask(client.machineIdentifier)}")
            logger.info(
                f"[CLIENT] Connecting to {mask(client.machineIdentifier)}")
            client = client.connect()
            logger.info(
                f"[CLIENT] Connected to {mask(client.machineIdentifier)}")
            return client


class Client():
    def __init__(self, obj):
        self.obj = obj
        self.machine_identifier = self.obj.machineIdentifier

    def request_timeline(self, attempt=2):
        logger.info("[CLIENT] Requesting timeline")
        if attempt == Config.PLEX_ATTEMPTS:
            return None
        timeline = self.obj.timeline
        if timeline:
            logger.info(
                f"[CLIENT] Timeline retrieved (playQueueID: {timeline.playQueueID})")
            return timeline
        logger.warning(
            f"[CLIENT] Requesting timeline request (attempt: {attempt})")
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


connection = auto_connect()
client = Client(connection)
