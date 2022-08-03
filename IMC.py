# Calcula IMC

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
  print("Abaixo do peso!")
elif imc >= 18.5 and imc <= 25:
  print("Peso normal! \n imc: %f" %imc)
elif imc > 25 and imc <= 30:
  print("Acima do peso!")
else: 
  print("Obeso!!!!")