# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input("Qual o valor do imóvel? R$"))
salario = float(input("Informe o seu rendimento mensal: R$"))
anos = float(input("Informe em quantos anos você pretende pagar: "))

prestação = valor / (anos * 12)
mínimo = salario * 30 / 100

print(f"Para pagar uma casa de R${valor:.2f} em {anos} anos")
print(f"a prestação será de R${prestação:.2f}")

if prestação <= mínimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
