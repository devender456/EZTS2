def pair_exist(arr,t,i):
    if i==len(arr):
        return -1
    if arr[i]==t:
        return i
    return pair_exist(arr,t,i+1)
a=[-3,8,7,2,5,13,18,9,6]
target=int(input())
print(pair_exist(a,target,0))

