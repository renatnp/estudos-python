def calcular_imposto(preco, porcentagem):
    valor_com_imposto = preco * (1 + porcentagem / 100)
    return valor_com_imposto

produtos = []

for i in range(3):
    nome = input(f"Digite o nome do {i+1}° produto: ")
    preco = float(input(f"Digite o preço de {nome}: "))
    porcentagem = float(input(f"Qual a porcentagem de imposto? "))
    print(" ")
    valor_final = calcular_imposto(preco, porcentagem)
    produto = {
        'nome': nome,
        'preco': preco,
        'porcentagem': porcentagem,
        'valor_final': valor_final 
    }
    produtos.append(produto)

for produto in produtos:
    print(f"Produto: {produto['nome']}")
    print(f"Preço original: R${produto['preco']:.2f}")
    print(f"Preço com imposto: R${produto['valor_final']:.2f}")
    print(" ")