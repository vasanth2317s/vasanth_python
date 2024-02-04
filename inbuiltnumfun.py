   #inbuilt numerical function


import math
print(math.sqrt(145))
#12.041594578792296

print(math.pow(2,7))
#128.0

print(math.exp(2))
#7.38905609893065

print(math.ceil(3.2))
#4

print(math.floor(6.9))
#6

print(round(6.6))
#7

print(math.fabs(-4.6))
#4.6

print(max(3,2,98,87,65))
#98

print(min(3,2,98,87,65))
#2

a=12345
count=0
while a!=0:
    a=a//10
    count+=1
print(count)
#5

b=5498775
c=str(b)
print(len(c))
#7

a=(1,2,7,9,8,6)
print(a[3:5])
#(9,8)

a=(1,3,7,9,8,6)
print(a[::-1])
#(6,8,9,7,3,1)


