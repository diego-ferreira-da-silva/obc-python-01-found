gamesList = ["Resident Evil", "Red Dead Redemption 2", 
            "The Legend of Zelda", "Baldurs Gate 3"]

# 1 - Tamanho da lista
print(len(gamesList))

# 2 - Recupera um item da lista pelo índice
print(gamesList.index("Baldurs Gate 3"))

# 3 - Adiciona item ao final da lista
gamesList.append("Ori")
gamesList.append("Guacamelee!")
print(gamesList)

# 4 - Ordena lista
gamesList.sort()

#listaJogos.reverse()
print(gamesList)

# 5 - Copia os itens de uma lista para outra
gamesReset = gamesList.copy()
gamesReset.remove('Red Dead Redemption 2')
gamesReset.remove('Guacamelee!')
print(gamesReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)