# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR
# DIGITADO FOR IMPAR, DESCONSIDERE-O.

s = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
       s = s + n
print(f'A soma de todos os números PARES é igual a {s}')
