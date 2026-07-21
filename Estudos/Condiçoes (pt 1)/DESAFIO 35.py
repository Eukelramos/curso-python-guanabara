# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podm ou não forma um triângulo.

print('=-'*20)
print('ANALISADOR DE TRIANGULO')
print('=-'*20)

r1 = float(input("Digite o primeiro comprimento: "))
r2 = float(input("Digite o segundo comprimento: "))
r3 = float(input("Digite o terceiro comprimento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com os tres comprimentos é possível forma um triangulo')
else:
    print('Infelizmente com esses comprimentos nao é possível forma um triangulo')
