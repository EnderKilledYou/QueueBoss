import threading

from cancel_token import CancellationToken


class ThreadJob:

    def __init__(self, table_type):
        self.thread = None
        self._table_type = table_type
        self._id = None
        self._cancel_token = CancellationToken()

    def __del__(self):
        self._table_type = None
        self.thread = None

    def start(self):
        threading_thread = threading.Thread(target=self._start)
        threading_thread.start()
        self.thread = threading_thread

    def set_id(self, id):
        self._id = id

    def _start(self):
        pass

    def stop(self):
        self._cancel_token.cancel()
