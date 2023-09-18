tupla = (1, 2, 3, 4, 5, 6, 7, 8)
confirma = True
for n in tupla:
    if n % 2 != 0:
        confirma = False
        
if confirma:
    print("só tem pares")   
else:
    print("tem impares")            