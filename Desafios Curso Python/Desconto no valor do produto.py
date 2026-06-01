# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Digite o valor atual do produto R$'))

desconto = valor * 0.05
nvalor = valor -desconto

print(f'Com o desconto de 5%, você só pagará R${nvalor:.2f} ')
