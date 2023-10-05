def quicksort(a):
    if(len(a)<1):
        return a
    pv=a[0]
    left=[i for i in a if i<pv]
    right=[i for i in a if i>pv]
    return quicksort(left)+[pv]+quicksort(right)
a=[12,45,6,89,2,32,21]
print(quicksort(a))
