# REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UMA NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.

n = int(input('Digite um número? '))
for c in range(1, 11):
    r = n * c
    print(f'{n} x {c} = {r}')

