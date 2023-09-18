tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
pares = ()
for n in tupla:
    if n % 2 == 0:
        pares += (n,)

print(pares)