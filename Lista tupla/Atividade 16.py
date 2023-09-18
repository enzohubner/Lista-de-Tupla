tupla1 = (1, 2, 3, 4)
tupla2 = (1, 2, 3, 4)
tupla3 = tuple()


if len(tupla1) == len(tupla2):
    for n in range(len(tupla1)):
        soma = tupla1[n] + tupla2[n]
        tupla3 += (soma,)

print(tupla3)        