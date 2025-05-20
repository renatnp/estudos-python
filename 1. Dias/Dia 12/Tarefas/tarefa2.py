import random

# Lista de números de 1 a 50
lista = list(range(1, 51))

sorteio = random.choice(lista)

tentativa = int(input("Adivinhe o número sorteado (entre 1 e 50): "))

if tentativa == sorteio:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena! Você errou. O número era {sorteio}.")
