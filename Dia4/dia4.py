# 1. Criando uma lista com vários itens:
# Os colchetes servem para criar a lista e também para acessar os itens.
nomes = ["Ana", "Bruno", "Carlos", "Diana"]

print(nomes)  # Exibe todos os itens da lista.

# 2. Acessando elementos individuais da lista:
print(nomes[0]) # Mostra Ana.
print(nomes[2]) # Mostra Carlos.

# 3. Substituindo um item da lista:
nomes[1] = "Beatriz"  # Substitui Bruno por Beatriz.

print(nomes)

# 4. Adicionando um novo nome ao final da lista com ".append()":
nomes.append("Eduardo")

print(nomes)

# 5. Removendo um item da lista pelo valor com ".remove()":
nomes.remove("Carlos")

print(nomes)

# 6. Removendo o último item da lista com ".pop()":
nomes.pop()

print(nomes)

# 7. Verificando o tamanho da lista com "len()":
print(f"A lista tem {len(nomes)} nomes.")  # Exibe a quantidade de itens

# 8. Percorrendo a lista com um laço for:
for nome in nomes:
    print(f"Olá, {nome}!")
