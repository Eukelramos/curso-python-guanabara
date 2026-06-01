#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#EX: digite um número: 6.127 O número 6.127 tem a parte inteira 6.

#IMPORTAÇÃO COMPLETO DO MÓDULO OCUPA MAIS ESPAÇO NA MEMÓRIA.
#import math
#num = float(input('Digite um número: '))
#captura de tela (f'O valor digitado foi {num} e a sua porção inteira é {math.trunc(num)}')

#IMPORTAÇÃO Apenas DE UM OBJETO DO MÓDULO.
from math import trunc
num = float(input('Digite um número: '))
print (f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')

