#setfunctions

a={'red','blue','green'}
print(a)
a.add("yellow")
print(a)

b={'white',"black"}
print(a.update(b))
print(a)

c={'vasanth','mano','yuvan'}
d={'vasanth','mano','dinesh'}
e=c^d
print(e)

c={'vasanth','mano','yuvan'}
d={'vasanth','mano','dinesh'}
e=c|d
print(e)

c={'vasanth','mano','yuvan'}
d={'vasanth','mano','dinesh'}
e=c&d
print(e)

c={'vasanth','mano','yuvan'}
d={'vasanth','mano','dinesh'}
e=c-d
print(e)

a=[1,2,1,5,2,8]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)     

a=[1,2,1,5,2,8]
b=sorted(list(set(a)))
print(b)

a={"id":1,"name":"abc"}
print(a["name"])
a["id"]=21
print(a)
b={"age":21,"course":"python"}
a.update(b)
print(a)
print(a.items())
print(a.pop("id"))
print(a)

print(a.popitem())
print(a)

print(a.clear())
print(a)

del a["name"]
print(a)
