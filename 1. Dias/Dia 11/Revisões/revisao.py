def calcular_frete(peso, distancia):
    frete = (peso * 0.5) + (distancia * 8)
    return frete

clientes = []

for i in range(3):
    nome = input(f"Digite o {i+1}° nome: ")
    tipo = input("Qual o tipo do produto? ")
    peso = int(input("Informe o peso do produto (kg): "))
    distancia = int(input("Distância da entrega (km): "))
    print(" ")
    frete = calcular_frete(peso, distancia)
    cliente = {
        'nome': nome,
        'tipo': tipo,
        'peso': peso,
        'distancia': distancia,
        'frete': frete
    }
    if frete > 300:
        cliente['status'] = "Frete caro"
    clientes.append(cliente)
print("\nRelatório de Entregas:")
for cliente in clientes:
    print(f"Cliente: {cliente['nome']}")
    print(f"Produto: {cliente['tipo']}")
    print(f"Frete: {frete}")
    print(f"Status: {cliente.get('status', 'Frete normal')}")