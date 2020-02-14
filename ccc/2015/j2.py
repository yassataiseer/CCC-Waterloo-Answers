line = input()

happy = line.count(":-)")
sad = line.count(":-(")

hc = 0
sc = 0

for i in range(len(line)):
    if line[i:i+3] == ":-)":
        hc = hc + 1
    elif line[i:i+3] == ":-(":
        sc = sc + 1

if hc>sc:
    print("happy")
elif hc<sc:
    print("sad")
elif hc==0 and sc==0:
    print("none")
elif hc==sc:
    print("none")

