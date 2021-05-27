def cake(candles):
    count= 1
    candles.sort(reverse=True)
    for i in range(1,len(candles)):
        if candles[0] == candles[i]:
            count+=1
    print(count)

cake([2,4,5,2,5])