palavras = []

for i in range(8):
    p = input(f"Digite a {i+1}° palavra: ")
    palavras.append(p)

buscar = input("Digite uma palavra para buscar: ")

# Verifica se a palavra está na lista.
if buscar in palavras:
    # Conta quantas vezes a palavra aparece na lista.
    vezes = palavras.count(buscar)
    print(f'A palavra "{buscar}" aparece {vezes} vezes.')

    # Utiliza o enumerate() para buscar as posições onde a palavra aparece.
    print("Ela está nas posições: ", end="")

    # Percorre a lista com enumerate() para pegar as posições das palavras.
    for indice, palavra in enumerate(palavras):
        if palavra == buscar:  # Verifica se a palavra na posição atua  l é igual à palavra buscada.
            print(indice, end=" ")  # Se for, imprime a posição (índice) da palavra.
else:
    # Caso a palavra não esteja na lista.
    print(f'A palavra "{buscar}" não está na lista.')