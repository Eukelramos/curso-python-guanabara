# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite uma ano da sua preferencia: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f'O ano de {ano} ele e bissexto')
else:
    print(f'O ano {ano} nao e bissexto')