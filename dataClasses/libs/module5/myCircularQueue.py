class MyCircularQueue(object):
    def __init__(self, k):
        if type(k) != int :
            raise ValueError('arg k is not of type int') 

        elif k <= 0:
            raise ValueError('arg k must be greater than 0')
        
        else:
            self.max_size = k
            self.size = 0
            self.queue = []

    def __repr__(self):
        return str(self.queue)

    def front(self):
        if self.size == 0:
            return -1
        else:
            return self.queue[0]

    def rear(self):
        if self.size == 0:
            return -1
        else:
            return self.queue[self.size - 1]

    def enqueue(self, value):
        if self.size == self.max_size:
            return False
        else:
            self.queue.append(value)
            self.size += 1
            return True

    def dequeue(self):
        if self.size == 0:
            return False
        else:
            self.queue.pop(0)
            self.size -= 1
            return True

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size 


if __name__ == '__main__':
    a = MyCircularQueue(5)
    for i in range(1, 11):
        if i <= 5:
            a.enqueue(i)
        else:
            a.dequeue()
        print(a.is_empty(), a.is_full(), a)

    