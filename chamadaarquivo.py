file = "exemplo.txt"

teste = open(file, 'r')
for indice, linha in enumerate(teste):
  print(indice, linha)

teste.close()