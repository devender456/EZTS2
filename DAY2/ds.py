'''nbrs=[1,2,3,4]
def total(nbrs):
    total=0
    for i in nbrs:
        total=total+i
    return total
print(total(nbrs))    '''



def linear(li,target):
    for i in li:
        if i==target:
            print(i)
            return True
    return False
n=int(input())
li=list(map(int,input().strip().split()))[:n]
print(li)
target=int(input())
print(linear(li,target))