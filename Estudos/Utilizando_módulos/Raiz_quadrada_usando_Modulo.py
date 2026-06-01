import math # math é a biblioteca de matematica que já vem instalada.
#from math import sqrt #(dá matemática importe raiz_quadrada)

num = int(input('digite um número: '))

raiz = math.sqrt(num) # sqrt é para saber a raiz quadrada do número. Se eu usar from não digito math nesta linha.

print (f'A raiz quadrada de {num} é {raiz:.2f}')

