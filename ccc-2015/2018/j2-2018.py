a = int(input())
lineone = input()
linetwo = input()

count = 0 

for i in range(a):
    if lineone[i]=="C"==linetwo[i]:
        count+= 1

print(count)



