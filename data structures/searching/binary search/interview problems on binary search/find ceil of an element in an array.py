def ceil(list,searchnumber):
    left_index = 0
    right_index = len(list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]

        if mid_number == searchnumber:
            print("search number found in the list")
            return searchnumber

        elif mid_number < searchnumber:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1

    return list[left_index]

list = [1, 2, 4, 5, 6, 7, 8, 91, 10]
print(ceil(list,3))