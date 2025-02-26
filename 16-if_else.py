name = input('Digite o nome do jogo\n')
Yearlaunch = int(input('Digite o ano de lançamento\n'))
classification = float(input('Digite a nota do jogo\n'))

if classification >= 8.0 and Yearlaunch >= 2015:
  print(f'O jogo {name} é Bom. Recomendo joga-lo')
else:
  print(f'O jogo {name} ainda não atingiu uma boa pontuação.')