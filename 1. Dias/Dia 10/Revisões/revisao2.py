funcionarios = []
for i in range(4):
    nome = input(f"Digite o nome do {i+1}° funcionário: ")
    cargo = input(f"Digite o cargo de {nome}: ")
    salario = float(input(f"Digite o salário de {nome}: "))
    bonus = input(f"Participa do sistema de bônus (sim ou não): ")
    funcionario = {
        'nome': nome,
        'cargo': cargo,
        'salario': salario
    }
    if funcionario['salario'] > 5000:
        funcionario['status'] = "Alto salário"
    if bonus == 'sim':
        funcionario['bonus'] = "Ativo"
    funcionarios.append(funcionario)
print("\nRelatório Final:")
for funcionario in funcionarios:
    print(f"{funcionario['nome']} é {funcionario['cargo']} e ganha R${funcionario['salario']:.2f}.")
    print(f"Bônus: {funcionario.get('bonus', 'Não participa')}.")
    print(f"Status: {funcionario.get('status', 'Normal')}.\n")