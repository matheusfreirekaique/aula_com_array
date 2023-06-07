import random

quntidade_jogadores = int(input('Digite o número de jogadores: '))

jogadores = []

for i in range(quntidade_jogadores):
    nome = input(f'Digite o nome dos jogadores {i+1}:')
    aleatorios = (random.randint(1,10))
    jogadores.append(nome)
    jogadores.append(aleatorios)

valor_vencedor = 0
maior_numero = jogadores[0]

for i in range(1, quntidade_jogadores):
    if jogadores[i] > maior_numero:
        maior_numero = jogadores[i]
        valor_vencedor = i

print('Os jogadores:', jogadores[valor_vencedor])
