livros = []
for i in range(3):
    titulo = input(f"Digite o título do {i+1}° livro: ")
    autor = input(f"Digite o nome do autor de {titulo}: ")
    ano = input(f"Digite o ano de publicação de {titulo}: ")
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }
    livros.append(livro)
print("\n --- LIVROS CADASTRADOS: --- ")
for livro in livros:
    print(f"{livro['titulo']}, de {livro['autor']}, ({livro['ano']}).")