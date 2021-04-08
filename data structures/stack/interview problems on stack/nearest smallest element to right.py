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

def nearest_smallest_element_to_right(arr):
    elements=[]
    for i in range(len(arr)-1,-1,-1):
        if stack1.size()==0:
            elements.insert(0,-1)

        elif stack1.size()>0 and stack1.top()<arr[i]:
            elements.insert(0,stack1.top())

        elif stack1.size()>0 and stack1.top()>=arr[i]:
            while stack1.size()>0 and stack1.top()>=arr[i]:
                stack1.pop()

            if stack1.size()==0:
                elements.insert(0,-1)
            else:
                elements.insert(0,stack1.top())


        stack1.push(arr[i])

    return elements

'''





'''
This method is more optimized and the space complexity gets reduced when compared with the other method
'''

def nearest_smallest_element_to_right(arr):
    for i in range(len(arr)-1,-1,-1):
        if stack1.size() == 0:
            stack2.push(-1)
        elif stack1.size() > 0 and stack1.top() < arr[i]:
            stack2.push(stack1.top())
        elif stack1.size() > 0 and stack1.top() >= arr[i]:
            while stack1.size() > 0 and stack1.top() >= arr[i]:
                stack1.pop()

            if stack1.size() == 0:
                stack2.push(-1)
            else:
                stack2.push(stack1.top())

        stack1.push(arr[i])

    while stack2.size()!=0:
        node=stack2.pop()
        print(node)

stack1=stack()
stack2=stack()

array=[1,3,2,4]
print(nearest_smallest_element_to_right(array))