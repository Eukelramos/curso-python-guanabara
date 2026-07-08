# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela
# se o usuário venceu ou perdeu.

import random
num = random.randint(0,5)
esc = int(input ('Diga qual número será sorteado entre 0 e 5: '))
if num == esc:
    print (f'Boa escolha você escolheu o número {esc} e o sorteado foi {num}')
else:
    print (f'Não foi desta vez, o número sorteado foi {num}')
