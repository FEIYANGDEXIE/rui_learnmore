class Queen(object):
    def __init__(self):
        self.__queen = []

    def push(self, data):
        self.__queen.append(data)

    def is_empty(self):
        return True if len(self.__queen) == 0 else False

    def get_size(self):
        return len(self.__queen)

    def pop(self):
        if not self.is_empty():
            return self.__queen.pop(0)
        else:
            raise IndexError("pop from empty stack")

    def top(self):
        if not self.is_empty():
            return self.__queen[0]
        else:
            raise IndexError("stack is empty")

a=Queen()
a.push(6)
a.push(2)
a.push(5)
a.push(3)
print(a.pop())
print(a.top())