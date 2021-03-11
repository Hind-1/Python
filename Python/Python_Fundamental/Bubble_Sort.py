def Bubble_Sort(arr):
    print(len(arr))
    for i in range(len(arr)) :
        for i in range (0 , len(arr)-i-1):
            # 3-0-1=2
            # 3-1-1=1
            # 3-2-1=0
            if arr[i+1]<arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
print(Bubble_Sort([6,3,0,1,2,4,5]))

