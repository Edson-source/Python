# codigo de calculadora entre 2 numeros

numero1 = float (input("Digite o valor do numero 1: "))
numero2 = float (input("Digite o valor do numero 2: "))
operador = str(input("Digite uma operação: \n Soma (+) \n Subtração (-) \n Multiplicação (*) \n Divisão (/) \n"))

if operador == '+':
   resultado = numero1 + numero2
elif operador == '-':
   resultado = numero1 - numero2
elif operador == '*':
   resultado = numero1 * numero2
elif operador == '/':
   resultado = numero1 / numero2

print("O resultado da operação é ", resultado)