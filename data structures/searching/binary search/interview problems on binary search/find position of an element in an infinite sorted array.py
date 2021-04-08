def binary_search(list,left_index,right_index,searchnumber):
    count=0
    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]

        if mid_number==searchnumber:
            print("search number found in the list")
            count=1
            return mid_index
        elif mid_number<searchnumber:
            left_index=mid_index+1
        else:
            right_index=mid_index-1

    if count==0:
        print("search number not found in the list")
        return -1

def position_of_an_element(list,searchnumber):
    left_index=0
    right_index=1

    while list[right_index]<searchnumber:
        left_index=right_index
        right_index=right_index * 2
        #print(right_index)

    if list[right_index]==searchnumber:
        print("search number found in the list")
        return right_index
    else:
        return binary_search(list,left_index,right_index,searchnumber)


list=[1,2,3,4,5,6,7,8,9,10]
print(position_of_an_element(list,6))