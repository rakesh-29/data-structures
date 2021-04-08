from collections import deque

class stack:
    def __init__(self):
        self.container=deque()
    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def isempty(self):
        return len(self.container)==0

s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
print(s.peek())