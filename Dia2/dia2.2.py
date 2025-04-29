# 1. Operadores Aritméticos
a = 10
b = 3

print("Soma:", a + b)                
print("Subtração:", a - b)           
print("Multiplicação:", a * b)       
print("Divisão:", a / b)             
print("Divisão inteira:", a // b)    
print("Resto da divisão:", a % b)    
print("Potência:", a ** b)           



# 2. Operadores Relacionais
x = 5
y = 10

print(x == y)   # Igual? → False
print(x != y)   # Diferente? → True
print(x < y)    # Menor? → True
print(x > y)    # Maior? → False
print(x <= y)   # Menor ou igual? → True
print(x >= y)   # Maior ou igual? → False



# 3. Operadores Lógicos
print(True and False) # AND: só dá True se os dois forem True → False
print(True or False)  # OR: dá True se pelo menos um for True → True
print(not True)       # NOT: inverte o valor → False



# 4. Condicional if, elif e else
idade = 18             

if idade < 18:                         # Verifica se a idade é menor que 18
    print("Menor de idade")
elif idade == 18:                      # Se não for menor, verifica se é igual a 18
    print("Tem exatamente 18 anos")
else:                                  # Se não for nenhuma das anteriores, é maior de 18
    print("Maior de idade")
