# def Da(x):
#     return x - 15

# a = Da(20)
# print(a)

# def Da(x = 20):
#     return x - 15
# a = Da(20)
# print(a)

# def func(x,y):
#     return x**2 + y**2
# func = lambda x,y : x**2 + y**2


# def func(x,y,z=7):
#     return x+y+z
# print(func(y=12,x=333))


s = '19/5544  6521/1449  3580/2984  5984/6164  2583/9588  3467/1440  8636/7706  8023/6847  6023/570  1545/7361  5893/4221  5994/3118  5054/1547  4062/780  3433/6926  2390/3702  6714/2278  7180/9156  3466/2294  8733'
s = s.split("/")
num = int(s[0])
s.pop(0)
n1 = []
n2 = []
mass = []
r1 = ""
r2 = ""
a = 0
dif = []
for i in s:
    i = i.split("  ")
    n1.append(i[0])
    n2.append(i[1])
for i in range(num):
    if int(n1[i]) > int(n2[i]):
        dif.append(int(n1[i]) - int(n2[i]))
        mass.append(int(n2[i]))
    else:
        dif.append(int(n2[i]) - int(n1[i]))
        mass.append(int(n1[i]))
dif = sorted(dif)
for i in dif:
    if i % 2 == 1:
        dif = i
        break
summ = sum(mass)
if summ % 2 == 0:
    r1 = "+"
else: r1 = "-"
for i in mass:
    if i%2==0:
        a+=1
    else: a -=1
if a>0:
    r2 = "+"
elif a<0:
    r2 = "-"
else: r2 = "ЧОЗАХУЙНЯБЛЯТЬ?"
if r1==r2:
    print(summ)
else:
    print(summ+dif)
