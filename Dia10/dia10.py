# 1. Função simples (sem parâmetros):
def saudacao():  # Define uma função chamada "saudacao".
    print("Olá!")  # Esta mensagem só será exibida quando a função for chamada.

saudacao()  # Aqui chama-se a função para executar o que está dentro dela.

# 2. Função com parâmetro:
def apresentar(nome):  # "nome" é um parâmetro (espaço reservado para um valor).
    print(f"Olá, {nome}!")  # A função usa o valor do parâmetro para personalizar a mensagem.

apresentar("Ana")     # "Ana" é o argumento que preenche o parâmetro "nome".
apresentar("Carlos")  # Cada chamada pode usar um nome diferente.

# 3. Função com retorno de valor:
def somar(a, b):  # Função com dois parâmetros: "a" e "b".
    return a + b  # Retorna ("devolve") o resultado da soma para quem chamou a função

# Podemos guardar o valor retornado em uma variável
resultado = somar(3, 4)  # A função executa a soma 3 + 4 e retorna 7
print("Resultado da soma:", resultado)  # Exibe o resultado retornado pela função