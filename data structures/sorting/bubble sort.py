def bubble_sort(list):
    size=len(list)

    for i in range(size-1):
        count=0
        for j in range(size-i-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                count=1

        if count==0:
            break

    return list

list=[1,6,4,2,3,4,6,4,6,7,8,9,0]
print(bubble_sort(list))