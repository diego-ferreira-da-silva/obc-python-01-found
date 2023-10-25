gameName = "Fifa 23"
gameDescription = """
  Fifa 21 é um jogo de futebol, desenvolvido pela EA Sport,
  que possibilita jogar Online e Local
"""

print(gameName.upper()) #Retornar String em Maiúsculo
print(gameName.lower()) #Retorna String em minúsculo
print(gameName.capitalize()) #Apenas primeria Letra em maiúscula
print(gameName.title()) #Apenas primeira letra em maiúscula
print(gameName.center(10, '-')) #Retorna string centralizada com caractere de preenchimento
print(gameName.find('a')) #Retorna a posição de um determinado caractere
print(gameDescription.count("f")) #Conta caractere
print(gameDescription.replace("Fifa", "PES")) #Altera um elemento por outro
print(gameDescription.split(',')) #Divide a string quebrando pelo ,