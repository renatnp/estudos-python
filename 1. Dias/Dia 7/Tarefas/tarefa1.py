cadastro = []

# Pede o nome e a idade 4 vezes
for i in range(4):
    nome = input(f"Digite o nome da {i+1}° pessoa: ")  # Solicita o nome
    idade = int(input(f"Digite a idade de {nome}: "))  # Solicita a idade e converte para inteiro
    cadastro.append([nome, idade])  # Adiciona uma sublista (nome, idade) à lista cadastro

print("\nDados cadastrados:")
for pessoa in cadastro:
    print(f"{pessoa[0]} tem {pessoa[1]} anos.")  # Exibe o nome e a idade de cada pessoa na lista
