produtos = []
for i in range(4):
    nome = input(f"Digite o nome de seu {i+1}° produto: ")
    preço = float(input(f"Digite o preço do(a) {nome}: "))
    categoria = input(f"Qual a categoria do(a) {nome}: ")
    produto = {
        'nome': nome,
        'preço': preço,
        'categoria': categoria
    }
    produtos.append(produto)

soma = 0
for produto in produtos:
    soma += produto['preço']

media = soma / len(produtos)

print("\n --- PRODUTOS CADASTRADOS: --- ")
for produto in produtos:
    print(f"{produto['nome']} ({produto['categoria']}) - R${produto['preço']:.2f}")

print(f"\nSoma dos produtos: R${soma:.2f}")
print(f"Média de preço: R${media:.2f}")

mais_caro = produtos[0]
mais_barato = produtos[0]

for produto in produtos:
    if produto['preço'] > mais_caro['preço']:
        mais_caro = produto
    if produto['preço'] < mais_barato['preço']:
        mais_barato = produto

print(f"\nProduto mais caro: {mais_caro['nome']} - R${mais_caro['preço']:.2f}")
print(f"Produto mais barato: {mais_barato['nome']} - R${mais_barato['preço']:.2f}")