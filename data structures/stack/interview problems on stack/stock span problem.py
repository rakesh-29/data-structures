from collections import deque
class stack:
    def __init__(self):
        self.container=deque()
    def push(self,value):
        self.container.append(value)
    def push_back(self,value):
        self.container.appendleft(value)
    def pop(self):
        return self.container.pop()
    def top(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
    def isempty(self):
        return len(self.container)==0


'''
def stock_span_problem(arr):
    elements=[]
    for i in range(len(arr)):
        if stack1.size()==0:
            elements.append((i,-1))
        elif stack1.size()>0 and stack1.top()[1]>arr[i]:
            elements.append((i,stack1.top()[0]))
        elif stack1.size()>0 and stack1.top()[1]<=arr[i]:
            while stack1.size()>0 and stack1.top()[1]<=arr[i]:
                stack1.pop()

            if stack1.size()==0:
                elements.append((i,-1))
            else:
                elements.append((i,stack1.top()[0]))

        stack1.push((i,arr[i]))

    for index,ngl in elements:
        res=index-ngl
        print(res)

'''




'''
This is one the the most optimised method in terms of space complexity when compare to the previous method
'''
def stock_span_problem(arr):

    for i in range(len(arr)):
        if stack1.size() == 0:
            stack2.push_back((i, -1))
        elif stack1.size() > 0 and stack1.top()[1] > arr[i]:
            stack2.push_back((i, stack1.top()[0]))
        elif stack1.size() > 0 and stack1.top()[1] <= arr[i]:
            while stack1.size() > 0 and stack1.top()[1] <= arr[i]:
                stack1.pop()

            if stack1.size() == 0:
                stack2.push_back((i, -1))
            else:
                stack2.push_back((i, stack1.top()[0]))

        stack1.push((i, arr[i]))

    while stack2.size()>0:
        node=stack2.pop()
        res=node[0]-node[1]
        print(res)



stack1=stack()
stack2=stack()

array=[100,80,60,70,60,75,85]
stock_span_problem(array)