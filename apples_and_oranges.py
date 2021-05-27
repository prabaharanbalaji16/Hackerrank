def countApplesAndOranges(s, t, a, b, apples, oranges):
    aplcount=0
    orgcount = 0
    for apple in range(len(apples)):
        apples[apple]=a+apples[apple]
    for orange in range(len(oranges)):
        oranges[orange]=b+oranges[orange]
    
    for apple in apples:
        if apple >= s and apple <=t:
            aplcount+=1
    for orange in oranges:
        if orange >= s and orange <=t:
            orgcount+=1
    print(aplcount)
    print(orgcount)

print(countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6]))