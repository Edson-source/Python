# Listas

# Mutavel, Dinamica, Heterogenea e Indexada

lista = ["Edson", "Michele", "Kelvin", "Ana"]

print(type(lista))
print(dir(lista))
print(lista)

print(lista[0])
print(lista[1])
print(lista[-1])
print(lista[:2])
print(lista[0:2])
print(lista[::2])

lista.append("Keko")
print(lista)
lista.remove("Kelvin")
print(lista)

print(lista[::len(lista)-1])

del lista[3]
print(lista)

lista.pop(1)
print(lista)

print(len(lista))
print(lista.count("Edson"))
print(lista.index("Ana"))

lista.insert(3, "Edson")
print(lista)

lista.reverse()
print(lista)

lista.sort()
print(lista)

lista.clear()
print(lista)