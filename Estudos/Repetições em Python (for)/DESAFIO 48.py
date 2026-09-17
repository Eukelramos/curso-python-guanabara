# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO MÚLTIPLOS DE TRÊS
# E QUE SE ENCONTRAM NO INTERVALO DE 1 E 500.

soma = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        soma += c
print(soma)
