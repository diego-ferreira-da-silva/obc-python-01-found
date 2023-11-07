""" Exercício 3

Cálculo da Distância

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas."""

distancia = float(input("Qual a distância que você quer percorrer em KM\n"))
if distancia > 200.0:
  valorKM = 0.35
  valorViagem = distancia * valorKM
else:
  valorKM = 0.50
  valorViagem = distancia * valorKM

print(f"O valor da viagem será de R${valorViagem} custando R${valorKM} o KM")

#--------------------------------------------------------------------------------------------------------
"""Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%."""

salario = float(input("Digite o valor do salario para saber o valor do aumento e a porcentagem\n"))

if salario > 1250.00:
  aumento = 0.10
  porcentagem = 10
  salarioAumento = salario + salario*aumento
else:
  aumento = 0.15
  porcentagem = 15
  salarioAumento =salario + salario*aumento
  
print(f"O valor do Salário é R${salario} e receberá {porcentagem}% ficará R${salarioAumento}")