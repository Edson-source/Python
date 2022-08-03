# Laços de repetição

# While
contador = 1
while contador <= 4:
  print(f'executou: {contador}')
  contador += 1

postagens = [
  "Hoje eu vim para a UFSC", #0
  "A aula foi no laboratorio A119", #1
  "Os alunos gostam de mexer no celular", #2
  "Hoje eu vou comer sushi", #3
]

contador = 0

while contador < len(postagens):
  print(postagens[contador])
  contador += 1
  if contador != len(postagens):
    print("++++++++++++++")
############################################################

# For
for indice in postagens:
  print(indice)
  print("+++++++")
###########################################################
for indice in range(1,11):
  print(indice)
###########################################################
for indice, postagem in enumerate(postagens):
  print(f'{indice} - {postagem}')
  print("+++++++++++++++++++")

###########################################################
palavra = "eumechamoedsonney"

for letra in palavra:
  print(letra)

###########################################################
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio')

for mes in meses:
  print(mes)

###########################################################
frutas = {'banana', 'maça', 'abacaxi', 'uva'}

for fruta in frutas:
  print(fruta)

############################################################
