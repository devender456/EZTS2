n=int(input())
a=97
for i in range(n):
    for j in range(i):
        print(chr(a),end=' ')
        a=a+1
        if a==123:
            a=97
    print()