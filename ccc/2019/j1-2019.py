b3=int (input())
b2=int (input())
b1=int (input())

a3=int (input())
a2=int (input())
a1=int (input())

apple_total= (b3*3)+(b2 *2) + (b1*1)
banana_total =  (a3*3)+(a2 *2) + (a1*1)

if banana_total>apple_total:
    print("B")
elif banana_total<apple_total:
    print("A")
elif banana_total==apple_total:
    print("T")