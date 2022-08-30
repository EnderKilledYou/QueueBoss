from main import QueueBossBase


class DatabaseQueue(QueueBossBase):
    def __init__(self, db):
        super().__init__()
        self._db = db

    def _process(self, job):
        return job(self._db)
