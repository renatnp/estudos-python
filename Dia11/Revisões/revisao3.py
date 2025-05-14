def calcular_bonus(vendas):
    valor = (vendas * 0.1) + vendas
    return valor
cadastro = []
for i in range(3):
    nome = input(f"Digite o nome do {i+1}° vendedor: ")
    vendas = float(input(f"Digite o total de vendas de {nome}: "))
    bonus = input("Participa do bônus? (sim ou não): ")
    print(" ")
    vendedor = {
        'nome': nome,
        'vendas': vendas,
    }
    if bonus == "sim":
        vendedor['bonus'] = calcular_bonus(vendas)
    if vendas > 10000:
        vendedor['status'] = "Top vendedor"
    cadastro.append(vendedor)
print("Relatório de Vendedores:")
for vendedor in cadastro:
    print(f"Vendedor: {vendedor['nome']}")
    print(f"Valor total de vendas: {vendedor['vendas']}")
    print(f"Bônus: {vendedor.get('bonus', 'Sem bônus')}")
    print(f"Status: {vendedor.get('status', 'Normal')}")
    print(" ")