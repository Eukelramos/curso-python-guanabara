# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de pagamento:

# - Á vista dinheiro/cheque: 10% de desconto
# - Á vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print(f"{' LOJAS TECH ':=^40}")
pc = float(input("perço das compras:"))
print("""FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = pc - (pc * 10 / 100)
elif opção == 2:
    total = pc - (pc * 5 / 100)
elif  opção == 3:
    total = pc
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opção == 4:
    total = pc + (pc * 20 / 100)
    totparc = int(input('Quantos parcelas?'))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    total = pc
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${pc:.2f} vai custar R${total:.2f}')
