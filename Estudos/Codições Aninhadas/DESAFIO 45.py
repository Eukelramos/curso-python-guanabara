# Crie um programa que faça o computador jogar jokempô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

# --- VALIDAÇÃO ANTES DE USAR O ÍNDICE ---
if jogador not in (0, 1, 2):
    print('JOGADA INVÁLIDA!')
else:
    print('-=' * 11)
    print(f'O computador escolheu {itens[computador]}')
    print(f'Jogador escolheu {itens[jogador]}')
    print('-=' * 11)

    if computador == 0:
        if jogador == 0:
            print('Empate')
        elif jogador == 1:
            print('PARABÉNS, você venceu')
        elif jogador == 2:
            print('O computador venceu!')
    elif computador == 1:
        if jogador == 0:
            print('O computador venceu!')
        elif jogador == 1:
            print('Empate')
        elif jogador == 2:
            print('PARABÉNS, você venceu')
    elif computador == 2:
        if jogador == 0:
            print('PARABÉNS, você venceu')
        elif jogador == 1:
            print('O computador venceu!')
        elif jogador == 2:
            print('Empate')
