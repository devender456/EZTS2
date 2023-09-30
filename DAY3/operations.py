'''#in the given array nbr occurs twice only one nbr occurs one time
a=[1,2,1,2,4,]
num=0
for i in a:
    num=num^i
print(num)   '''

'''#swap 2 nbrs using xor
a=100
b=200
a=a^b
b=b^a
a=a^b
print(a)
print(b)'''


''''# for given nbr n check the kth bit is set or not
n=10
k=2
result=n&(1<<k-1)
print(result)
if result==0:
    print(no )
else:
    print(yes)    '''



'''# print xor of all nbrs
#o(n)
n=int(input())
j=0
for i in range(1,n+1):
    j=j^i
print(j) 

#o(1)
if(n%4==0):
    print(n)
elif(n%4==1):
    print(1)
elif(n%4==3):
    print(n+1)
elif(n%4==3):
    print(0)  '''



# find the all xor of given nbrs within the range
ll=int(input())
ul=int(input())
j=0
for i in range(li,ul+1):
    j=(j^i)^(j^(ll-ul))
print(j)


