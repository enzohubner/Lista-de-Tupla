import operator
tupla = (('Brasil', 295), ('Belgica', 30))
populacao_maior = 0
pais_populoso = ''

for pais, populacao in tupla:
    if populacao > populacao_maior:
        pais_populoso = pais

print(pais_populoso)
