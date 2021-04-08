def merge_sort(list):
    if len(list)<=1:
        return

    size=len(list)
    mid=size // 2
    left=list[:mid]
    right=list[mid:]

    merge_sort(left)
    merge_sort(right)
    return merge_two_lists(list,left,right)
def merge_two_lists(list,a,b):
    len_a=len(a)
    len_b=len(b)
    i=j=k=0

    while i<len_a and j<len_b:
        if a[i]<b[j]:
            list[k]=a[i]
            i=i+1
            k=k+1
        else:
            list[k]=b[j]
            j=j+1
            k=k+1

    while i<len_a:
        list[k]=a[i]
        i=i+1
        k=k+1

    while j<len_b:
        list[k]=b[j]
        j=j+1
        k=k+1
    return list

list=[1,6,4,5,3,2,3,5,7,8,9,0]
print(merge_sort(list))