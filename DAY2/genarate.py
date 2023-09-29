def generatelist(n):
    table=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(j)
        table.append(row)
    return table
print(generatelist(10))