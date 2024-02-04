a="welcome to python class"
print (a[-1])
print(a*3)

a=[1,2,3,4,5,6,7,8]
print(a[1:])

print(a[:5])

print(a[1:5])

b=['a','b','c',1,2,3,'d','e',5,6]
print(b[2:])
print(b[:7])
print(b[5:10])
a=['abc','1231','aba','323','15a']
b=[]

for i in a:
    if i[0]==i[-1]:
        b.append(i)
print(b)
print(len(b))

#Double Slicing
a=[1,2,3,4,5,6,7,8,9]
a[1:8:2]
a[1:8]
a[1:8:2]

#reversing
a=[1,2,3,4,5,6,7,8,9]
print(a[::-2])
print(a[::-1])

#practice Question
a="Welcome to python Class"
print(a[1:7])
print(a[::-1])
print(a[::-2])
print(len(a))
print(max(a))
print(min(a))
b="a1","A"
print(min(b))

#Built-in function
#strip
a="aaa pyhton aaa"
print(a.strip("a"))
print(a.lstrip("a"))
print(a.rstrip("a"))

#for capitalize
a="hi welcome"
print(a.capitalize())
print(a.title())
print(a.index("w"))

