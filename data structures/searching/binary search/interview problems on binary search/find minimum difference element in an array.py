def floor_of_an_element(list,searchnumber):
    left_index=0
    right_index=len(list)-1

    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]

        if mid_number==searchnumber:
            print("search number found in the list")
            return searchnumber

        elif mid_number<searchnumber:
            left_index=mid_index+1

        else:
            right_index=mid_index-1

    return list[left_index-1]


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

def minimum_difference_element(list,searchnumber):
    number1=floor_of_an_element(list,searchnumber)
    number2=ceil(list,searchnumber)

    count1=searchnumber-number1
    count2=number2-searchnumber

    if count1>count2:
        return number2
    else:
        return number1

list=[1,2,5,6,7,8,9,10]

#print(minimum_difference_element(list,4))
#print(minimum_difference_element(list,3)