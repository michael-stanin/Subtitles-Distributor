from queue import Queue


class SetQueue(Queue):
    def _init(self, maxsize):
        self.queue = set()

    def _put(self, item):
        self.queue.add(item)

    def _get(self):
        return self.queue.pop()

    def to_list(self):
        """
        Returns a copy of all items in the queue without removing them.
        """
        with self.mutex:
            return list(self.queue)
