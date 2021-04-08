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
            left_index=mid_index+1

        else:
            right_index=mid_index-1

    if count==0:
        print("search number not found in the list")
        return 0

list=[1,2,3,4,5,6,7,8,9,10]
searchnumber=8
print(binary_search(list,searchnumber))