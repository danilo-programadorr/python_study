gameList = ['Resident Evil', 'star Wars Jedi Survivor', 
            'The Legend of  Zelda','Red Dead 2', 'Mario Odyssey', 'Good of War']
# 1 - Tamanho da lista
print (len(gameList))

# 2 - Reculperar um intem da lista pelo indice
print(gameList.index('Good of War'))

# 3 - adicionar um intem ao final da lista
gameList.append('Gta V')
print(gameList)

# 4 - Ordenar a lista
gameList.sort()
print(gameList)

# 5 - copiar o s itens de uma lista para outra
gameReset = gameList.copy()
gameReset.remove('Gta V')
print(gameReset)

# 6 - Remove todos os itens da lista
gameList.clear()
print(gameList)
