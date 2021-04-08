from collections import deque

class queue:

    def __init__(self):
        self.buffer=deque()

    def enque(self,value):
        self.buffer.appendleft(value)

    def deque(self):
        return self.buffer.pop()

    def peek(self):
        return self.buffer[-1]

    def size(self):
        return len(self.buffer)

    def isempty(self):
        return len(self.buffer)==0

q=queue()
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
q.enque(6)
q.enque(7)
q.enque(8)
print(q.peek())