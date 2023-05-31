import random

quntidade_jogadores = int(input('Digite o número de jogadores: '))

jogadores = []

for i in range(quntidade_jogadores):
    nome = input(f'Digite o nome dos jogadores {i+1}:')
    aleatorio = (random.randint(1,10))
    jogadores.append(nome)
    jogadores.append(aleatorio)
    
print('Os jogadores:', jogadores)
print('Os valore aleatorio obitiodos por cada jogador é:', aleatorio)