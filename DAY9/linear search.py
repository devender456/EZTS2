a=list(map(int,input().split()))
target=int(input())
flag=0
for i in range(len(a)):
    if a[i]==target:
        print(i)
        flag=1
        break
if(flag==0):
    print("element not found")