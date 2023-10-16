def arr(n):
    if n==1:
        return 1
    return n+arr(n-1)
a=[1,2,3,4]
b=998
print(arr(b)-1)