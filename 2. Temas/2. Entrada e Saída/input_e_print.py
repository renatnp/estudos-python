# Entrada de dados com input() e saída com print()

nome = input("Digite seu nome: ")            # input sempre retorna string
idade = int(input("Digite sua idade: "))     # converte para inteiro com int()

print(f"Olá {nome}, você tem {idade} anos.")

# ---------------------------------------------------------------

# Exemplo do uso da função print e do parâmetro 'end'

print("Primeira linha")          # Por padrão, print adiciona uma quebra de linha no final
print("Segunda linha")

print("Sem quebra de linha", end=" ")  # Usando end=" " para não quebrar linha, mas colocar espaço
print("continuação da mesma linha")
