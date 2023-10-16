'''def fun(m):
    if m<=2:return
    fun(m-2)
    fun(m-4)
    print(m)
fun(10)'''

def fun(m):
    if m<=2:
        return m
    return fun(m-4)+fun(m-2)
print(fun(4))