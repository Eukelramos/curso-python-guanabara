#Faça um programa que leia a largura e a altura de uma parade em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2m².

lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = lar * alt
tinta = area / 2

print (f'A parede tem {area:.2f}m² de area.')
print(f'Serão necessários {tinta:.2f} litros de tinta.')

# O f antes do ' no conchete do print é a abreviação do .format
