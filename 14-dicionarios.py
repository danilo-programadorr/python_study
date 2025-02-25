gameFifa = {
  'name': 'Fifa 25',
  'yearLaunch': '2024',
  'gamePrice': 'R$ 90.50',
  'classificaton': 8.5,
  'genre' : ['esportes', 'familia'] # lista dentro de um dicionário
}

print(gameFifa)
print(len(gameFifa))  
print(type(gameFifa))

# 1- Recuperar um elemento do Dicionário
print(gameFifa['genre'])
print(gameFifa.get('name'))

# 2- Buscar apenas as chaves do dicionário
print(gameFifa.keys())

# 3- Buscar apenas os valores do dicionário
print(gameFifa.values())

# 4- Buscar itens do dicionário chave e valor
print(gameFifa.items())

# 5- Adicionar intens no dicionáro
gameFifa['Players'] = 2
print(gameFifa)

# 6- Atualiza itens do dicionario
gameFifa.update({'Players'})
print(gameFifa)

# 7- Remove itens no dicionario
gameFifa.pop('Players')
print(gameFifa)