def last_ocuurance(list,searchnumber):
    left_index=0
    right_index=len(list)-1
    count=0

    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]

        if mid_number==searchnumber:
            count=mid_index
            left_index=mid_index+1

        elif mid_number<searchnumber:
            left_index=mid_index+1

        else:
            right_index=mid_index-1
    
    if count==0:
        print("search number not found in the list")
        return -1

    return count

list=[1,2,2,2,2,2,3,4,5,6,7,8,9,10]
print(last_ocuurance(list,2))