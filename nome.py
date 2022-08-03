frase = "Oi meu nome é Edson !"

# True or False
print("nome" in frase)
print("Edson" in frase)
print("edson" in frase)

# retorna quantidade de caracteres na frase
print(len(frase))
print(frase.lower()) # minusculo
print(frase.upper()) # maiusculo
print(frase.capitalize()) # primeira letra maiuscula

print(dir(str))

print(frase.split())

dados = "Edson;22anos;1.72;01/06/2000"
print(dados.split(";"))