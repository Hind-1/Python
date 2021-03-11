
def Insertion_Sort(arr):
    for i in range (1,len(arr)):
        index = arr[i]
        # index = arr[1]= 3
        j =i-1
        while j>=0 and index<arr[j]:
            print("time")
            arr[j + 1] = arr[j]
            # arr[1]= 6
            j -= 1
        arr[j + 1] = index
        print("iw")
    return arr
print(Insertion_Sort([6,3]))
