def kangaroo(x1, v1, x2, v2):
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        print(x1)
        x2+=v2
        print(x2)
    return "NO"

print(kangaroo(14,4,98,2))