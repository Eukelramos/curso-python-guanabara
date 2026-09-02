# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes


r1 = float(input("Digite o primeiro comprimento: "))
r2 = float(input("Digite o segundo comprimento: "))
r3 = float(input("Digite o terceiro comprimento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com os tres comprimentos é possível forma um triangulo')

    if r1 == r2 == r3:
        print("O triângulo é Equilátero ")

    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print("O triângulo é Isósceles")
    else:
        print("O triângulo é Escaleno")

else:
    print("Infelizmente, não é possível formar um triângulo ")

