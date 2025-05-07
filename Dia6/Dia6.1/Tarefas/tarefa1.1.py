valores = []
for i in range(6):
    v = int(input(f"Digite o {i+1}° valor: "))
    valores.append(v)
print(f"Valores digitados: {valores}")
valores.sort()
print(f"Lista em ordem crescente: {valores}")
valores.reverse()
print(f"Lista invertida: {valores}")
valores.sort(reverse=True)
print(f"Lista em ordem decrescente: {valores}")

# Mostra o maior valor da lista.
print(f"Maior valor: {max(valores)}")

# Mostra o menor valor da lista.
print(f"Menor valor: {min(valores)}")