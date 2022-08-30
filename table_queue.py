import os

from thread_queue import ThreadedQueue


class TableQueue(ThreadedQueue):
    def __init__(self, queue_boss, count=os.cpu_count()):
        super().__init__(queue_boss)
        self._queues = [queue_boss().start()] * count

    def _least_busy_boss(self):
        return self._queues.sort(key=lambda x: x.count())[0]

    def _get_table_claims(self):
        return []

    def _claim_table(self, id):
        return False

    def _queue_check(self):
        for id in self._get_table_claims():
            if self._claim_table(id):
                boss = self._least_busy_boss()
                boss.add_work(id)
