# Utilizando o Input
"""
Comentário multiplas linhas

Jogoteca
"""

name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n")) 
gamePrice = float(input("Digite o preço do Jogo:\n"))
planIncluded = input("Está incluso no serviço mensal?\n")

print(f"O nome do jogo que está jogando é: {name}")
print(f"O Ano de lançamento: {yearLaunch}")
print(f"Valor R${gamePrice}")
print(f"Incluso no mensal: {planIncluded}")