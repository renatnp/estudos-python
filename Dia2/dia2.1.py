# 1. Variáveis
# Variáveis de diferentes tipos:
nome = "Maria"           # string: texto
idade = 20               # int: número inteiro
altura = 1.65            # float: número decimal
tem_carteira = True      # bool: valor lógico (True ou False)


# 2. Tipos de Dados
print(type(idade))         # int: Números inteiros.     - 20
print(type(altura))        # float: Números decimais.   - 1.65
print(type(nome))          # str: Texto.                - "Maria"
print(type(tem_carteira))  # bool: Valores lógicos.     - True

# Exemplo de tipos de dados
numero_inteiro = 10     # int
numero_decimal = 3.14   # float
texto = "Olá, Mundo!"   # str
verdadeiro = True       # bool


# 3. Conversão de Tipos (Type Casting): Alterando um tipo de dado para outro
# Ex.: converter string para inteiro
idade_string = "20"          # id: tipo string
idade = int(idade_string)    # Converte string para int


# 4. Entrada com input() - Recebe dados do usuário.
# "input()" retorna um valor como string, então converterei para o tipo desejado.
nome_usuario = input("Digite seu nome: ")               # Recebe nome como string
idade_usuario = int(input("Digite sua idade: "))        # Recebe idade e converte para int
altura_usuario = float(input("Digite sua altura: "))    # Recebe altura e converte para float

# Exibe os dados recebidos com uma "f-string" (uma forma de incluir variáveis dentro de strings):
print(f"Olá, {nome_usuario}! Você tem {idade_usuario} anos e mede {altura_usuario}m.")