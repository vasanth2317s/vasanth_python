for i in range (1,5,1):
    for j in range(1,5,1):
        print(i*j,end=" ")
    print() 
    
for i in range (1,6,1)	:
    for j in range(0,i,1):
        print(i*j,end=" ")
    print()          

b=1
while(b<11):
    print(11,"*",b,"=",11*b)
    b=b+1


for s in range(1,9,1):
    print(s,"^","2=",2**s)

a=0   
for i in range(1,11,1):
    a=a+i
print(a)
 
a=5
for i in range(1,50,1):
    a=a^i
    print(a)