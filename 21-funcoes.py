def wellcome():
  print("Olá Mundo!")
  
wellcome()

def sum():
  return 5 + 4

#Função para cadastrar um jogo

def create_game():
  name = input("Digite o nome do jogo:\n")
  yearLaunch = int(input("Digite o ano de lançamento do jogo:\n")) 
  gamePrice = float(input("Digite o preço do Jogo:\n"))
  noteRating = input("Digite a nota de avaliação do jogo\n")
  print(f"{name} - R${gamePrice}")  

create_game()