def linear_search(list,searchnumber):
    count=0
    for i in list:
        if i==searchnumber:
            print("search number found in the list")
            count=1
            return searchnumber
    if count==0:
        print("search number not found in the list")
        return 0

list=[1,2,3,4,5,6,7,8,9,10]
print(linear_search(list,10))