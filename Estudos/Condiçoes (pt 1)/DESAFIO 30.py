# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
nu = int(input('Digite um número: '))
if nu % 2 == 0:
    print(f'O número {nu} é PAR')
else:
    print (f'O número {nu} é IMPAR')