arr=[3,9,-2,8,7,6,3]
idx=[[0,4],[2,5],[0,1],[0,6]]
result=[]
for i in idx:
    sum=0
    for j in range(i[0],i[1]+1):
        sum=sum+arr[j]
    result.append(sum)
print(*result,end='\n')
arr=[3,9,-2,8,7,6,3]
p=[]
for i in range(1,len(arr)):
    arr[i]=arr[i]+arr[i-1]
print(arr)
idx=[[0,4],[2,5],[0,1],[0,6]]
for i in idx:
    k=i[0]
    m=i[1]
    print(arr[m],arr[k])
    p.append(arr[m]-arr[k])
print(p)