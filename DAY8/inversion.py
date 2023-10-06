a=[9,6,8,4,5]
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            count+=1
print(count)
a=list(map(int,input().split()))
print(a)