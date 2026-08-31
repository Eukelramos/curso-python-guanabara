# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input("Qual foi sua nota no primeiro semestre? "))
n2 = float(input("Qual foi sua nota no segundo semestre? "))

m = (n1 + n2)/2
if m < 5:
    print (f"Sua média foi {m:.1f}, logo, você esta REPROVADO")
elif m >= 5 and m <= 6.9:
    print (f"Sua média foi {m:.1f}, logo, você esta em RECUPERAÇÃO")
else:
    print(f"Sua média foi {m:.1f}, logo esta APROVADO")
