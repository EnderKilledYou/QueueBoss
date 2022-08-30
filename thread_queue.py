import threading

from cancel_token import CancellationToken


class ThreadedQueue:
    def __init__(self, queue_boss):
        self._queue_boss = queue_boss

    def start(self):
        self._token = CancellationToken()
        self._thread_timer = threading.Thread(target=self._queue_check, )
        self._thread_timer.start()

    def _queue_check(self):
        pass
