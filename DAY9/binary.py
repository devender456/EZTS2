def binary(a,begin,end,target):
    if begin<=end:
        mid=(begin+end)//2
        if target==a[mid]:
            return mid
        if target<a[mid]:
            return binary(a,begin,mid-1,target)
        elif target>a[mid]:
            return binary(a,mid+1,end,target)
    else:
        return False


a=[1,2,4\,5,6,7,8,109]
target=109
b=binary(a,0,len(a)-1,target)
print(b)