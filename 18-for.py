gamesList = ["God Of War", "Baldurs Gate 3", "Uncharted", 10]

#Iterando valores de uma lista
for game in gamesList:
  print(game)
print("-"*10)
  
# Quando a condição for atendida, o Loop será encerrado
for game in gamesList:
  if game == "Baldurs Gate 3":
    break
  print(game)
print("-"*10)

#Quando a condição for atendida o loop vai para proxima iteração
for game in gamesList:
  if game == "Baldurs Gate 3":
    continue
  print(game)
print("-"*10)

#Avaliação do Jogo
gameName = input("Digite o nome do Jogo\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))
soma = 0

for i in range(gameRating):
  nota = float(input("Digite a nota para o jogo\n"))
  soma += nota
print(f"A média de avaliação do {gameName} é {soma/gameRating :.2f}")