tupla = (1, 55, 22, 6, 86, 2, 21)
confirma = True

for n in tupla:
    if n < 10:
        confirma = False

if confirma == True:
    print('Apenas maiores de 10')
else:
    print('tem menores de 10')    

