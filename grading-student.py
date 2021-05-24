def student(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            grades[i] = grades[i]
        elif (grades[i]+1)%5 ==0:
            grades[i] = grades[i] +1
        elif (grades[i]+2)%5 == 0:
            grades[i]=grades[i]+2
        else:
            grades[i] = grades[i]
    return grades

mark = (student([4,73,67,38,33]))
print(mark)