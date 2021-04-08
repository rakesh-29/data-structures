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


def nsl(arr):
    elements=[]
    for i in range(len(arr)):
        if stack1.size()==0:
            elements.append((-1,arr[i]))
        elif stack1.size()>0 and stack1.top()[1]<arr[i]:
            elements.append((stack1.top()[0],arr[i]))
        elif stack1.size()>0 and stack1.top()[1]>=arr[i]:
            while stack1.size()>0 and stack1.top()[1]>=arr[i]:
                stack1.pop()
            if stack1.size()==0:
                elements.append((-1,arr[i]))
            else:
                elements.append((stack1.top()[0],arr[i]))

        stack1.push((i,arr[i]))

    return elements

def nsr(arr):
    elements = []
    temp=len(arr)
    for i in range(len(arr)-1,-1,-1):
        if stack1.size() == 0:
            elements.append((temp, arr[i]))
        elif stack1.size() > 0 and stack1.top()[1] < arr[i]:
            elements.append((stack1.top()[0], arr[i]))
        elif stack1.size() > 0 and stack1.top()[1] >= arr[i]:
            while stack1.size() > 0 and stack1.top()[1] >= arr[i]:
                stack1.pop()
            if stack1.size() == 0:
                elements.append((temp, arr[i]))
            else:
                elements.append((stack1.top()[0], arr[i]))

        stack1.push((i, arr[i]))

    return elements

def solution(array):
    list_of_next_smallest_left=nsl(array)
    list_of_next_smallest_right=nsr(array)   #this is getting wrong  why?
    return list_of_next_smallest_right

'''
    area_list=[]
    #for left1,left2 in list_of_next_smallest_right,list_of_next_smallest_left:
    for i in range(len(array)-1):
        #length=(left1[0]-left2[0])-1
        length=list_of_next_smallest_right[i][0]-list_of_next_smallest_left[i][0]-1
        #area=length * left1[1]
        area=length * list_of_next_smallest_left[i][1]
        area_list.append(area)

    maximum_area=area_list[0]

    for i in range(1,len(array)-1):
        if maximum_area<area_list[i]:
            maximum_area=area_list[i]

    return maximum_area
'''


array=[6,2,5,4,5,1,6]
stack1=stack()
print(solution(array))