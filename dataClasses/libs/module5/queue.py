class Queue(object):
    def __init__(self, maxsize=None):
        self.queue = []
        self.maxsize = maxsize

    def __repr__(self):
        return str(self.queue)

    def get_size(self):
        return len(self.queue)

    def full(self):
        return len(self.queue) == self.maxsize

    def enqueue(self, data):
        if self.full():
            raise ValueError('Queue out of space')
        else:
            self.queue.append(data)
            return True

    def dequeue(self):
        if self.get_size() == 0:
            raise ValueError("Nothing to dequeue")

        else:
            return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def contains(self, data):
        return data in self.queue