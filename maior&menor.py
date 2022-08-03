# 

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
numero3 = int(input("Digite um numero: "))

maior = numero1
menor = numero2

if numero1 > maior:
  maior = numero1
if numero2 > maior:
  maior = numero2
if numero3 > maior:
  maior = numero3
if numero1 < menor:
  menor = numero1
if numero2 < menor:
  menor = numero2
if numero3 < menor:
  menor = numero3

print("O menor numero é: %d" %menor)
print("O maior numero é: %d" %maior)