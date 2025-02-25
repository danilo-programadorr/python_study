gameName = "Fifa 23"

gameDescription = """
  Fifa 23, é um jogo de futebol 
  desenvolvido pela EA Sports,
  e que possibilita jogar o Fifa localmente ou online 
"""

print(gameName.upper()) # retornar string em Maiúsculo
print(gameName.lower()) # retornar string em Minuscula
print(gameName.capitalize()) # apenas a primeira letra em Maiúscula
print(gameName.title()) # apenas a primeira letra em Maiúscula
print(gameName.center(11,'-')) # retornar string centralizada com caractere de preenchimento
print(gameName.find("2")) # Retorna a posição de um determinado caractere
print(gameDescription.count("t")) # Conta de caracteres
print(gameDescription.replace("Fifa","Pes")) # Altera um elemento pelo outro
print(gameDescription.split(",")) # separa  