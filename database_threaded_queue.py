import os

from database_queue import DatabaseQueue
from thread_queue import ThreadedQueue


class DatabaseThreadedQueue(ThreadedQueue):
    def __init__(self, count=os.cpu_count()):
        super().__init__(DatabaseQueue)
        self._queues = [DatabaseQueue().start()] * count


    def _get_table_claims(self):
        return []

    def _claim_table(self, id):
        return False

    def _queue_check(self):
        for id in self._get_table_claims():
            if self._claim_table(id):
                boss = self._least_busy_boss()
                boss.add_work(id)
