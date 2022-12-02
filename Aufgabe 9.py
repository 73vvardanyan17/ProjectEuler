
liste = []
for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a < b < c and a+ b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                liste.append(a)
                liste.append(b)
                liste.append(c)

print(liste)
print(a*b*c)
