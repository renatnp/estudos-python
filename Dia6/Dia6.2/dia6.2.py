# Criando uma lista com números
numeros = [5, 2, 7, 5, 9, 1, 5]

# Verifica se o número 5 está na lista
if 5 in numeros:
    print("O número 5 está na lista.")

# Verifica se o número 8 está na lista
if 8 not in numeros:
    print("O número 8 não está na lista.")

# Conta quantas vezes o número 5 aparece na lista com .count()
quantidade = numeros.count(5)
print(f"O número 5 aparece {quantidade} vezes.")
