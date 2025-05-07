notas = []

# Coleta 5 notas do usuário e adicionando à lista.
for i in range(5):
    nota = float(input(f"Digite a {i + 1}° nota: "))
    notas.append(nota)

print(notas)

# Mostra cada nota individualmente com a posição.
for i in range(len(notas)):
    print(f"Nota {i + 1}: {notas[i]}")

# Calcula a média.
soma = sum(notas)  # A função sum() soma todos os valores de uma lista.
media = soma / len(notas)  # Divide pela quantidade de notas.

# Mostra a média
print(f"A média das notas é: {media:.2f}")  # .2f deixa com 2 casas decimais.

# Mostra quantas notas foram digitadas.
print(f"Você digitou {len(notas)} notas.")
