# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salario? '))
if salario > 1250:
    novo = salario * 1.10
    print(f'Com o aumento de 10%, seu novo salário é de R${novo:.2f}')
else:
    novo = salario * 1.15
print(f'Com o aumento de 15%, seu novo salário é de R${novo:.2f}')
