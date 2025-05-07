nomes = []
idades = []

for i in range(6):
    nome = input(f"Digite o {i+1}° nome: ")
    nomes.append(nome)

for i in range(6):
    idade = int(input(f"Digite a idade de {nomes[i]}: "))
    idades.append(idade)

mais_velho = max(idades)                   # Pega a maior idade.
indice = idades.index(mais_velho)          # Pega em que posição está essa idade.
print(f"A pessoa mais veha é {nomes[indice]}, com {mais_velho} anos.") 
# Pega o nome que está na mesma posição da idade.