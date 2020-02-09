a = int(input())
b=int(input())
c = int(input())
d = int(input())

if a==b==c==d:
    print("Fish At Constant")

elif a<b<c<d:
    print("Fish Rising")
elif a>b>c>d:
    print("Fish Diving")
else:
    print("No Fish")