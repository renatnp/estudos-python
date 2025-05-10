def calculadora_frete(peso, distancia):
    frete = peso * 0.50 + distancia * 0.10
    return frete

dados = []

for i in range(3):
    nome = input("Digite seu nome: ")
    pesov = float(input(f"Digite o peso da {i+1}° carga (em kg): "))
    distanciav = int(input("Digite a distância da carga (em km): "))
    
    pessoa = {
        'nome': nome,
        'peso': pesov,
        'distancia': distanciav
    }
    dados.append(pessoa)

for pessoa in dados:
    valor_frete = calculadora_frete(pessoa['peso'], pessoa['distancia'])
    print(f"{pessoa['nome']}, será cobrado R$ {valor_frete:.2f} pelo frete.")
