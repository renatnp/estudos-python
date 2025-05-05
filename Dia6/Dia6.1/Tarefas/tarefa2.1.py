num = []
for i in range(10):
    n = int(input(f"Digite o {i+1}° número: "))
    num.append(n)
print(f"Maior valor: {max(num)}")
print(f"Menor valor: {min(num)}")
soma = sum(num)
print(f"Soma dos números: {soma}")
media = soma / len(num)
print(f"Média dos números: {media:.2f}")