#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Vamos calcular os lados de um triângulo retângulo... \nDigite o comprimento do cateto opsto:'))
ca = float(input('Agora digite o comprimento do cateto adjacente:'))

hipotenusa = hypot(co, ca)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')
