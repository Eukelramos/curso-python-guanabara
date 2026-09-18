# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS.
# EX: APOS A SOPA,
# A SACADA DA CASA,
# A TORRE DA DERROTA,
# O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

frase = input('Digite uma frase: ').upper().replace(' ', '')
invertida = ''
for c in range(len(frase) - 1, -1, -1):
    invertida += frase[c]
if frase == invertida:
    print('É PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')