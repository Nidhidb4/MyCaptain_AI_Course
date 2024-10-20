n = int(input("enter the number: ")) 
a = 0
b = 1
i = 2  

print(a)  
print(b)  

while i < n:  
    nextnum = a + b  
    print(nextnum)   
    a = b            
    b = nextnum      
    i += 1           
