# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite um valor '))

cm = m * 100
mm = m * 1000

print('Logo, {} metros é igual a {} centímetros e  a {} milímetros '.format(m,cm,mm))
