def binary_search(list,searchnumber):
    left_index=0
    right_index=len(list)-1
    count=0

    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]
        if mid_number==searchnumber:
            print("search number found in the list")
            count=1
            return mid_number
        elif mid_number<searchnumber:
            right_index=mid_index-1
        else:
            left_index=mid_index+1

    if count==0:
        print("search number not found in the list")
        return -1
list=[10,9,8,7,6,5,4,3,2,1,0]
print(binary_search(list,8))