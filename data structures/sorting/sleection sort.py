def swap(list,a,b):
    if list[a]!=list[b]:
        temp=list[a]
        list[a]=list[b]
        list[b]=temp


def selection_sort(list):
    for i in range(len(list)-1):
        min_index=i
        for j in range(i+1,len(list)):
            if list[j]<list[min_index]:
                min_index=j
        swap(list,i,min_index)
    return list

list=[1,6,3,4,5,3,4,7,9,5,7,3,4,5,8,4,7,0,9,0]
print(selection_sort(list))