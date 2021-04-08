def swap(list,a,b):
    if list[a]!=list[b]:
        temp=list[a]
        list[a]=list[b]
        list[b]=temp
def horare_partition(list,start,end):
    pivot_index=start
    pivot=list[pivot_index]

    while start<end:
        while start<len(list) and list[start]<=pivot:
            start=start+1
        while list[end]>pivot:
            end=end-1
        if start<end:
            swap(list,start,end)
    swap(list,pivot_index,end)
    return end

def quick_sort(list,start,end):
    if start<end:
        pi=horare_partition(list,start,end)
        quick_sort(list,start,pi-1)
        quick_sort(list,pi+1,end)

    return list

list=[1,5,3,3,4,7,5,6,8,6,7,8,9,0]
start=0
end=len(list)-1
print(quick_sort(list,start,end))