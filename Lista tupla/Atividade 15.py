tupla = ('banana', 'azul')
teste = input("Digite uma fruta: ")

for n in tupla:
    if n == teste:
        print(tupla.index(n))
