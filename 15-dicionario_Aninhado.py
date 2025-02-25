import pprint

GameDict = {
  'Resident Evil':{
    'YearLauch': 2020,
    'classificação': 9.0,
    'genre':['ação','suspense']
  },
  'Red Dead 2':{
    'YearLauch': 2021,
    'classificação': 9.5,
    'genre':['ação','suspense']
  },
  'Good of War':{
    'YearLauch': 2018,
    'classificação': 9.7,
    'genre': ['ação','Aventura']
  }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(GameDict)

# 1 - Buscar informação dentro de um dicionario aninhado.
print(GameDict['Resident Evil']['genre'])

# 2 - Adicionar um novo item.
GameDict['Red Dead 2']['players'] = 1
print(GameDict['Red Dead 2'])

# 3 - excluir um dicionario.
del GameDict['Red Dead 2']
pp.pprint(GameDict)