produtos = []
for i in range(4):
    nome = input(f"Digite o nome de seu {i+1}° produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite o estoque do produto: "))
    produto = {
        'nome': nome,
        'preco': preco,
        'estoque': estoque
    }
    produtos.append(produto)

for produto in produtos:
    if produto['estoque'] == 0:
        print(f"{produto['nome']} está fora de estoque.")

for produto in produtos:
    if produto['estoque'] <= 5:
        produto['Reposição'] = "Reposição urgente"

print("\n--- RELATÓRIO DE PRODUTOS ---")
for produto in produtos:
    observacao = produto.get('Reposição', 'Reposição não necessária')
    print(f"{produto['nome']}, com preço R${produto['preco']:.2f}, tem estoque de {produto['estoque']}. Obs.: {observacao}.")