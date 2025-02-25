""" 

Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere
Ex:
fifa 23 → **fi#a 23**
restart→ resta#t

 troca de  caractere 
Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.
Ex:
abc xyz → **xyc abz**
"""
gameDescription = """
  Fifa 23, é um jogo de futebol 
  desenvolvido pela EA Sports,
  e que possibilita jogar o Fifa localmente ou online 
"""
## *Substituindo caractere repetido
"""gameName = input('Digite o nome do jogo!\n')

char = gameName[0].lower()
new_name = gameName.replace(char,'$')
new_name = char + new_name[1:]
print(new_name)

## *troca de  caractere
stg1 = 'abc'
stg2 = 'akm'
new_stg1 = stg2[:2] + stg1[2:]
new_stg2 = stg1[:2] + stg2[2:]
print(new_stg1,new_stg2)"""

def percurso_text(texto, char_antigo, char_novo):
  resultado = ""
  for caractere in texto:
    if caractere == char_antigo:
      resultado += char_novo  # Substitui o caractere antigo pelo novo
    else:
      resultado += caractere # Mantém o caractere original
  return resultado

char_antigo = "S" 
char_novo = "$"
texto_modificado = percurso_text(gameDescription, char_antigo, char_novo)
print(texto_modificado)   