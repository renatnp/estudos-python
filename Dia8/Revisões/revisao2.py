lista = []
for i in range(4):
    nome = input(f"Digite o {i+1}° nome: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    lista.append([nome, idade])
print("\nCadastro:")
for pessoa in lista:
    print(f"{pessoa[0]} tem {pessoa[1]} anos.")
print(f"\nTotal de pessoas cadastradas: {len(lista)}")
print("\nMaiores de idade:")
for pessoa in lista:
    if pessoa[1] >= 18:
        print(f"{pessoa[0]} é maior de idade, com {pessoa[1]} anos.")
soma = 0
for pessoa in lista:
    soma += pessoa[1]
media = soma / len(lista)
print(f"A média das idades cadastradas é: {media:.2f} anos. ")
mi = lista[0][1]
pmv = lista[0][0]
mei = lista[0][1]
pmn = lista[0][0]
for pessoa in lista:
    if pessoa[1] > mi:
        mi = pessoa[1]
        pmv = pessoa[0]
    if pessoa[1] < mei:
        mei = pessoa[1]
        pmn = pessoa[0]
print(f"\nA pessoa mais velha é {pmv}, com {mi} anos.")
print(f"A pessoa mais nova é {pmn}, com {mei} anos.")