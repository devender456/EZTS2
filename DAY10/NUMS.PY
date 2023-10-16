a=list(map(int,input().split()))
sum=0
st=''
i=0
while(i<len(a)):
    if a[i]==4:
        while(a[i]!=7):
            st=st+str(a[i])
            i=i+1
        st=st+str(a[i])
        i=i+1
    else:
        sum=sum+a[i]
        i=i+1
print(sum+int(st))

