filmes = []
for i in range(3):
    titulo = input(f"Digite o título do {i+1}° filme: ")
    diretor = input(f"Qual o diretor deste filme? ")
    ano = int(input(f"Quando lançou o {titulo}? "))
    filme = {
        'titulo': titulo,
        'diretor': diretor,
        'ano': ano
    }
    filmes.append(filme)
for filme in filmes:
    print(f"\n{filme['titulo']}, dirigido por {filme['diretor']}, lançado em {filme['ano']}.")
print("\n --- Filmes lançados antes de 2010: --- ")
for filme in filmes:
    if filme['ano'] < 2010:
        print(f"{filme['titulo']}")
soma = 0
for filme in filmes:
    soma += filme['ano']
media = soma / len(filmes)
print(f"\nMédia do ano de lançamento dos filmes cadastrados: {media:.2f}")
