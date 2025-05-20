# 1. Função que recebe uma lista como parâmetro:
# Esta função percorre uma lista de dicionários e exibe nome e preço de cada produto
def exibir_produtos(lista):
    for produto in lista:
        print(f"{produto['nome']} custa R${produto['preco']:.2f}")

produtos = [
    {'nome': 'Mouse', 'preco': 50.0},
    {'nome': 'Teclado', 'preco': 120.0},
    {'nome': 'Monitor', 'preco': 750.0}
]

exibir_produtos(produtos)

# 2. Função que retorna um dicionário:
# Essa função cria um dicionário com dados de um contato e o devolve
def criar_contato(nome, telefone):
    contato = {
        'nome': nome,
        'telefone': telefone
    }
    return contato  # devolve o dicionário criado

# Chamando a função e armazenando o retorno em uma variável
novo = criar_contato("Laura", "1199999-9999")
print(novo)

# 3. Função com mais de dois parâmetros:
# Essa função recebe título, autor e ano, e devolve um dicionário representando um livro
def cadastrar_livro(titulo, autor, ano):
    return {
        'título': titulo,
        'autor': autor,
        'ano': ano
    }

livro1 = cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899)
print(livro1)