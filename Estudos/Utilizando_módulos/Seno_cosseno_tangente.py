#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno. cosseno e tangente
# desse ângulo.

from math import sin, cos, tan, radians, trunc

angulo = float(input('Digite  o ângulo: '))

seno = sin (radians (angulo))
cosseno = cos (radians (angulo))
tangente = tan (radians (angulo))

print (f'O seno de {trunc(angulo)}° é {seno:.2f} ')
print (f'O cosseno de {trunc(angulo)}° é {cosseno:.2f} ')
print (f'A tangente de {trunc(angulo)}° é {tangente:.2f} ')
