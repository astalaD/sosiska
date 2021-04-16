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
