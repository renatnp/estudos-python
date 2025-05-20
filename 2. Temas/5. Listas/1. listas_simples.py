# Cria uma lista com valores
frutas = ["maçã", "banana", "laranja"]

# Acessa elementos pelo índice (começa em 0)
print(frutas[0])  # maçã
print(frutas[2])  # laranja

# Adiciona elementos
frutas.append("uva")
print(frutas)

# Remove elementos
frutas.remove("banana")
print(frutas)

# Cria listas usando range()
numeros = list(range(1, 6))  # [1, 2, 3, 4, 5]
print(numeros)

# Converte string em lista de caracteres
palavra = "Python"
letras = list(palavra)
print(letras)
