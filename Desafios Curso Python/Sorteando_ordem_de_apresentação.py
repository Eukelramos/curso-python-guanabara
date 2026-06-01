# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

print('Vamos sortear a ordem de apresentação dos 4 alunos destacados.')

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]

random.shuffle(lista) #shuffle() embaralha a lista toda.

print('A ordem de apresentação será:')
print('1- ',lista[0])
print('2- ',lista[1])
print('3- ',lista[2])
print('4- ',lista[3])
