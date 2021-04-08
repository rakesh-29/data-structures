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
def nearest_smallest_element_to_left(arr):
    elements=[]
    for i in range(len(arr)):
        if stack1.size()==0:
            elements.append(-1)
        elif stack1.size()>0 and stack1.top()<arr[i]:
            elements.append(stack1.top())
        elif stack1.size()>0 and stack1.top()>=arr[i]:
            while stack1.size()>0 and stack1.top()>=arr[i]:
                stack1.pop()
            if stack1.size()==0:
                elements.append(-1)
            else:
                elements.append(stack1.top())

        stack1.push(arr[i])
    
    return elements

'''



'''
This method is some what more optimized when compared with the previous method in terms of space complexity
'''
def nearest_smallest_element_to_left(arr):
    for i in range(len(arr)):
        if stack1.size()==0:
            stack2.push_back(-1)
        elif stack1.size()>0 and stack1.top()<arr[i]:
            stack2.push_back(stack1.top())
        elif stack1.size()>0 and stack1.top()>=arr[i]:
            while stack1.size()>0 and stack1.top()>=arr[i]:
                stack1.pop()
            if stack1.size()==0:
                stack2.push_back(-1)
            else:
                stack2.push_back(stack1.top())

        stack1.push(arr[i])

    while stack2.size()!=0:
        node=stack2.pop()
        print(node)


stack1=stack()
stack2=stack()

list=[1,3,2,4]
print(nearest_smallest_element_to_left(list))