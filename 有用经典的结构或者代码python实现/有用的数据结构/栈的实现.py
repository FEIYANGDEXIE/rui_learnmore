class Stack(object):
    def __init__(self):
        self.__stack = []

    def push(self, data):
        self.__stack.append(data)

    def is_empty(self):
        return True if len(self.__stack) == 0 else False

    def get_size(self):
        return len(self.__stack)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def top(self):
        if not self.is_empty():
            return self.__stack[-1]
        else:
            raise IndexError("stack is empty")

a=Stack()
a.push('1')
a.push(2)
a.push(3)
print(a.pop())
print(a.top())

