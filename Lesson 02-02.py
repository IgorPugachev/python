x = list(input("Введите какое-нибудь слово "))

y = 0
for i in range(int(len(x) / 2)):
    x[y], x[y + 1] = x[y + 1], x[y]
    y += 2

print(x)