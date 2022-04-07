class Queue(object):
    def __init__(self, maxsize=None):
        self.queue = []
        self.maxsize = maxsize

    def __repr__(self):
        return str(self.queue)

    def get_size(self):
        return len(self.queue)

    def is_full(self):
        return len(self.queue) == self.maxsize

    def enqueue(self, data):
        if self.is_full():
            raise IndexError('queue out of space')
        else:
            self.queue.append(data)
            return True

    def dequeue(self):
        if self.get_size() == 0:
            raise IndexError("dequeue from empty queue")

        else:
            return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def contains(self, data):
        return data in self.queue