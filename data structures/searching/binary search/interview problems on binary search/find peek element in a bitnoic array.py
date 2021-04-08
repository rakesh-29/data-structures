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
                return mid_number

            elif list[mid_index]>list[mid_index-1]:
                left_index=mid_index+1

            else:
                right_index=mid_index-1


        if mid_index==0:
            if list[0]>list[1]:
                count=1
                return list[0]

            else:
                count=1
                return list[1]

        if mid_index==len(list)-1:

            if list[len(list)-1]>list[len(list)-2]:
                count=1
                return list[len(list)-1]

            else:
                count=1
                return list[len(list)-2]

    if count==0:
        print("peek element not found in the list")
        return -1

list=[1,2,3,4,5,6,7,12,2]
#list=[5,10,20,15]
print(find_peek_element(list))