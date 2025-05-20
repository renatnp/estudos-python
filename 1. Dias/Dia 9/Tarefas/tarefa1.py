cadastro = []

for i in range(3):
    nome = input(f"Digite o {i+1}° nome: ")
    cargo = input(f"Digite o cargo de {nome}: ")
    salario = float(input(f"Digite o salário de {nome}: "))
    pessoa = {
        'nome': nome,
        'cargo': cargo,
        'salario': salario
    }
    cadastro.append(pessoa)

print("\n--- ANÁLISE DE SALÁRIOS ---")
for pessoa in cadastro:
    if pessoa['salario'] > 3000.00:
        print(f"{pessoa['nome']} tem salário alto: R${pessoa['salario']:.2f}")
    else:
        print(f"{pessoa['nome']} tem um salário mediano: R${pessoa['salario']:.2f}")

for pessoa in cadastro:
    if pessoa['salario'] > 5000.00:
        pessoa['status'] = "Bônus"

print("\n--- RESUMO FINAL ---")
for pessoa in cadastro:
    print(f"{pessoa['nome']} é {pessoa['cargo']} e recebe R${pessoa['salario']:.2f} ({pessoa.get('status', 'Sem bônus')})")