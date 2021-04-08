def binary_search(list,left_index,right_index,searchnumber):
    count = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]

        if mid_number == searchnumber:
            count=mid_index
            right_index=mid_index-1

        elif mid_number < searchnumber:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return count

def position_of_an_element(list, searchnumber):
    left_index = 0
    right_index = 1

    while list[right_index] < searchnumber:
        left_index = right_index
        right_index = right_index * 2
        # print(right_index)

    return binary_search(list, left_index, right_index, searchnumber)


list = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]
print(position_of_an_element(list, 1))