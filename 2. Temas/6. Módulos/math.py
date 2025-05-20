# Usando funções do módulo math
import math

num = float(input("Digite um número: "))

raiz = math.sqrt(num)  # raiz quadrada
print(f"Raiz quadrada de {num} é {raiz:.2f}")

# Arredondar para cima
print(f"Arredondado para cima: {math.ceil(raiz)}")

# Arredondar para baixo
print(f"Arredondado para baixo: {math.floor(raiz)}")

# Número pi:
print(f"Pi: {math.pi}")

# Importando função específica
from math import pow
print(f"2 elevado a 3 é {pow(2,3)}")
