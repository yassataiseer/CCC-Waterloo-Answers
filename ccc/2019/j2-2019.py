l = int (input())

char = ''
num = 0

number = []
string = []
for i in range(l):
    num,char = input().split()
    number.append(int(num))
    string.append(char)


for x in range(l):
    print(number[x]*string[x])


