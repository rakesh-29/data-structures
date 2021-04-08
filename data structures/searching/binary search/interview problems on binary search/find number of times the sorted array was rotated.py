def number_of_rotations(list):
    left_index=0
    right_index=len(list)-1
    count=0

    if list[left_index]<list[right_index]:
        return right_index+1


    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]

        n=len(list)

        prev=(mid_index - 1 + n) % n

        next=(mid_index + 1) % n

        if list[prev]>mid_number and list[next]>mid_number:
            count=1

            #temp=len(list)-mid_index

            return mid_index

        elif list[left_index]<mid_number:
            left_index=mid_index+1

        elif list[right_index]>mid_number:
            right_index=mid_index-1

    ''' This was not mandatory optional '''
    if count==0:
        print(" array was not rotated ")
        return len(list)

def solution(list):
    index=number_of_rotations(list)
    numberof_rotations=len(list)-index

    return numberof_rotations

list=[3,4,5,6,1,2]

#list=[1,2,3,4,5,6,7,8,9,10]

'''This code doesn't work for this case where all are of same numbers'''
#list=[3,3,3,3,3,3,3]

print("number of rotations are ",solution(list))