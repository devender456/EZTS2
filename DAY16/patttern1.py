row=6
col=6
for i in range(row):
    for j in range(col):
        if i==j or i+j==row-1:
            print(' ',end=' ')
        elif i==0 or i==6-1 or j==0 or j==6-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()