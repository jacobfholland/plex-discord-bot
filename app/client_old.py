class Client:
    def __init__(self) -> None:
        self.client = self.connect_client()

    def client_required(func):
        def wrapper(self, *args, **kwargs):
            if self.client is not None:
                return func(self, *args, **kwargs)
            else:
                print("Error: The client is not found.")
        return wrapper

    @client_required
    def pause(self):
        if self.client:
            self.client.pause()
        print("Client not found")

    @client_required
    def stop(self):
        self.client.stop()

    @client_required
    def seek(self, offset):
        # Offset in milliseconds
        self.client.seekTo(offset=offset)

    @client_required
    def next(self):
        self.client.skipNext()

    @client_required
    def previous(self):
        self.client.skipPrevious()

    @client_required
    def skip_to(self, key):
        self.client.skipTo(key)

    @client_required
    def step_back(self):
        self.client.stepBack()

    @client_required
    def step_forward(self):
        self.client.stepForward()

    @client_required
    def shuffle(self, shuffle):
        # Shuffle is integer: 0 off, 1 on
        self.client.setShuffle(shuffle)

    @client_required
    def play(self, metadata_id, offset=0):
        self.queue_add(metadata_id)
        time.sleep(2)
        self.next()

    @client_required
    def is_playing(self):
        return self.client.isPlayingMedia()

    @client_required
    def timeline(self, attempt=0):
        if self.client.timeline:
            return self.client.timeline
        time.sleep(2)
        return self.timeline(attempt=attempt+1)

    @client_required
    def queue(self):
        timeline = self.timeline()
        if timeline:
            queue = PlayQueue.get(
                plex,
                timeline.playQueueID,
                includeBefore=False
            )
            media = plex.fetchItem(timeline.ratingKey)
            queue.items.insert(0, media)
            self.client.refreshPlayQueue(queue.playQueueID)
            return queue
        return None

    @client_required
    def queue_items(self):
        queue = self.queue()
        if queue:
            return queue.items[:Config.PLEX_SEARCH_LIMIT]
        return None

    @client_required
    def queue_add(self, metadata_id, next=True):
        media = plex.fetchItem(metadata_id)
        queue = self.queue()
        queue.addItem(media, playNext=next)
        self.client.refreshPlayQueue(queue.playQueueID)
        return queue

    @client_required
    def queue_remove(self, metadata_id):
        media = plex.fetchItem(metadata_id)
        queue = self.queue()
        queue.removeItem(media)
        self.client.refreshPlayQueue(queue.playQueueID)
        return queue

    @client_required
    def queue_remove(self, metadata_id):
        media = plex.fetchItem(metadata_id)
        queue = self.queue()
        queue.removeItem(media)
        self.client.refreshPlayQueue(queue.playQueueID)
        return queue

    @client_required
    def queue_move(self, metadata_id):
        # TODO: afterItemID for specifying where to move to
        media = plex.fetchItem(metadata_id)
        queue = self.queue()
        queue.moveItem(media)
        self.client.refreshPlayQueue(queue.playQueueID)
        return queue
