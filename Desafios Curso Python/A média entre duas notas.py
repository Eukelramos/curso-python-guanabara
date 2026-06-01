# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Diga seu nome:')
nt1 = float(input('Digite sua nota no teste: '))
nt2 = float(input('Digite sua nota na prova: '))

m = (nt1 + nt2) / 2

print ('Logo, {} a sua média na unidade foi {:.1f}'.format(nome,m))
