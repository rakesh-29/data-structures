def first_ocuurance(list,searchnumber):
    left_index=0
    right_index=len(list)-1
    count=0

    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]
        if mid_number==searchnumber:
            count=mid_index
            right_index=mid_index-1
        elif mid_number<searchnumber:
            left_index=mid_index+1
        else:
            right_index=mid_index-1

    if count==0:
        print("search number not found in the list")
        return -1

    return count

def last_ocuurance(list, searchnumber):
    left_index = 0
    right_index = len(list) - 1
    count = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]

        if mid_number == searchnumber:
            count = mid_index
            left_index = mid_index + 1

        elif mid_number < searchnumber:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1

    if count == 0:
        print("search number not found in the list")
        return -3

    return count

def count_of_an_element(list,searchnumber):
    index_of_first_occurance=first_ocuurance(list,searchnumber)
    index_of_last_occurance=last_ocuurance(list,searchnumber)

    count=(index_of_last_occurance-index_of_first_occurance) + 1
    return count


list=[1,2,2,2,2,2,3,4,5,7,8,9,10]

'''
These are the three different cases :-

In case-1:- The element 6 was not found in the list so in that case i need to return -1 whereas

In case-2:- The element 1 was present so i need to return 1

In case-3:- The element 2 was found 5 times so first finding firstocuurance of 2 and then finding last
             Occurance of 2 and then returning count
'''
#print(count_of_an_element(list,6)) # case-1
#print(count_of_an_element(list,1)) #case-2
#print(count_of_an_element(list,2)) #case-3