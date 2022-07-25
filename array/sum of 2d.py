def sumDiagonal(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i][i]
    print(sum)
a = [2,3,4,5],[5,7,8,4],[3,4,1,22]
sumDiagonal(a)