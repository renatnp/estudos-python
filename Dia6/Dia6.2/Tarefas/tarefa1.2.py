lista = []
for i in range(6):
    n = int(input(f"Digite seu {i+1}° número: "))
    lista.append(n)
num = int(input("Digite um número para buscar: "))
if num in lista:
    print(f"O número {num} está na lista e aparece {lista.count(num)} vezes.")
else:
    print(f"O número {num} não está na lista.")