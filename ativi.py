import random

quntidade_jogadores = int(input('Digite o número de jogadores: '))

jogadores = []

num_aleatorios = []

for i in range(quntidade_jogadores):
    nome = input(f'Digite o nome dos jogadores {i+1}:')
    jogadores.append(nome)
    
    num_aleatorio = random.randint(1, 10)
    num_aleatorios.append(num_aleatorio)
    

valor_vencedor = 0
maior_numero = num_aleatorios[0]

for i in range(quntidade_jogadores):
    if num_aleatorios[i] > maior_numero:
        maior_numero = num_aleatorios[i]
        valor_vencedor = i
        

print('jogador vencedor é:', jogadores[valor_vencedor])
print('valor sorteado é:', num_aleatorios[valor_vencedor])



