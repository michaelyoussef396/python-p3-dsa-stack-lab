class Stack:

    def __init__(self, items=None, limit=1000):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) >= self.limit:
            raise Exception("Stack is full")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None  # Return None if stack is empty
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        return self.isEmpty()

    def full(self):
        return len(self.items) == self.limit

    def search(self, value):
        try:
            return len(self.items) - 1 - self.items[::-1].index(value)
        except ValueError:
            return -1
