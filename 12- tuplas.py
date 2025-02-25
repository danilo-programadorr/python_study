gamesTuple = ('Resident Evil', 'star Wars Jedi Survivor', 
            'The Legend of  Zelda','Red Dead 2', 'Mario Odyssey', 'Good of War','Mario Odyssey')
#print(gamesTuple)
#print(type(gamesTuple))
#name = ('Danilo',)
#print(type(name))

# - 1 Buscar os dois primeiro da tupla
print(gamesTuple[:2])
# - 2 Buscar os dois  primeiro itens da tupla
print(gamesTuple[-1])
# - 3 buscar jogos até uma determinada posição
print(gamesTuple[:3])
# - 4 Buscar jogos de uma posição em diante
print(gamesTuple[2:])
# - 5 Recuperar um itemda tupla pelo indice
print(gamesTuple.index('Red Dead 2'))
# - 6 Retorna o número de vezes que o valor x aparece na tupla
print(gamesTuple.count('Mario Odyssey'))

# - não possibilita adicionar valores na tupla
# - não possibilita remover valores na tupla
# - não possibilita ordenar valores na tupla

