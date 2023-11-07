gameBaldursGate = {
    "name" : "Baldurs Gate {version}",
    "version" : 3,
    "gamePrice" : 200,
    "classification" : 9.5,
    "genre": ["RPG","Aventura", "Ação"]
    }

print(gameBaldursGate)
print(len(gameBaldursGate))
print(type(gameBaldursGate))

#Recuperar um elemento

print(gameBaldursGate["genre"])
print(gameBaldursGate.get('classification'))

#Buscar apenas chaves do dicionário
print(gameBaldursGate.keys()) #retorna apenas as chaves
print(gameBaldursGate.values()) #retorna apenas os valores

#Buscar item do dicionário com chave e valor
print(gameBaldursGate.items())

#Adionar itens no dicionário
gameBaldursGate["players"] = 4
print(gameBaldursGate)

#Atualizar itens
gameBaldursGate.update({"players": 3})
print(gameBaldursGate)


#remover
gameBaldursGate.pop("players")
print(gameBaldursGate)
