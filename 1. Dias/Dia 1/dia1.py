# 1. Variáveis e Operações

# Define variáveis:
nome = "João"     # Nome da pessoa.
idade = 16        # Idade da pessoa.
altura = 1.80     # Altura da pessoa.

# Exibe as variáveis no console:
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)

# Definindo várias variáveis de uma vez:
x, y, z = "Banana", "Maçã", "Cereja"
print(x)  # Mostra Banana
print(y)  # Mostra Maçã
print(z)  # Mostra Cereja

# Um valor para várias variáveis:
a = b = c = "Laranja"
print(a)  # Mostra Laranja
print(b)  # Mostra Laranja
print(c)  # Mostra Laranja

# Operações com variáveis:
soma = 10 + 5             # Soma de dois números.
multiplicacao = 4 * 3     # Multiplicação de dois números.

# Exibe os resultados das operações:
print("Soma: ", soma)
print("Multiplicação: ", multiplicacao)



# 2. Estruturas de Controle (Condicionais e Loops):
# Condicional (If-Else):
# Verifica se a pessoa é maior ou menor de idade.
if idade <= 17:
    print("Você é menor de idade!")
else:
    print("Você é maior de idade.")

# Loop com 'for':
# O 'for' imprime números de 1 até 4 (não inclui o 5).
for i in range(1, 5):
    print("Número:", i)

# Loop com 'while':
# O 'while' imprime números de 1 até 5 (inclusive).
contador = 1
while contador <= 5:
    print("Número:", contador)
    contador += 1    # Incrementa 1 ao contador a cada repetição.