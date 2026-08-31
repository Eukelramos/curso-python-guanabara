# A confederação nacional de natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# = Até 20 anos: Sênior
# = Acima: Master

from datetime import date
anoatual = date.today().year
ano = int(input("Olá atleta, informe o ano de seu nascimento: "))
idd = anoatual - ano
if idd <= 9:
    print(f"O atleta tem {idd}, sua categoria é MIRIM")
elif idd <=14:
    print(f"O atleta tem {idd}, sua categoria é INFANTIL")
elif idd <= 19:
    print(f"O atleta tem {idd}, sua categoria é JUNIOR")
elif 20 == idd:
    print(f"O atleta tem {idd}, sua categoria é SÊNIOR")
else:
    print(f"O atleta tem {idd}, sua categoria é MASTER")
