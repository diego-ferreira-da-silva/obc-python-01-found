gameDescription = """
  Fifa 23 é um jogo de futebol
  desenvolvido pela EA Sport
  que possibilita jogar Online e Local
"""
gameName = "Fifa "
gameVersion = "23"
line = "="

#Contatenação
print(line*25)
gameFullName = gameName + gameVersion
print(gameFullName)

#Operação
print(line*25)

#busca
print("Fifa" in gameDescription)
print("futebol" in gameDescription)
print("Parangolé" in gameDescription)