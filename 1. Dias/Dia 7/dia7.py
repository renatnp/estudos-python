# 1. Listas aninhadas (listas dentro de listas):

# A lista 'pessoas' é a lista principal.
pessoas = []

pessoas.append(["Ana", 20])  # Sublista ["Ana", 20]: nome = "Ana", idade = 20
pessoas.append(["Carlos", 17])  # Sublista ["Carlos", 17]: nome = "Carlos", idade = 17

# Acessa o nome da primeira pessoa (Ana), que está na sublista [0][0]
print(pessoas[0][0])  # Saída esperada: "Ana"

# Acessando a idade da segunda pessoa (Carlos), que está na sublista [1][1]
print(pessoas[1][1])  # Saída esperada: 17

# Pode-se adicionar quantas sublistas desejar.
pessoas.append(["João", 30])  # Adicionando uma nova pessoa com nome João e idade 30

print(pessoas[2][0])  # Saída esperada: "João"
print(pessoas[2][1])  # Saída esperada: 30

print(pessoas)  # Saída esperada: [['Ana', 20], ['Carlos', 17], ['João', 30]]
