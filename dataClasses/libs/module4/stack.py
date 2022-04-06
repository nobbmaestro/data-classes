class Stack(object):
    def __init__(self, data=None):
        self.stack = []
        if data:
            self.push(data)

    def __repr__(self):
        return str(self.stack)
    
    def get_size(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.get_size() == 0:
            raise IndexError("pop from empty stack")
        else:
            return self.stack.pop()

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return None

    def contains(self, data):
        return data in self.stack
    