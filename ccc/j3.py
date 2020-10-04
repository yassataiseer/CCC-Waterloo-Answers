def test(a):
  first = []
  secound = []
  for i in range(a):
    x = input()
    fir,sec=x.split(",")
    first.append(fir)
    secound.append(sec)
  first_1 = min(first) 
  first_1 = int(first_1) - 1
  secound_1 = min(secound) 
  secound_1 = int(secound_1) - 1
  first_2 = max(first)
  first_2 = int(first_2) + 1
  secound_2 = max(secound)
  secound_2 = int(secound_2) + 1
  answer1 = str(first_1)+","+ str(secound_1)
  answer2 = str(first_2) + "," + str(secound_2)
  print(answer1)
  print(answer2)
  

a = int(input())
test(a)
