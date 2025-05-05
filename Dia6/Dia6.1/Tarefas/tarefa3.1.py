vendas = []
for i in range(7):
    venda = float(input(f"Digite o valor da venda do dia {i+1}:"))
    vendas.append(venda)

print(f"Vendas: {vendas}")

print(f"Maior valor: {max(vendas)}")
print(f"Menor valor: {min(vendas)}")

soma = sum(vendas)
media = soma / len(vendas)
print(f"Média: {media:.2f}")

vendas.sort()
print(f"Valores em ordem crescente: {vendas}")
vendas.sort(reverse=True)
print(f"Valores em ordem decrescente: {vendas}")

