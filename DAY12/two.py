def two_poin(a,t,b,e):
    if b==e:
        return False
    if a[b]+a[e]==t:
        return True
    if a[b]+a[e]<t:
        return two_poin(a,t,b+1,e)
    if a[b]+a[e]>t:
        return two_poin(a,t,b,e-1)
a=[-3,8,7,2,5,13,18,9,6]
a.sort()
target=int(input())
print(two_poin(a,target,0,len(a)-1))

