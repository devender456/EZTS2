
''' # print 1st 10 nbrs

def value(n):
    values=[]
    for i in range(n):
         values.append(i)
    print(values)     
   


n=int(input()) 
value(n) 
x=96707012576812570
print(type(x))   '''



#create one class that consists of three variables you have to take two methods first method is two argumented fuction
# fist one is string type of an argument and inside of the method this string reverse value we have to print square root of 
#integer value
#second method:method name is display results inside we have to len(str) second statement modulo division
# two integer variables  
class a:
    def __init__(self):
        self.x=input("enter the string:")
        self.y=int(input("enter the number:"))
        self.z=int(input("enter the number:"))        
    def reverse(self):
        self.x=self.x[::-1]
        self.y=self.y*self.y
        print(self.y)
    def display_results(self):
        print(self.x)
        print(len(self.x))
        print(self.y%self.z)        
chintu=a()
chintu.reverse()
chintu.display_results()
