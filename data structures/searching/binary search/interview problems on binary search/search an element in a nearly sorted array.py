def search_in_nearly_sorted_array(list,searchnumber):
    left_index=0
    right_index=len(list)-1
    count=0

    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]

        if left_index<mid_index-1 and list[mid_index-1]==searchnumber:
            count=1
            print("search number found in the list")
            return searchnumber

        elif right_index>mid_index+1 and list[mid_index+1]==searchnumber:
            count=1
            print("search number found in the list")
            return searchnumber

        elif mid_number==searchnumber:
            count=1
            print("search number found in the list")
            return searchnumber

        elif mid_number<searchnumber:
            left_index=mid_index+1

        else:
            right_index=mid_index-1

    if count==0:
        print("search number not found in the list")
        return -1

list=[5,10,20,15]
print(search_in_nearly_sorted_array(list,20))