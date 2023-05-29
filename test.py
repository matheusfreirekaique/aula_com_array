import random

lista = []

n = int(input('insira a quantidade de nuemeros: '))

for i in range(0,n):
    aleatoriro = int(random.random() * 100)
    lista.append(aleatoriro)
    
print(lista)