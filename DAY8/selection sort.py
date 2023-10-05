a=[19,8,94,2,19,69,1]
for i in range(len(a)):
    min=i
    for j in range(i+1,len(a)):
        if(a[min]>a[j]):
            min=j
    a[min],a[i]=a[i],a[min]
    print(a)
print(a)