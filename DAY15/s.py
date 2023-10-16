x = 'madammadam'
a=[[0] * 10 for _ in range(10)]  
for i in range(len(a)):
    for j in range(i,len(a)):
        if i==j:
            a[i][j]=1
            
        if x[i]==x[j]:
            a[i][j]=1
            print(x[i:j+1])     
print(a)