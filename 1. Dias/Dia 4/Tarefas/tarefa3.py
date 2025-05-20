# Cria uma lista vazia para armazenar os nomes.
nomes = []

# Pede ao usuário para digitar 5 nomes e adicionando na lista.
for i in range(5):  # O range(5) faz o loop rodar 5 vezes.
    nome = input(f"Digite o {i + 1}º nome: ")  # Recebe o nome e mostra a posição.
    nomes.append(nome)  # Adiciona o nome à lista.

# Exibe os nomes com suas respectivas posições.
for i in range(len(nomes)):  # O "range(len(nomes))" garante que vai percorrer toda a lista.
    print(f"Nome número {i + 1}: {nomes[i]}")  # Exibe o nome e sua posição.

# Mostran quantos nomes foram digitados
print(f"\nForam digitados {len(nomes)} nomes.")
