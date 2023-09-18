tupla = (1, 2, 2, 3, 3, 4, 5, 6, 7)
tupla_teste = ()

for n in tupla:
    if n not in tupla_teste:
        tupla_teste += (n,)

print(tupla_teste)