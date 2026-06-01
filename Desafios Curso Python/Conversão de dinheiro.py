# Crie um programa que leia quanto dinheiro uma pessoal tem na carteira e
# mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27.

carteira = float(input ('Quanto você quer trocar? '))

d = carteira / 3.27

print('Você terá Us${:.2f}'.format(d))
