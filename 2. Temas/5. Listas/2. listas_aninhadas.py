# Listas dentro de listas (matrizes, tabelas)

# Cada elemento é uma lista, formando uma matriz 2x3
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

# Acessando elementos (linha 0, coluna 2)
print(matriz[0][2])  # 3

# Percorrendo a matriz com loops aninhados
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # quebra de linha para próxima linha da matriz
