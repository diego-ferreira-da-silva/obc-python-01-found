"""
*args - Utilizado quando não temos certeza de quantos argumentos teremos em uma função
- Os argumentos são passados como tuplas

**kwargs - Além dos valores, podemos passar as chaves para cada argumentos,
- São passados como dicionários
"""

#Soma de números

def sum(*num):
  sum_total = 0
  for n in num:
    sum_total += n
  print(f"Soma é: {sum_total}")
  
sum(7)
sum(10, 12, 10)

# Apresentação de cursos

def presentation(**data):
  for key, value in data.items():
    print(f"{key} - {value}")

print("Dados curso")
presentation(name="Python", category="backend", level="Iniciante")    
presentation(name="Visão computacional com Python", category="IA", level="avançado")    
