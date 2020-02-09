V = int (input())

votes = input()

A = votes.count("A")
B = votes.count("B")

if A+B==V:
    if A> B:
        print("A")
    else:
        print("B")