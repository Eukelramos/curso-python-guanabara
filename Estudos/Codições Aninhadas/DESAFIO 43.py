# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

ps = float(input("informe o seu peso atual: "))
alt = float(input("informe o seu altura: "))
imc = ps / alt ** 2
if imc < 18.5:
    print ("Você esta abaixo do peso normal")
elif 18.5 <= imc < 25:
    print ("Você esta no peso normal")
elif 25 <= imc < 30:
    print ("Você esta com sobrepeso")
elif 30 <= imc < 40:
    print ("Você esta com obesidade")
else:
    print ("Você esta com obesidade mórbida")
