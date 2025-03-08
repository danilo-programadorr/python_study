""" 
Cálculo da Distância

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas.
"""
distancia = float(input('Quantos km deseja percorrer ?\n')) 

if distancia <= 200:
  ticket = 0.5 * distancia
else:
  ticket = 0.35 * distancia
print(f'O valor da passagem será R${ticket:.2f}  ') # difine quantas casas decimais terá depois do ponto 
   

"""
Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
"""

salario = float(input('Informe aqui seu Salario! \n'))
if salario > 1250:
  aumento = salario + (salario * 0.10) 
else:
  aumento = salario  + (salario * 0.15)
 
print (f'Seu salário foi para R${aumento}')