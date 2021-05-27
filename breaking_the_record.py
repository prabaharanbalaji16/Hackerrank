def records(scores):
    worst = scores[0]
    best = scores[0]
    best_count = 0
    worst_count = 0
    for i in range(len(scores)):
        if scores[i]>best:
            best = scores[i]
            best_count+=1
        elif scores[i]< worst:
            worst = scores[i]
            worst_count +=1
records([10 ,5 ,20, 20, 4, 5, 2, 25, 1])