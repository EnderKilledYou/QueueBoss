from thread_job import ThreadJob


class TableThreadJob(ThreadJob):
    def _start(self, id):
        self._id = id
        self._work()

    def _work(self):
        work = get_claimed(self._table_type, self._id)
        self._do_work(work)
        del work

    def _do_work(self, work):
        pass

    def stop(self):
        self._cancel_token.cancel()
        unclaim_table_type(self._table_type, self._id)
