num1 = float(input('Digite o número 1\n'))
num2 = float(input('Digite o número 2\n'))
operation = input('Digite a operação a Realizar (+ - * /)\n')

if operation == '+':
   result = num1 + num2
elif operation == '-':
  result = num1 - num2 
elif operation == '*':
  result = num1 * num2
elif operation == '/':
  result = num1 / num2    
else:
  print('Operação Inválida')
  result = 0   
  
print(f'O resultado é: {result}')