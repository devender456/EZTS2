row=int(input())
col=(2*row)-1
start,end=row-1,row-1
for i in range(row):
    for j in range(col):
        if j>=start and j<=end:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    start=start-1
    end=end+1
    print(start,end)
