n = int(input())


acount = 0
dcount = 0

ant = []
dav = []


for i in range(n):
    acount,dcount = input().split()
    if acount ==dcount:
        pass
    elif acount> dcount:
        dav.append(int(acount))
    else:
        ant.append(int(dcount))
    

b= 0
for parts in ant:
    b += parts
print(100-b)
a = 0
for part in dav:
    a +=part
print(100-a)