gameSet = {"Fifa 10", "Guacamalee", "Baldurs Gate 3", "The Legend of Zelda",
           "Super Mário World", "Resident Evil 4"}
print(gameSet)

# Buscar o tamanho do set
print(len(gameSet))

# True e 1 são considerados o mesmo valor
# Então se mandarmos apresentar ele não mostra todo set
exempleSet = {"Assassins Creed", True, 1, 100}
print(exempleSet)

# É possível adicionar itens de outro Set
gameSet.update(exempleSet)
#diferente da Lista, não é possível ter valores repitidos no Set
print(gameSet)

# É possível remover item do Set
gameSet.remove(True)
gameSet.remove(100)
print(gameSet)


#Não permite recuperar valores por fatiamento o Slice