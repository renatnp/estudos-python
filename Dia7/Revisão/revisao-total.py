nomes = []
idades = []

for i in range(6):
    nome = input(f"Digite o {i+1}° nome: ")
    nomes.append(nome) 

for i in range(6):
    idade = int(input(f"Digite a idade de {nomes[i]}: "))
    idades.append(idade) 

for i in range(len(nomes)):
    print(f"{nomes[i]} tem {idades[i]} anos.")

print(f"A quantia de pessoas cadastradas é {len(nomes)}.")

# Encontra a maior idade da lista.
mais_velho = max(idades)

# Encontra o índice (posição) da maior idade.
indice = idades.index(mais_velho)

# Mostra quem é a pessoa mais velha.
print(f"A maior idade é {mais_velho} e pertence a {nomes[indice]}")

# Encontra a menor idade e seu respectivo nome.
mais_novo = min(idades)
indice2 = idades.index(mais_novo)
print(f"A menor idade é {mais_novo} e pertence a {nomes[indice2]}")

# Calcula a média das idades.
soma = sum(idades)
media = soma / len(idades)
print(f"A média de idade é {media:.2f} anos.")  # Exibe a média com duas casas decimais.

# Mostra quem é maior de idade (18 anos ou mais).
for i in range(len(idades)):
    if idades[i] >= 18:
        print(f"{nomes[i]} é maior de idade com {idades[i]}.")
