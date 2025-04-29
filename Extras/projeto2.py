# Calculadora

n1 = float(input("Número 1: "))
op = input("Operação: ")
n2 = float(input("Número 2: "))

resultado = None

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "*":
    resultado = n1 * n2
elif op == "/":
    if n2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        resultado = n1 / n2
elif op == "%":
    if n2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        resultado = n1 % n2
elif op == "**":
    resultado = n1 ** n2
elif op == "//":
    if n2 == 0:
        print("Divisão por zero não é permitida.")
    else:
       resultado = n1 // n2
else:
    print("Operação inválida (ou ainda não aprendi a adicionar).")

if resultado is not None:
    print(f"Resultado: {resultado}")