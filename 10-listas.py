gameFifa = [ "Fifa 24", 2025,90.50,True ]

gameList = ['Resident Evil', 'star Wars Jedi Survivor', 
            'The Legend of  Zelda','Red Dead 2', 'Mario Odyssey', 'Good of War']

# print(gameList[:2])
# print(gameList[-1])
# print(gameList[:3])

# primeira forma
'''indice = [1,3,5]
selected_games = [gameList[a] for a in indice]
print(selected_games)'''

#segunda forma

indice = [0,3,5,7]

for i in indice:
  if i < len(gameList): # Verifica se o índice está dentro do intervalo válido
    print(gameList[i]) # Imprime o jogo correspondente ao índice
  else:
    print(f'o indice {i} não está listado')   
      
