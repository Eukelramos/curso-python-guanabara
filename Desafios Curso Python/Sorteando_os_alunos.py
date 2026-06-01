#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
a1 = input('O professor quer sortea entre 5 alunos quem vai apagar o quadro.\nPrimeiro aluno:')
a2 = input('Quem mais?')
a3 = input('Próximo ')
a4 = input('Próximo ')
a5 = input('O ultimo ')

alunos = [a1,a2,a3,a4,a5]
sorteado = random.choice(alunos) #Para sortear um nome numa lista, use random.choice():

print (f'O sorteado foi {sorteado}')
