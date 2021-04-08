def swap(list,a,b):
    if list[a]!=list[b]:
        temp=list[a]
        list[a]=list[b]
        list[b]=temp


def lomuto_partition(list,start,end):
    pivot_index=end
    pivot=list[pivot_index]
    pindex=start

    for i in range(start,end):
        if list[i]<=pivot:
            swap(list,i,pindex)
            pindex=pindex+1
    swap(list,pindex,end)
    return pindex
def quick_sort(list,start,end):
    if start<end:
        pi=lomuto_partition(list,start,end)
        quick_sort(list,start,pi-1)
        quick_sort(list,pi+1,end)
    return list

list=[1,9,2,5,3,5,7,8,5,6,7,9,0]
start=0
end=len(list)-1
print(quick_sort(list,start,end))