# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input ('Digite um número:'))

do = n1 * 2
tri = n1 * 3
rq = n1 ** (1/2)

print ('O dobro de {} é {}, O triplo é {} e a raiz quadrada é {:.3f}'.format (n1, do, tri, rq))
