gameName = "Fifa 23"
gameDescription = """
  Fifa 23 é um jogo de futebol desenvolvido pela EA Sport
  que possibilita jogar Online e Local
"""

#Fatiamento - string[início:fim] - índice começa em 0 e o final -1

# 1- Busque toda String a partir da primeira posição
print(gameName[0:])

#2 - Busque toda string a partir da última posição
print(gameName[:7])

## 3- Busque toda string da terceira até a última posição
print(gameName[2:])

"""
# - string[início:passo] - índice começa em 0 e o final -1
passo - determina o incremento. Por padrão é 1 mas é possível ser definido,
"""

# 4- Busque toda string de 2 em 2
print(gameName[::2])

# 5- Busque toda string nos índices ímpares
print(gameName[1::2])

# 6- Inverter uma string
print(gameName[::-1])