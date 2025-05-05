# Criando uma lista vazia
numeros = []

# Pegando 5 números do usuário com um for
for i in range(5):
    num = int(input(f"Digite o {i + 1}° número: "))
    numeros.append(num)  # Adiciona o número digitado na lista

print(f"Números digitados: {numeros}")

numeros.sort()  # Organiza os itens da lista em ordem crescente
print(f"Lista em ordem crescente: {numeros}")

numeros.reverse()  # Inverte a ordem dos elementos da lista
print(f"Lista invertida: {numeros}")

numeros.sort(reverse=True)  # Organiza em ordem decrescente
print(f"Lista em ordem decrescente: {numeros}")
