nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
print(f"Nome: {nome} | Idade: {idade} anos | Altura: {altura}m")

if idade > 18:
    print("Você é maior de idade!")
elif idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem 18 anos.")

for i in range(idade + 1):
    print(f"Contando: {i}")

while idade >= 0:
    print(f"Regredindo: {idade}")
    idade -= 1
