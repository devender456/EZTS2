arr=[2,3,7,6,0]
for i in range(len(arr)):
    if i in arr:
        continue
    else:
        print(i)
        break