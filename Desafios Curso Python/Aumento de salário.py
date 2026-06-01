# Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário,
# com 15% de aumento.

salario = float(input('Digite o seu salario aqui R$'))

aumento = (salario * 15) / 100
nsalario = salario + aumento

print(f'Seu novo salario é de R${nsalario:.3f}')
