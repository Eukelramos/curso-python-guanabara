# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagem de até 200km e R$0,45 para viagens mais longas.
dtc = float(input('Qual a distância (em km) da viagem que você deseja fazer? '))
if dtc <= 200:
    preco = dtc * 0.50
else:
    preco = dtc * 0.45
print(f'O valor da viagem é de R${preco:.2f}')

