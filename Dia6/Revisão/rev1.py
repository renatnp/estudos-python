notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
soma = sum(notas)
média = soma / len(notas)
print(f"A média das notas é: {média:.2f}")