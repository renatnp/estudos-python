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