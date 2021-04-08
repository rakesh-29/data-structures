import numpy as np
def search(arr,searchnumber):
    i=0
    j=3
    while i>=0 and i<4 and j>=0 and j<4:
        if arr[i][j]==searchnumber:
            print("search number found in the list")
            return searchnumber
        elif arr[i][j]>searchnumber:
            j=j-1
        elif arr[i][j]<searchnumber:
            i=i+1


    if i>3 or j<0:
        print("search number not found in the list")
        return -1

array=np.array([ [10,20,30,40],[15,25,35,45],[27,29,37,45],[32,33,39,50] ])
print(search(array,29))