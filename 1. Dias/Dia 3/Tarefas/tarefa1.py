numero = int(input("Digite um número: "))  # Número é o que o usuário digitou.
for i in range(numero + 1):                # i é o valor que está sendo contado.
    print(f"Contando: {i}")
while numero >= 0:
    print(f"Regredindo: {numero}")
    numero -= 1