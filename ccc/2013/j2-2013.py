a = input()
allow = ("I, O, S, H, Z, X, N")
f = 0
for letters in a:
    if letters != allow:
        pass
    else:
        f+= 1
if f==0:
    print("YES")
else:
    print("NO")