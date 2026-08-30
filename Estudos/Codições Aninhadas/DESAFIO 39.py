# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falte ou que passaou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input("Qual o ano de nascimento?"))
idade = atual - nasc
print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}.")
if idade < 18:
    faltam = 18 - idade
    print(f"Você ainda vai se alistar. Faltam {faltam} anos.")
    print(f"Seu alistamento será em {atual + faltam} anos.")
elif idade == 18:
    print("Está na hora de se alistar.")
else:
    passou = idade - 18
    print(f"Já passou do tempo. Passaram {passou} anos.")
    print(f"Seu alistamento foi em {atual - passou} anos. ")
