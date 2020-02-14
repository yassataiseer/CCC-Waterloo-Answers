

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
for i in range(1):
    a,b,c,d = input().split()
    e,f,g,h = input().split()
    i,j,k,l = input().split()
    m,n,o,p = input().split()

r1 = int(a)+int(b)+int(c)+int(d)
r2 = int(e)+int(f)+int(g)+int(h)
r3 = int(i)+int(j)+int(k)+int(l)
r4 = int(m)+int(n)+int(o)+int(p)

c1 = int(a)+int(e)+int(i)+int(m)
c2 = int(b)+int(f)+int(j)+int(n)
c3 = int(c)+int(g)+int(k)+int(o)
c4 = int(d)+int(h)+int(l)+int(p)




if r1==r2==r3==r4:
    if c1==c2==c3==c4:
        print("magic")
else:
   print("not magic")

