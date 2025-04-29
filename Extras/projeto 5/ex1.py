from ex2 import Calculo
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ano = 2025

cemanos = Calculo(idade, ano)

print(f"Olá {nome}!\nVocê terá 100 anos em {cemanos}")
