cadastro = []
for i in range(4):
    nome = input(f"Digite o nome da {i+1}° pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    cadastro.append([nome, idade])

print("\n--- DADOS CADASTRADOS: ---")
for pessoa in cadastro:
    print(f"{pessoa[0]} tem {pessoa[1]} anos.")

print(f"\nTotal de pessoas cadastradas {len(cadastro)}")

print("\nMaiores de idade:")
for pessoa in cadastro:
    if pessoa[1] >= 18:
        print(f"{pessoa[0]} tem {pessoa[1]} anos.")

soma = 0
for pessoa in cadastro:
    soma += pessoa[1]

media = soma / len(cadastro)
print(f"A média de idade é: {media:.2f}")


maior_idade = cadastro[0][1]
pessoa_mais_velha = cadastro[0][0]

menor_idade = cadastro[0][1]
pessoa_mais_nova = cadastro[0][0]

for pessoa in cadastro:
    if pessoa[1] > maior_idade:
        maior_idade = pessoa[1]
        pessoa_mais_velha = pessoa[0]

    if pessoa[1] < menor_idade:
        menor_idade = pessoa[1]
        pessoa_mais_nova = pessoa[0]

print(f"\nA pessoa mais velha é {pessoa_mais_velha}, com {maior_idade} anos.")
print(f"A pessoa mais nova é {pessoa_mais_nova}, com {menor_idade} anos.")