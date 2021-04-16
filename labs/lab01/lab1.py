print("заданиэ 2 :")
def a(q=26):
    if q == 1:
        return 1
    if q % 2 == 0:
        if q > 0:
            return q + (q - 1)
        else:
             return print("чо воще те нада")
    if q > 1:
        return 2 * (q - 2)
    else:
       return print("чо воще те нада")
q = int(input("функцыя"))
print(a(q))

print("заданиэ 1")
x = 0
y = 1
z = x + y
 for i in range(10):
    x = x + z
    z = x + z

print("задание 3 ")
n = int(input("число"))
if n == 0:
    x = 1
else:
    for i in range(1,n + 1):
       u = u * i
y = 0
for i in range(n+1):
    y = y + n
print(f"додаваня: { y}")
l = 2
k = 1
while l <= n:
    l *= 2
    k += 1
    o = (k-1) * n
print(f"степень двойки: {o}")

print("задание 4")
s = input("стих")
s = s.lower()
s = s.split(" ")
print(s)
j = input("архив с буквой:")
h = input(" кокой пожелаете второй архив: ")
bukva1 = []
bukva2 = []
for word in s:
    for i in word:
        if i == j:
            bukva1.append(word)
        if i == h:
            bukva2.append(word)

m = len(bukva1)
n = len(bukva2)
if m > n:
    print(f"архив с {j} больше ")
if n > m:
    print(f"архив с {h} больше ")
