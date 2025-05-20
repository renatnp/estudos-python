from math import pow

def elevar(base, expoente):
    resultado = pow(base, expoente)
    return resultado

print("Calculadora de Potências:\n")

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
print(" ")

calculo = elevar(base, expoente)

print(f"Resultado: {calculo}")
