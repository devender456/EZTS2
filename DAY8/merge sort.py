def mergesort(a):
    if len(a)>1:
        mid=len(a)//2
        left=a[:mid]
        print(left)
        right=a[mid:]
        print(right)
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                a[k]=left[i]
                i += 1
                k += 1
            else:
                a[k]=right[j]
                j += 1
                k += 1
        while(i<len(left)):
            a[k]=left[i]
            i=i+1
            k=k+1
        while(j<len(right)):
            a[k]=right[j]
            j=j+1
            k=k+1
a=[12,45,6,89,2,32,21]
mergesort(a)
print(a)