""" Antecessor e Sucessor de um número
Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição. """

Ano = int(input('coloque o ano \n'))
print(f"o ano novo de {Ano}  é {Ano +1} e o antecessor é {Ano -1} ") 

"""  
 Média de 4 notas
Escreva um programa em Python que leia quatro números e calcule a média entre esses números
""" 
nome_aluno = input('digite o nome do aluno \n')
matematica = float(input('digite a nota \n')) 
portugues = float(input('digite a nota \n'))
história = float(input('digite a nota \n'))
quimica = float(input('digite a nota \n'))
soma =  matematica + portugues + história + quimica
Média = soma / 4
print(f"A média do {nome_aluno} foi {Média}")