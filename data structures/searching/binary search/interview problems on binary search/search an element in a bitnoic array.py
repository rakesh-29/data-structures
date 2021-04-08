def binary_search(list,left_index,right_index,searchnumber):
   count=0
   while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]
        if mid_number==searchnumber:
            #print("search number found in the list")
            count=1
            return searchnumber

        elif mid_number<searchnumber:
            left_index=mid_index+1
        else:
            right_index=mid_index-1

   if count==0:
        #print("search number not found in the list")
        return -1



def find_peek_element(list):
    left_index=0
    right_index=len(list)-1
    count=0

    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]
        if mid_index>0 and mid_index<len(list)-1:

            if list[mid_index-1]<list[mid_index] and list[mid_index]>list[mid_index+1]:
                count=1
                return mid_index

            elif list[mid_index]>list[mid_index-1]:
                left_index=mid_index+1

            else:
                right_index=mid_index-1


        if mid_index==0:
            if list[0]>list[1]:
                count=1
                return 0

            else:
                count=1
                return 1

        if mid_index==len(list)-1:

            if list[len(list)-1]>list[len(list)-2]:
                count=1
                return len(list)-1

            else:
                count=1
                return len(list)-2

    if count==0:
        print("peek element not found in the list")
        return -1


def search_an_element(list,searchnumber):
    index=find_peek_element(list)
    left=binary_search(list,0,index,searchnumber)
    right=binary_search(list,index+1,len(list)-1,searchnumber)

    if left>right:
        return left
    else:
        return right


list=[1,2,3,5,6,7,12,2]
#list=[5,10,20,15]
print(search_an_element(list,4))