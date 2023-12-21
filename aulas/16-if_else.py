name = input("Digite o nome do Jogo: ")
yearLunch = int(input("Digite o ano de lançamento do jogo: "))
classification = float(input("Digite a nota de classificação do jogo: "))

if classification > 8.0 or yearLunch > 2015:
  print(f"O jogo {name} é bom. Recomendo joga-lo.")
else:
  print(f"O jogo {name} ainda não tem uma nota alta. Não recomendo joga-lo")