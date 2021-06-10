def sumpair(ar,k,n):
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            num = ar[i]+ar[j]
            if num % k ==0:
                count+=1
    print(count)
sumpair([1,3,2,6,1,2],3,6)
