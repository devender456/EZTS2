a=input()
c=0
for i in range(len(a)):
    if(a[i] >= chr(97) and a[i] <= chr(122)) or (a[i] >= chr(65) and a[i] <= chr(90)):
        continue
    else:
        c=i
        break
b=''
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
print(b)