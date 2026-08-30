# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

numero = int(input('Digite um numero inteiro: '))
esc = int(input('Quais das opções abaixo você escolhe? Utilizando 1,2,3 \n 1 - binário \n 2 - octal \n 3 - hexadecimal\n Qual a sua escolha?'))
if esc == 1:
    print(f"Em binário o número é {bin(numero)[2:]}")
elif esc == 2:
    print(f"Em octal o número é {oct(numero)[2:]} ")
elif esc == 3:
    print(f"Em hexadecimal o número é {hex(numero)[2:]}")
else:
    print ("\033[00;40mNâo existe essa opção\033[m")

