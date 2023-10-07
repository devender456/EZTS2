di={}

maxi=[]
i=0
while(i<4):
    a,b=input().split(':')
    di[a]=int(b)
    i=i+1
for i in di:
    max=0
    while(di[i]!=0):
        rem=di[i]%10
        if rem>max and rem<=len(i):
            max=rem
        di[i]=di[i]//10
    if max!=0:
        maxi.append(i[max-1])
    else:
        maxi.append('X')
print(''.join(maxi))