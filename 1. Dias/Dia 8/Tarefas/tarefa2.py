cadastro = []

for i in range(4):
    nome = input(f"Digite o nome da {i+1}° pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    cidade = input(f"Digite a cidade de {nome}: ")
    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }
    cadastro.append(pessoa)

print("\n --- CADASTROS: --- ")
for pessoa in cadastro:
    print(f"{pessoa['nome']} tem {pessoa['idade']} anos e mora em {pessoa['cidade']}.")

print(f"\nQuantia de pessoas cadastradas: {len(cadastro)}")

print("\nMaiores de idade:")
maiores_de_idade = False
for pessoa in cadastro:
    if pessoa['idade'] >= 18:
        print(f"{pessoa['nome']} é maior de idade, com {pessoa['idade']} anos")
        maiores_de_idade = True 
if not maiores_de_idade:
    print("Não há maiores de idade.")

soma = 0

for pessoa in cadastro:
    soma += pessoa['idade']

media = soma / len(cadastro)
print(f"A média de idades é: {media:.2f} anos.")

maior_idade = cadastro[0]['idade']
menor_idade = cadastro[0]['idade']

for pessoa in cadastro:
    if pessoa['idade'] > maior_idade:
        maior_idade = pessoa['idade']
    if pessoa['idade'] < menor_idade:
        menor_idade = pessoa['idade']

print(f"A maior idade é: {maior_idade}")
print(f"A menor idade é: {menor_idade}")