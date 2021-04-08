def isvalid(list,number_of_students,mid):
    student=1
    sum=0
    for i in list:
        sum=sum+i
        if sum>mid:
            student=student+1
            sum=i

        if student>number_of_students:
            return False

    return True

def allocate_minimum_pages(list,number_of_students):
    start=max(list)
    end=0

    for i in list:
        end=end+i

    result=-1

    while start<=end:
        mid=(start+end) // 2

        if isvalid(list,number_of_students,mid)==True:
            result=mid
            end=mid-1
        else:
            start=mid+1

    return result


list=[10,20,30,40]
print(allocate_minimum_pages(list,2))