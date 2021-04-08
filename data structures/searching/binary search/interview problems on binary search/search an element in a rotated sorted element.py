def binary_search(list,left_index,right_index,searchnumber):
   count=0

   while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]

        if mid_number==searchnumber:
            print("search number found in the list")
            count=1
            return searchnumber

        elif mid_number<searchnumber:
            left_index=mid_index+1

        else:
            right_index=mid_index-1

   if count==0:
       print("search number not found in the list")
       return -1


def index(list):
    left_index=0
    right_index=len(list)-1
    mid_index=(left_index+right_index) // 2
    mid_number=list[mid_index]
    count=0

    if list[left_index]<list[right_index]:
        return left_index


    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]

        n=len(list)

        prev=(mid_index - 1 + n) % n

        next=(mid_index + 1) % n

        if list[prev]>mid_number and list[next]>mid_number:
            count=1

            #temp=len(list)-mid_index

            return mid_index

        elif list[left_index]<mid_number:
            left_index=mid_index+1

        elif list[right_index]>mid_number:
            right_index=mid_index-1

    ''' This was not mandatory optional '''
    if count==0:
        print(" array was not rotated ")
        return len(list)

def search_element_in_rotated_sorted_array(list,searchnumber):
    index__=index(list)
    count1=binary_search(list,0,index__-1,searchnumber)
    count2=binary_search(list,index__,len(list)-1,searchnumber)

    if count1>count2:
        return count1
    else:
        return count2

list=[3,4,5,6,7,8,1,2]
print(search_element_in_rotated_sorted_array(list,2))