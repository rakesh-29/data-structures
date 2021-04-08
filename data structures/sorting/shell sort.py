def shell_sort(list):
    size=len(list)
    gap=size // 2

    while gap>0:
        for i in range(gap,len(list)):
            temp=list[i]
            j=i
            while j-gap>=0 and list[j-gap]>temp:
                list[j]=list[j-gap]
                j=j-gap
            list[j]=temp
        gap=gap // 2

    return list

list=[1,6,3,4,3,3,4,6,8,6,7,8,9,0]
print(shell_sort(list))