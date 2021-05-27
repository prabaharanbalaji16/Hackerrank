def miniMaxSum(arr):
    minval=0
    maxval=0
    mini = arr
    mini.sort()
    for i in range(0,len(arr)-1):
        minval +=mini[i]
    maxi = arr
    maxi.sort(reverse=True)
    for i in range(0,len(arr)-1):
        maxval+=maxi[i]
miniMaxSum([3,4,5,2,1])