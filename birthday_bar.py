def birthday_bar(s,d,m):
    count = 0
    if m==1:
        for i in s:
            if i == d:
                count+=1
                return count
    else:
        try:
            for i in range(0,len(s)):
                res = 0
                for j in range(0,m):
                    res = res+s[i+j]
                    if res == d:
                        count+=1
            return count
        except Exception:
            return count

print(birthday_bar([1 ,2, 1, 3, 2],3,2))
# birthday_bar([2 ,5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1,],18,7)
# ReadableBuffer


# count = 0
#     bars=0
#     sumofintegers = d
#     amount = m
#     if len(s) == 1:
#         if s[0] == sumofintegers:
#             count+=1
#         print(count)
#     else:
#         for i in range(0,len(s)-1):
#             bars +=s[i]
#             # if bars >= sumofintegers:
#             #     count+=1
#             #     bars-=sumofintegers
#             # if s[i] + s[i+1] == sumofintegers:
#             #     count+=1
#         print(count)