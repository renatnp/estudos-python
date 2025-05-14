def avaliar_alunos(nota, frequencia):
    if nota >= 7 and frequencia >= 75:
        return "Aprovado"
    else:
        return "Reprovado"
alunos = []
for i in range(3):
    nome = input(f"Digite o nome do {i+1}° aluno: ")
    nota = float(input(f"Digite a nota de {nome} (0 a 10): "))
    frequencia = int(input(f"Digite a nota de {nome} (0 a 100): "))
    aluno = {
        'nome': nome,
        'nota': nota,
        'frequencia': frequencia,
        'status': avaliar_alunos(nota, frequencia)
    }
    alunos.append(aluno)
print("Relatório Final:")
for aluno in alunos:
    print(f"Aluno: {aluno['nome']}")
    print(f"Nota: {aluno['nota']}")
    print(f"Frequência: {aluno['frequencia']}")
    print(f"Status: {aluno['status']}")
    print(" ")