l = int(input())

number = []
character = []
char = ''
num = 0

for i in range(l):
    num,char = input().split()
    number.append(int(num))
    character.append(char)

for x in range(l):
    print(number[x] *character[x])


































'''
l = int(input())
number= []
string = []
num = 0
char = ''
for i in range(l):
    num,char = input().split()
    number.append(int(num))
    string.append(char)

for x in range(l):
    print(number[x]* string[x])''' 