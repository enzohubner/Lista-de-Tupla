import operator
datas = ((12, 4, 2020), (5, 11, 2019), (1, 1, 2022), (15, 8, 2021))

datas_ordenadas = sorted(datas, key=operator.itemgetter(2, 1, 0))

for n in datas_ordenadas:
    print(n)