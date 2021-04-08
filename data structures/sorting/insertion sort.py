def insertion_sort(list):
    for i in range(1,len(list)):
        temp=list[i]
        j=i-1
        while j>=0 and list[j]>temp:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=temp

    return list

list=[1,6,4,5,3,2,3,5,6,7,9,0]
print(insertion_sort(list))