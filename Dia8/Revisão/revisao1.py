lista = []
for i in range(4):
    nome = input(f"Digite o nome da {i+1}° pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    lista.append([nome, idade])
print("\n --- Cadastros: --- ")
for pessoa in lista:
    print(f"{pessoa[0]} tem {pessoa[1]} anos.")