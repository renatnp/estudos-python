# Estruturas de Repetição (Laços)

# 1. FOR
# Repete um bloco de código um número conhecido de vezes
for i in range(5):   # Vai de 0 até 4 (não inclui o 5)
    print("Repetição:", i)

print()  # Pula uma linha no terminal para separar visualmente

# 2. WHILE
# Repete um bloco de código enquanto a condição for verdadeira
contador = 0
while contador < 5:  # Enquanto contador for menor que 5
    print("Contando:", contador)
    contador += 1   # Aumenta o contador em +1 a cada volta

print()

# 3. BREAK
# Encerra o loop na hora
for i in range(10):
    if i == 5:
        break   # Sai do loop quando i for igual a 5
    print(i)

print()

# 4. CONTINUE
# Pula o resto do código dentro do loop e vai para a próxima volta
for i in range(5):
    if i == 2:
        continue   # Quando i for 2, pula e não executa o print
    print(i)

# Observações:
# - range(n) cria uma sequência de 0 até n-1
# - break = parar o loop
# - continue = pular a volta atual e ir pra próxima
