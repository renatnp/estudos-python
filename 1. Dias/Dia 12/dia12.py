# 1. Importando Módulos e usando funções de bibliotecas:
import math  # O módulo 'math' contém várias funções matemáticas (raiz quadrada, potência, pi, etc.).

numero = float(input("Digite um número: "))

# Usa-se a função 'sqrt()' do módulo 'math' para calcular a raiz quadrada.
raiz = math.sqrt(numero)

print(f"A raiz quadrada de {numero} é {raiz:.2f}")

# 'ceil()' = arredonda o número para cima
print(f"Arredondado para cima: {math.ceil(raiz)}")

# 'floor()' = arredonda o número para baixo
print(f"Arredondado para baixo: {math.floor(raiz)}")


# 2. Usando o módulo 'random' para sorteios:
import random  # O módulo 'random' serve para gerar valores aleatórios.

nomes = ['Ana', 'Bruno', 'Carlos', 'Diana']

# A função 'choice()' do módulo 'random' escolhe um item aleatório da lista.
sorteado = random.choice(nomes)

print(f"O nome sorteado foi: {sorteado}")


# 3. Importando só uma função específica:
# Também pode-se importar apenas uma função específica, em vez de todo o módulo.
from math import pow  # Importa somente a função 'pow'

# 'pow(x, y)' = x elevado à potência y. Exemplo: 2³ = 8
resultado = pow(2, 3)

print(f"2 elevado a 3 é {resultado}")


# Resumo dos comandos importantes:
# import math            - importa todo o módulo 'math'.
# math.sqrt(x)           - calcula a raiz quadrada de x.
# math.ceil(x)           - arredonda x para cima.
# math.floor(x)          - arredonda x para baixo.
# import random          - importa o módulo para gerar valores aleatórios.
# random.choice(lista)   - sorteia um item aleatório da lista.
# from math import pow   - importa somente a função 'pow'.
# pow(base, expoente)    - calcula a potência.

# 4. Usando a função 'list()' para criar listas automaticamente:
# A função 'list()' transforma valores "iteráveis" (como uma string, tupla ou range) em uma lista.

# Exemplo 1: transformando um range em lista
numeros = list(range(1, 6))  # Gera a lista [1, 2, 3, 4, 5]
print(f"Lista de 1 a 5: {numeros}")

# Exemplo 2: transformando uma string em lista de letras
palavra = "Python"
letras = list(palavra)  # Gera a lista ['P', 'y', 't', 'h', 'o', 'n']
print(f"Letras da palavra: {letras}")

# Exemplo 3: transformando uma tupla em lista
tupla = (10, 20, 30)
lista_convertida = list(tupla)  # Converte a tupla em lista
print(f"Tupla convertida em lista: {lista_convertida}")