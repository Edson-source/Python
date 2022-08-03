# interpolação de texto
# concatenação de texto

carro = "Ka"
ano = 2018
preco = 30000

# Concatenação
print("Carro: " + carro + " Preço: " + str(preco))

# Versões antigas
print("Carro: %s, ano: %d, preço: %f" %(carro, ano, preco))

# Versões recentes
print("Carro: {}, ano: {}, preço: {}" .format(carro, ano, preco))
print("Carro: {0}, ano: {1}, preço: {2}" .format(carro, ano, preco))

# Versão atual
print(f'Carro: {carro}, Ano: {ano}, Preço: {preco}')