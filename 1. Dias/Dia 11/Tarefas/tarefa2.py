def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

filmes = []
for i in range(3):
    nome = input(f"Nome do {i+1}° filme: ")
    nota1 = int(input("Sua primeira nota: "))
    nota2 = int(input("Sua segunda nota: "))
    nota3 = int(input("Sua terceira nota: "))
    print(" ")
    media = calcular_media(nota1, nota2, nota3)
    filme = {
        'nome': nome,
        'media': media
    }
    filmes.append(filme)

for filme in filmes:
    print(f"Filme: {filme['nome']}")
    print(f"Média das avaliações: {filme['media']:.2f}")