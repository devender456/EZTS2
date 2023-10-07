a=[2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
b=[0]*len(a)

result=[0]*len(a)
for i in a:
    b[i] =b[i] + 1
print(b)    
for i in range(1,len(b)):
    b[i]=b[i]+b[i-1]
    print(b)

for i in a:
    b[i]=b[i]-1
    result[b[i]]=i
print(result)