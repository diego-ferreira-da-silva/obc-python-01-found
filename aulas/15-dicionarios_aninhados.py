import pprint

gamesDict = {
  "Baldurs Gate" : {
      "name" : "Baldurs Gate {version}",
      "version" : 3,
      "yearLaunch": 2023,
      "gamePrice" : 299,
      "classification" : 9.5,
      "genre": ["RPG","Aventura", "Ação"]
  },
  "Resident Evil 4" : {
    "yearLaunch": 2023,
    "classification": 9.2,
    "gamePrice": 200,
    "genre": ["Ação", "Aventura", "Terror"]
  },
  "Donkey Kong Country":{
    "yearLaunch": 1995,
    "classification": 9.5,
    "genre": ["Aventura", "Plataforma"]
  }
}
pp = pprint.PrettyPrinter(depth=3)
pp.pprint(gamesDict)

#Buscar informação dentro do dicionário aninhado
#buscando uma info
print(gamesDict["Baldurs Gate"]["genre"])

#adicionar um novo item
gamesDict["Baldurs Gate"]["players"] = 1
pp.pprint(gamesDict["Baldurs Gate"])

#excluir um dicionário
del gamesDict["Donkey Kong Country"]
pp.pprint(gamesDict)