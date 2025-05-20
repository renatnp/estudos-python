presentes = []
for i in range(5):
    nome = input("Digite um nome: ")
    presentes.append(nome)
n = input("Digite um nome para buscar: ")
if n in presentes:
    print("O nome está na lista de presença")
else:
    print("O nome não está na lista de presença")