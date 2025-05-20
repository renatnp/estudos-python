# Entrada sempre é string, então convertemos para número se necessário
idade_str = input("Digite sua idade: ")
idade_int = int(idade_str)        # Converte string para inteiro

altura_str = input("Digite sua altura em metros (ex: 1.75): ")
altura_float = float(altura_str)  # Converte string para float

print(f"Idade + 5 = {idade_int + 5}")
print(f"Altura + 0.1 = {altura_float + 0.1}")
